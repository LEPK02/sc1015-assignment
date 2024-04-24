# Predicting Football Results Using Machine Learning
by Luke, Rachmiel, and Billie (FCEA Team 6)

### Setting Up the Project Locally
Clone the Repository
```git clone https://github.com/LEPK02/sc1015-assignment.git```
Navigate to the Project Directory
```cd sc1015-assignment```
Create the Conda Environment
```conda env create -f environment.yml```
Activate the Conda Environment
```conda activate sc1015```

## Workflow: Running the project

### 1. Data collection via webscraping (./webscraping)
- [teams_data_fbref.ipynb](./webscraping/teams_data_fbref.ipynb) (inspired by [Parth Athale](https://github.com/parth1902/Scrape-FBref-data)) -> pull season data from [FBRef](https://fbref.com/en/) using **Beautiful Soup**
    - Gather season data from top 5 leagues
        - Find all teams
        - Find table using HTML tags
        - Iterate through all tables and combine into one dataframe
    - If team is newly promoted (i.e. no previous season's data), gather data from league they were promoted from
        - Get page for league below
        - Repeat steps above and pull data for newly promoted team
    - Handle HTTP 429
- [scores_football_data.ipynb](./webscraping/scores_football_data.ipynb) -> pull match scores from [Flashscore](https://www.flashscore.com/) using **Playwright**
    - Gather match scores from top 5 leagues
        - Find div element holding data
        - Extract timestamp
    - Gather fixtures (matches to be played) for current season (2023-24)
    - Gather league table for current season (2023-24) so that we can evaluate our predictions for current season
- [squad_values_transfermarkt.ipynb](./webscraping/squad_values_transfermarkt.ipynb) -> pull season data from [Transfermarkt](https://www.transfermarkt.com/) using **Beautiful Soup**
    - Gather season data from top 5 leagues
        - Find all teams
        - Find table using HTML tags
        - Iterate through all tables and combine into one dataframe
        - Save club icons as .png files
- Save raw data as .csv

### 2. Clean data [01_data_processing.ipynb](./01_data_processing.ipynb)
- Combine data across competitions and years using inner join (drop duplicate columns)
    - Resolve team name conflicts
    - Drop missing data
- Remove promotion playoff results from scores dataframe
- Combine score data to get season statistics
- Combine squad value data into team dataframe (requires name mapping as data is pulled from different sources)
- Save cleaned and combined data as .csv files

### 3. Exploratory data analysis [02_exploratory_analysis.ipynb](./02_exploratory_analysis.ipynb)
- Methodology
    - Examine correlations
    - Observe trends/patterns
    - Find extremes/outliers
    - Visualise data
    - Draw hypotheses
- Evaluation: correlations between Points Per Game (PPG) and:
        - Goals Scored, Conceded
        - Possession
        - Squad Value

### 4. Feature Selection from over 250 features [03_feature_selection.ipynb](./03_feature_selection.ipynb)
- Methodology
    - Correlation: Drop highly correlated features; prevent redundancy and multicollinearity in the model.
    - Logistic Regression: Drop features that are not significant in predicting 'W', 'L, and 'D'
    - Boruta Algorithm: Drop features that are not relevant to the outcome using Random Forest.

### 5. Conduct models and make predictions [04_machine_learning.ipynb](./04_machine_learning.ipynb)
- Using Classification Algorithms
    - Logistic Regression
    - Decision Tree
    - Random Forest
    - Extra Trees
    - Gradient Boosting
    - Naive Bayes
    - K-Neighbors
    - Support Vector

### 6. Conduct Deep Learning and make predictions [05_deep_learning.ipynb](./05_deep_learning.ipynb)
- Chosen model: Long-Short Term Memory (LSTM)
    - Games are played sequentially and we can store memory of previous games when predicting the outcome

### 7. Evaulation Models [06_model_evaluation.ipynb](./06_model_evaluation.ipynb)
- Compare the results of the 8 classification models and the LSTM model.
    - Accuracy, Precision, Recall, F1-Score

## Data Directory Structure

The `data` directory contains several subdirectories. Below is the hierarchy and description of each subdirectory and its contents:

```
data/
├── club icons/
├── country icons/
├── exploratory analysis/
│   ├── eda_prev_season.csv
|   └── eda_same_season.csv
├── machine_learning/
|   ├── outcome/ 
|   ├── scoreline/ 
|   ├── tables/ 
│   ├── predictions/ 
|   ├── lstm_metrics.csv
|   ├── model_metrics.csv
|   └── 2023_predict.csv
├── scores/
│   ├── raw/
│   ├── scores.csv
│   └── results.csv
├── squad values/
│   ├── raw/
│   └── squad_values.csv
└── teams/
    ├── raw/ 
    ├── teams_agg.csv
    └── teams.csv
```

### Club Icons
Contains icons for different clubs (used in EDA).

### Country Icons
Contains icons for different countries (used in EDA).

### Exploratory Analysis (Currently idle)
This folder is intended for storing datasets used in exploratory data analysis, but might be deleted as it uses teams_agg.csv :
- `eda_prev_season.csv`: Results based on past performance
- `eda_same_season.csv`: Results based on current performance

### Machine Learning
Contains data prepared for feeding into machine learning algorithms, and data on predicted results:
- `outcome/`: Features with single categorical label of 'W', 'D', 'L'
- `scoreline/`: Features with two numeric labels of 'score', 'opponent_score'
- `tables/`: Stores the current season tables (which are still in progress)
- `predictions/`: Stores the predicted results of current season by the models
- `lstm_metrics.csv`: Metrics of LSTM model
- `model_metrics.csv`: Metrics of classification models
- `2023_predict.csv`: Features of each match to be predicted (unlabelled data)

### Scores
Contains both raw and aggregated data for matches played over the seasons:
- `raw/`: Scores from each season (2019-2023)
- `scores.csv`: Combined from raw/
- `results.csv`: Overview of results from scores.csv (ie. W, D, L, GF, GA, GD etc)

### Squad Values
Contains data on the valuation of teams' squads:
- `raw/`: Squad values from each season (2019-2023)
- `squad_values.csv`: Combined from raw/

### Teams
Data related to team details and performance:
- `raw/`: Contains season-specific team performance data.
- `teams.csv`: Combined team performance data over the seasons.
- `teams_agg.csv`: Contains only the aggregated data (eg. average per90 data of features) for the teams over the seasons → Used for EDA and Feature Engineering

## Telegram Workflow Bot
Sends notification on push/PR ([setup](https://cyaninfinite.com/getting-updates-from-github-via-telegram-bot/))

## References
- Webscraping:
  - Fbref for team performance: https://fbref.com/en/
  - Flashscore for team results: https://www.flashscore.com/
  - Transfermarkt for team squad values: https://www.transfermarkt.com/
- Data processing
  - COVID cancels Ligue 1 2019-20: https://www.cbssports.com/soccer/news/ligue-1-season-called-off-after-french-pm-edouard-philippe-bans-all-sporting-events-until-september/
  - Extra game for Italy 2022-23: https://www.90min.com/posts/spezia-vs-hellas-verona-everything-you-need-to-know-serie-a-relegation-play-off
  - Missing game for Italy 2023-24: https://onefootball.com/en/news/atalanta-vs-fiorentina-might-not-be-played-until-june-39340806
- Feature Selection:
   - Boruta Algorithm: https://www.sciencedirect.com/science/article/pii/S1877050922007955
- Machine Learning 
  - Classification Algorithms: https://towardsdatascience.com/top-10-binary-classification-algorithms-a-beginners-guide-feeacbd7a3e2
- Deep Learning
  - LSTM for football predictions: https://www.sciencedirect.com/science/article/pii/S2352864821000602

## Contributors
- Rachmiel: Model, Webscraping, Data Processing, Presentation
- Luke: EDA, Webscraping, Data Processing, Presentation
- Billie: Quality Assurance
