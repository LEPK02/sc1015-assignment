import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from boruta import BorutaPy


class PreProcessor:
    def __init__(self, X, y, encode='label', preserve_cols=['team', 'opponent', 'country'], passthrough_cols=['is_home']):
        assert encode in ['label', 'onehot', None], "Values of encode can only be label, onehot, or None"
        self.X = X
        self.y = y
        self.preserve_cols = preserve_cols
        self.passthrough_cols = passthrough_cols
        self.target_encoder = LabelEncoder() if encode == 'label' else OneHotEncoder() if encode == 'onehot' else None
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
        self.preprocess(encode)

    def preprocess(self, encode):

        # ENCODING FOR Y VALS
        if encode == 'label':
            self.y_train_encoded = self.target_encoder.fit_transform(self.y_train)
            self.y_test_encoded = self.target_encoder.transform(self.y_test)
        elif encode == 'onehot':
            self.target_encoder = OneHotEncoder(sparse=False)
            self.y_train_encoded = self.target_encoder.fit_transform(self.y_train.to_numpy().reshape(-1, 1)).toarray()
            self.y_test_encoded = self.target_encoder.transform(self.y_test.to_numpy().reshape(-1, 1)).toarray()
        else:
            self.y_train_encoded = self.y_train
            self.y_test_encoded = self.y_test
        # Adjust feature type identification based on preserved columns
        num_features = self.X_train.select_dtypes(include=[np.number]).columns.difference(self.preserve_cols + self.passthrough_cols)
        cat_features = self.X_train.select_dtypes(exclude=[np.number]).columns.difference(self.preserve_cols + self.passthrough_cols)
        
        # Update ColumnTransformer setup based on dynamically identified features
        self.preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), num_features),
                ('cat', OneHotEncoder(), cat_features),
                ('pass', 'passthrough', self.passthrough_cols)
            ])
        
        self.fit_transform()

    def fit_data_to_predict(self, df):
        df_preprocessed = self.preprocessor.transform(df.drop(columns=self.preserve_cols))
        df_preprocessed = pd.DataFrame(df_preprocessed, columns=self.get_feature_names(), index=df.index)
        return pd.concat([df_preprocessed, df[self.preserve_cols]], axis=1)
         

    def fit_transform(self):
        '''applies the preprocessing to the train and test features, except for the preserved features. It then retrieves the feature names and creates the dataframes that can be used by other models. To get the dataframes with the preserved columns, use get_processed_data()'''
        # Apply transformations without preserved columns
        df_train_preprocessed = self.preprocessor.fit_transform(self.X_train.drop(columns=self.preserve_cols))
        df_test_preprocessed = self.preprocessor.transform(self.X_test.drop(columns=self.preserve_cols))

        feature_names = self.get_feature_names()
        
        # Create processed DataFrames without preserved columns
        self.df_train_preprocessed = pd.DataFrame(df_train_preprocessed, columns=feature_names, index=self.X_train.index)
        self.df_test_preprocessed = pd.DataFrame(df_test_preprocessed, columns=feature_names, index=self.X_test.index)

    def get_feature_names(self):
        feature_names = []

        for name, transformer, features in self.preprocessor.transformers_:
            if isinstance(features, list) and len(features) == 0 or isinstance(features, (pd.Index, pd.Series)) and features.empty:
                continue
            if name == 'num' or name == 'cat':
                if hasattr(transformer, 'get_feature_names_out'):
                    feature_names.extend(transformer.get_feature_names_out(features))
                else:
                    feature_names.extend(features)
            elif name == 'pass':
                feature_names.extend(features)
        return feature_names

    def get_processed_data(self):
        '''returns as dataframes the preprocessed data, with the preserved columns. Can further filter to only include boruta features later on'''
        return pd.concat([self.df_train_preprocessed, self.X_train[self.preserve_cols]], axis=1), \
            pd.concat([self.df_test_preprocessed, self.X_test[self.preserve_cols]], axis=1), \
            self.y_train_encoded, self.y_test_encoded
    
class Boruta():

    def __init__(self):
        np.int = np.int32
        np.float = np.float64
        np.bool = np.bool_
        self.rf = RandomForestClassifier(n_jobs=-1, class_weight='balanced', max_depth=5)
        self.boruta = BorutaPy(self.rf, n_estimators='auto', verbose=2, random_state=1)
        self.selected_features = []

    def fit(self, df_train_preprocessed, y_train):
        '''fits the models onto the train dataset, does not include the preserved columns'''
        # Fit Boruta
        self.boruta.fit(df_train_preprocessed.values, y_train.values)
        self.selected_features = df_train_preprocessed.columns[self.boruta.support_].tolist()

    def get_selected_features(self):
        return self.selected_features