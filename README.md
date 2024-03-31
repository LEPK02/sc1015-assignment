# Predicting EPL Results Using Machine Learning
## Workflow
1. Data collection via webscraping (./webscraping)
- teams_data_fbref.ipynb (inspired by [Parth Athale](https://github.com/parth1902/Scrape-FBref-data)) -> pull season data from [FBRef](https://fbref.com/en/) using Beautiful Soup
    - Gather season data from top 5 leagues
        - Find all teams
        - Find table using HTML tags
        - Iterate through all tables and combine into one dataframe
    - If team is newly promoted (i.e. no previous season's data), gather data from league they were promoted from
        - Get page for league below
        - Repeat steps above and pull data for newly promoted team
    - Handle HTTP 429
- scores_football_data.ipynb -> pull match scores from [Flashscore](https://www.flashscore.com/) using Playwright
    - Gather match scores from top 5 leagues
        - Find div element holding data
        - Extract timestamp
- squad_values_transfermarkt.ipynb -> pull season data from [FBRef](https://fbref.com/en/) using Beautiful Soup
    - Gather season data from top 5 leagues
        - Find all teams
        - Find table using HTML tags
        - Iterate through all tables and combine into one dataframe
        - Save club icons as .png files
- Save raw data as .csv
2. Clean data (data_processing.ipynb)
- Combine data across competitions and years using inner join (drop duplicate columns)
    - Resolve team name conflicts
    - Drop missing data
- Remove promotion playoff results from scores dataframe
- Combine score data to get season statistics
- Combine squad value data into team dataframe (requires name mapping as data is pulled from different sources)
- Save cleaned and combined data as .csv files
3. Exploratory data analysis (exploratory_analysis.ipynb)
- Methodology
    - Examine correlations
    - Observe trends/patterns
    - Find extremes/outliers
    - Visualise data
    - Draw hypotheses
- Summary
    - Strong correlations
        - Positive
            - Points Per Game (PPG) & posession
            - PPG & squad value
            - PPG & goals scored
        - Negative
            - PPG & goals conceded
    - Weak correlations
        - Positive
            - PPG & tackles in attacking third - high press is not always better
            - PPG & goals per shot on target - more important to have more shots
        - Negative
            - PPG & tackles in defensive third, PPG & blocked shots - higher-volume of last-ditch defending may not always be indicative of wins because another way of defending is to prevent those chances from happening in the first place
4. Conduct models and make predictions (machine_learning.ipynb)

## Telegram Workflow Bot
Sends notification on push/PR ([setup](https://cyaninfinite.com/getting-updates-from-github-via-telegram-bot/))

## Contributors
Rachmiel - Model, Webscraping, Data Processing, Presentation
Luke - EDA, Webscraping, Data Processing, Presentation
Billie - Quality assurance
