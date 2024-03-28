# Columns pulled from team tables
DROPPED = [
    'pass_xa', 'ball_recoveries', 'aerials_lost', 'progressive_passes', 'npxg_per_shot',
    'progressive_carries', 'progressive_passes_received', 'xg_per90', 'npxg_xg_assist_per90',
    'aerials_won_pct', 'npxg_per90', 'npxg_xg_assist', 'xg_xg_assist_per90', 'xg', 'npxg_net',
    'xg_assist', 'xg_assist_per90', 'xg_net', 'npxg', 'aerials_won', 'shots_free_kicks'
]
STANDARD = [
    'players_used', 'avg_age', 'possession', 'games',
    'games_starts', 'minutes', 'minutes_90s', 'goals', 'assists',
    'goals_assists', 'goals_pens', 'pens_made', 'pens_att', 'cards_yellow',
    'cards_red', 'xg', 'npxg', 'xg_assist', 'npxg_xg_assist',
    'progressive_carries', 'progressive_passes', 'goals_per90',
    'assists_per90', 'goals_assists_per90', 'goals_pens_per90',
    'goals_assists_pens_per90', 'xg_per90', 'xg_assist_per90',
    'xg_xg_assist_per90', 'npxg_per90', 'npxg_xg_assist_per90'
]
GOALKEEPING = [
    'players_used', 'gk_games', 'gk_games_starts', 'gk_minutes',
    'minutes_90s', 'gk_goals_against', 'gk_goals_against_per90',
    'gk_shots_on_target_against', 'gk_saves', 'gk_save_pct', 'gk_wins',
    'gk_ties', 'gk_losses', 'gk_clean_sheets', 'gk_clean_sheets_pct',
    'gk_pens_att', 'gk_pens_allowed', 'gk_pens_saved', 'gk_pens_missed',
    'gk_pens_save_pct'
]
ADVANCED_GOALKEEPING = [
    'players_used', 'minutes_90s', 'gk_goals_against',
    'gk_pens_allowed', 'gk_free_kick_goals_against',
    'gk_corner_kick_goals_against', 'gk_own_goals_against', 'gk_psxg',
    'gk_psnpxg_per_shot_on_target_against', 'gk_psxg_net',
    'gk_psxg_net_per90', 'gk_passes_completed_launched',
    'gk_passes_launched', 'gk_passes_pct_launched', 'gk_passes',
    'gk_passes_throws', 'gk_pct_passes_launched', 'gk_passes_length_avg',
    'gk_goal_kicks', 'gk_pct_goal_kicks_launched',
    'gk_goal_kick_length_avg', 'gk_crosses', 'gk_crosses_stopped',
    'gk_crosses_stopped_pct', 'gk_def_actions_outside_pen_area',
    'gk_def_actions_outside_pen_area_per90', 'gk_avg_distance_def_actions'
]
SHOOTING = [
    'players_used', 'minutes_90s', 'goals', 'shots',
    'shots_on_target', 'shots_on_target_pct', 'shots_per90',
    'shots_on_target_per90', 'goals_per_shot', 'goals_per_shot_on_target',
    'average_shot_distance', 'shots_free_kicks', 'pens_made', 'pens_att',
    'xg', 'npxg', 'npxg_per_shot', 'xg_net', 'npxg_net'
]
PASSING = [
    'players_used', 'minutes_90s', 'passes_completed', 'passes',
    'passes_pct', 'passes_total_distance', 'passes_progressive_distance',
    'passes_completed_short', 'passes_short', 'passes_pct_short',
    'passes_completed_medium', 'passes_medium', 'passes_pct_medium',
    'passes_completed_long', 'passes_long', 'passes_pct_long', 'assists',
    'xg_assist', 'pass_xa', 'xg_assist_net', 'assisted_shots',
    'passes_into_final_third', 'passes_into_penalty_area',
    'crosses_into_penalty_area', 'progressive_passes'
]
PASS_TYPES = [
    'players_used', 'minutes_90s', 'passes', 'passes_live',
    'passes_dead', 'passes_free_kicks', 'through_balls', 'passes_switches',
    'crosses', 'throw_ins', 'corner_kicks', 'corner_kicks_in',
    'corner_kicks_out', 'corner_kicks_straight', 'passes_completed',
    'passes_offsides', 'passes_blocked'
]
# Goal-creating actions
GCA = [
    'players_used', 'minutes_90s', 'sca', 'sca_per90',
    'sca_passes_live', 'sca_passes_dead', 'sca_take_ons', 'sca_shots',
    'sca_fouled', 'sca_defense', 'gca', 'gca_per90', 'gca_passes_live',
    'gca_passes_dead', 'gca_take_ons', 'gca_shots', 'gca_fouled',
    'gca_defense'
]
DEFENCE = [
    'players_used', 'minutes_90s', 'tackles', 'tackles_won',
    'tackles_def_3rd', 'tackles_mid_3rd', 'tackles_att_3rd',
    'challenge_tackles', 'challenges', 'challenge_tackles_pct',
    'challenges_lost', 'blocks', 'blocked_shots', 'blocked_passes',
    'interceptions', 'tackles_interceptions', 'clearances', 'errors'
]
POSSESSION = [
    'players_used', 'possession', 'minutes_90s', 'touches',
    'touches_def_pen_area', 'touches_def_3rd', 'touches_mid_3rd',
    'touches_att_3rd', 'touches_att_pen_area', 'touches_live_ball',
    'take_ons', 'take_ons_won', 'take_ons_won_pct', 'take_ons_tackled',
    'take_ons_tackled_pct', 'carries', 'carries_distance',
    'carries_progressive_distance', 'progressive_carries',
    'carries_into_final_third', 'carries_into_penalty_area', 'miscontrols',
    'dispossessed', 'passes_received', 'progressive_passes_received'
]
MISCELLANEOUS = [
    'players_used', 'minutes_90s', 'cards_yellow', 'cards_red',
    'cards_yellow_red', 'fouls', 'fouled', 'offsides', 'crosses',
    'interceptions', 'tackles_won', 'pens_won', 'pens_conceded',
    'own_goals', 'ball_recoveries', 'aerials_won', 'aerials_lost',
    'aerials_won_pct'
]
CATEGORIES_LIST = [
    STANDARD,
    GOALKEEPING,
    ADVANCED_GOALKEEPING,
    SHOOTING,
    PASSING,
    PASS_TYPES,
    GCA,
    DEFENCE,
    POSSESSION,
    MISCELLANEOUS,
]

# Data Analysis
# Manually remove similar columns
# list(teams_df.columns)
# Data that is already averaged per game
TEAM_COLUMNS_DICT = {
    "squad": {
        "aggregated": [],
        "unaggregated": [
            'players_used',
            'pens_made',
            'pens_att',
            'cards_yellow',
            'cards_red',
            'cards_yellow_red',
            'fouls',
            'fouled',
            'offsides',
            'own_goals',
        ],
    },
    "gk": {
        "aggregated": [
            'gk_goals_against_per90',
            'gk_save_pct',
            'gk_clean_sheets_pct',
            'gk_psxg', # post-shot xG
            'gk_psnpxg_per_shot_on_target_against',
            'gk_psxg_net_per90',
            'gk_passes_pct_launched', # long pass completion
            'gk_pct_passes_launched', # percentage of passes that are long
            'gk_goal_kick_length_avg',
            'gk_crosses_stopped_pct',
            'gk_def_actions_outside_pen_area_per90',
        ],
        "unaggregated": [
            'gk_goals_against',
            'gk_shots_on_target_against',
        #     'gk_saves',
        #     'gk_clean_sheets',
            'gk_pens_saved',
            'gk_pens_missed',
            'gk_free_kick_goals_against',
            'gk_corner_kick_goals_against',
        #     'gk_own_goals_against', # same as own_goals
            'gk_psxg_net', # PSxG - goals allowed
        #     'gk_passes_completed_launched', # passes longer than 40 yards
        #     'gk_passes_launched',
        #     'gk_passes',
        #     'gk_passes_throws',
        #     'gk_goal_kicks',
        #     'gk_pct_goal_kicks_launched',
        #     'gk_crosses',
        #     'gk_crosses_stopped',
        #     'gk_def_actions_outside_pen_area',
        ],
    },
    "attack": {
        "aggregated": [
            'goals_per90',
            'assists_per90',
            'goals_assists_per90',
            'goals_pens_per90',
            'goals_assists_pens_per90',
            'xg_per90',
            'npxg_per90',
            'xg_assist_per90',
            'xg_xg_assist_per90',
            'npxg_xg_assist_per90',
            'shots_on_target_pct',
            'shots_per90',
            'shots_on_target_per90',
            'goals_per_shot',
            'goals_per_shot_on_target',
            'average_shot_distance',
            'npxg_per_shot',
        ],
        "unaggregated": [
        #     'shots',
        #     'shots_on_target',
        #     'shots_free_kicks',
        #     'xg_net',
        #     'npxg_net',
        #     'goals',
        #     'assists',
        #     'goals_assists',
        #     'goals_pens',
        #     'xg',
        #     'npxg',
        #     'xg_assist',
        #     'npxg_xg_assist',
        ],
    },
    "passing": {
        "aggregated": [
            'passes_pct',
            'passes_pct_short',
            'passes_pct_medium',
            'passes_pct_long',
        ],
        "unaggregated": [
            # Passing
        #     'passes_completed',
        #     'passes',
            'passes_total_distance',
            'progressive_passes',
            'passes_progressive_distance',
        #     'passes_completed_short',
        #     'passes_short',
        #     'passes_completed_medium',
        #     'passes_medium',
        #     'passes_completed_long',
        #     'passes_long',
            'pass_xa',
            'xg_assist_net',
            'assisted_shots',
            'passes_into_final_third',
            'passes_into_penalty_area',
            'crosses_into_penalty_area',
            
            # Passing Types
            'passes_live',
            'passes_dead',
            'passes_free_kicks',
            'through_balls',
            'passes_switches',
            'crosses',
            'throw_ins',
            'corner_kicks',
            'corner_kicks_in',
            'corner_kicks_out',
            'corner_kicks_straight',
            # 'passes_offsides',
            # 'passes_blocked',
        ],
    },
    "creation": {
        "aggregated": [
            'sca_per90',
            'gca_per90',
        ],
        "unaggregated": [
            # SCA
            'sca_passes_live',
            'sca_passes_dead',
            'sca_take_ons',
            'sca_shots',
            'sca_fouled',
            'sca_defense',
            # GCA
            'gca_passes_live',
            'gca_passes_dead',
            'gca_take_ons',
            'gca_shots',
            'gca_fouled',
            'gca_defense',
        ],
    },
    "possession": {
        "aggregated": [
            'take_ons_won_pct',
            'take_ons_tackled_pct',
            'possession',
        ],
        "unaggregated": [
            'touches',
            'touches_def_pen_area',
            'touches_def_3rd',
            'touches_mid_3rd',
            'touches_att_3rd',
            'touches_att_pen_area',
            'touches_live_ball',
            'take_ons',
        #     'take_ons_won',
        #     'take_ons_tackled',
            'carries',
            'carries_distance',
            'progressive_carries',
            'carries_progressive_distance',
            'carries_into_final_third',
            'carries_into_penalty_area',
            'miscontrols',
            'dispossessed',
            # 'passes_received',
            # 'progressive_passes_received',
        ],
    },
    "defence": {
        "aggregated": [
            'challenge_tackles_pct', # tackle success rate
            'aerials_won_pct',
        ],
        "unaggregated": [
            'tackles',
            'tackles_won',
            'tackles_def_3rd',
            'tackles_mid_3rd',
            'tackles_att_3rd',
            'challenge_tackles',
            'challenges',
            'challenges_lost',
            'blocks',
            'blocked_shots',
            'blocked_passes',
            'interceptions',
            'tackles_interceptions',
            'clearances',
            'errors',
            'ball_recoveries',
            'aerials_won',
            'aerials_lost',
        ],
    },
}

TEAM_COLUMNS_DICT_COMBINED = dict((category, list(sum(vals.values(), []))) for category, vals in TEAM_COLUMNS_DICT.items())

# Categorical data/data that does not need to be averaged per game
TEAMS_ABSOLUTE_COLUMNS = [
#     Squad stats
    'squad', # team name
    'avg_age',
#     GK stats
    'gk_wins',
    'gk_ties',
    'gk_losses',   
    'season_start_year',
    'season_end_year',
]