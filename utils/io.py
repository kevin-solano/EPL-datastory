import streamlit as st
import pandas as pd

@st.cache_data
def load_epl() -> pd.DataFrame:
    # load csv
    epl_2324 = pd.read_csv("PL-season-2324.csv")
    epl_2425 = pd.read_csv("PL-season-2425.csv")
    # season labels
    epl_2324["season"] = "2023-2024"
    epl_2425["season"] = "2024-2025"
    # combining initial dataset
    df = pd.concat([epl_2324, epl_2425], ignore_index=True)
    # for home
    df_1 = df.copy()
    df_1 = df_1.rename(columns={'HomeTeam': 'team',
                            'FTHG': 'goals_for',
                            'FTAG': 'goals_against',
                            'HS': 'shots',
                            'HST': 'shots_on_target',
                            'HF': 'fouls',
                            'HC': 'corners',
                            'HY': 'yellow',
                            'HR': 'red'
                            })
    
    df_1['home_away'] = 'home'
    df_1['result'] = df_1['FTR']
    df_1['points'] = df_1['result'].map({'H': 3,
                                     'D': 1,
                                     'A': 0
                                     })
    # for away
    df_2 = df.copy()
    df_2 = df_2.rename(columns={'AwayTeam': 'team',
                            'FTHG': 'goals_against',
                            'FTAG': 'goals_for',
                            'AS': 'shots',
                            'AST': 'shots_on_target',
                            'AF': 'fouls',
                            'AC': 'corners',
                            'AY': 'yellow',
                            'AR': 'red'
                            })
    df_2['home_away'] = 'away'
    df_2['result'] = df_2['FTR']
    df_2['points'] = df_2['result'].map({'H': 0,
                                     'D': 1,
                                     'A': 3
                                     })
    # long format
    df_3 = pd.concat([df_1, df_2], ignore_index=True)
    # combining into team season
    team_season = (df_3.groupby(['season', 'team'])
                   .agg(
        matches=('team', 'count'),
        wins=('points', lambda x: (x == 3).sum()),
        draws=('points', lambda x: (x == 1).sum()),
        losses=('points', lambda x: (x == 0).sum()),
        points=('points', 'sum'),
        goals_for=('goals_for', 'sum'),
        goals_against=('goals_against', 'sum'),
        goal_diff=('goals_for', lambda x: x.sum())
    ).reset_index()
    )
    team_season['goal_diff'] = (team_season['goals_for'] - team_season['goals_against'])
    
    return team_season


@st.cache_data
def load_homeaway() -> pd.DataFrame:
    # load csv
    epl_2324 = pd.read_csv("Pl-season-2324.csv")
    epl_2425 = pd.read_csv("Pl-season-2425.csv")
    # season labels
    epl_2324["season"] = "2023-2024"
    epl_2425["season"] = "2024-2025"
    # combining initial dataset
    df = pd.concat([epl_2324, epl_2425], ignore_index=True)
    # for home
    df_1 = df.copy()
    df_1 = df_1.rename(columns={'HomeTeam': 'team',
                            'FTHG': 'goals_for',
                            'FTAG': 'goals_against',
                            'HS': 'shots',
                            'HST': 'shots_on_target',
                            'HF': 'fouls',
                            'HC': 'corners',
                            'HY': 'yellow',
                            'HR': 'red'
                            })
    
    df_1['home_away'] = 'home'
    df_1['result'] = df_1['FTR']
    df_1['points'] = df_1['result'].map({'H': 3,
                                     'D': 1,
                                     'A': 0
                                     })
    # for away
    df_2 = df.copy()
    df_2 = df_2.rename(columns={'AwayTeam': 'team',
                            'FTHG': 'goals_against',
                            'FTAG': 'goals_for',
                            'AS': 'shots',
                            'AST': 'shots_on_target',
                            'AF': 'fouls',
                            'AC': 'corners',
                            'AY': 'yellow',
                            'AR': 'red'
                            })
    df_2['home_away'] = 'away'
    df_2['result'] = df_2['FTR']
    df_2['points'] = df_2['result'].map({'H': 0,
                                     'D': 1,
                                     'A': 3
                                     })
    return df_1, df_2

@st.cache_data
def load_longdf() -> pd.DataFrame:
    # load csv
    epl_2324 = pd.read_csv("Pl-season-2324.csv")
    epl_2425 = pd.read_csv("Pl-season-2425.csv")
    # season labels
    epl_2324["season"] = "2023-2024"
    epl_2425["season"] = "2024-2025"
    # combining initial dataset
    df = pd.concat([epl_2324, epl_2425], ignore_index=True)
    # for home
    df_1 = df.copy()
    df_1 = df_1.rename(columns={'HomeTeam': 'team',
                            'FTHG': 'goals_for',
                            'FTAG': 'goals_against',
                            'HS': 'shots',
                            'HST': 'shots_on_target',
                            'HF': 'fouls',
                            'HC': 'corners',
                            'HY': 'yellow',
                            'HR': 'red'
                            })
    
    df_1['home_away'] = 'home'
    df_1['result'] = df_1['FTR']
    df_1['points'] = df_1['result'].map({'H': 3,
                                     'D': 1,
                                     'A': 0
                                     })
    # for away
    df_2 = df.copy()
    df_2 = df_2.rename(columns={'AwayTeam': 'team',
                            'FTHG': 'goals_against',
                            'FTAG': 'goals_for',
                            'AS': 'shots',
                            'AST': 'shots_on_target',
                            'AF': 'fouls',
                            'AC': 'corners',
                            'AY': 'yellow',
                            'AR': 'red'
                            })
    df_2['home_away'] = 'away'
    df_2['result'] = df_2['FTR']
    df_2['points'] = df_2['result'].map({'H': 0,
                                     'D': 1,
                                     'A': 3
                                     })
    # long format
    df_3 = pd.concat([df_1, df_2], ignore_index=True)

    return df_3
