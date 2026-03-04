import altair as alt
import pandas as pd

def base_theme():
    return {
        "config": {
            "view": {"stroke": None},
            "axis": {"labelFontSize": 12, "titleFontSize": 14},
            "legend": {"labelFontSize": 12, "titleFontSize": 14},
        }
    }


def chart_season_comp(df: pd.DataFrame) -> alt.Chart:
    # metrics selector
    metric_selector = alt.param(bind=alt.binding_select(options=['points', 'wins', 'goal_diff'],name='Metric: '),
                            value = 'points',
                            name= 'selected_metric'
                            ) # team selector
    team_list = sorted(df['team'].unique().tolist())
    team_dropdown = alt.selection_point(fields=['team'],
                                    bind=alt.binding_select(options=team_list + [None],
                                                            labels=team_list + ['All'],
                                                            name='Highlight Team: '),
                                    name='highlight_team')
    # base chart
    base = (alt.Chart(df,
    title= 'EPL Team Season Comparison')
    .mark_line(point=True)
    .transform_calculate(
    target_val= 'datum[selected_metric]')
    .encode(
    y= alt.Y('team:N', title='Team', sort='-x'),
    x= alt.X('target_val:Q', title='Metric Value'),
    color = alt.Color('season:O').scale(domain=['2023-2024', '2024-2025'],
                                       range=["#71A9D7", "#0B1DE7"]),
    detail='team:N',
    opacity=alt.when(team_dropdown).then(alt.value(1)).otherwise(alt.value(0.2)),
    tooltip = ['target_val:Q'],
    )
    .add_params(metric_selector, team_dropdown)
    .properties(
    width= 500,
    height= 500)
    )
    
    return base



def chart_attack(df_1: pd.DataFrame, df_2: pd.DataFrame) -> alt.Chart:
    # loading formatted df
    cols = [
        'Date', 'season', 'team',
        'home_away','goals_for',
        'goals_against','shots',
        'shots_on_target', 'corners', 'fouls']
    home = df_1[cols]
    away = df_2[cols]
    attack_df = pd.concat([home, away])
    # cleaning last step: x-axis
    attack_df = (attack_df.sort_values(['season', 'team', 'Date']).reset_index(drop=True))
    attack_df['matchweek'] = (attack_df.groupby(['season', 'team']).cumcount() + 1)
    # rolling avg metrics
    attack_df = (attack_df.assign(
        rolling_goals=lambda x:
            x.groupby(['season', 'team'])['goals_for']
             .transform(lambda s: s.rolling(5, min_periods=1).mean()),

        rolling_corners=lambda x:
            x.groupby(['season', 'team'])['corners']
             .transform(lambda s: s.rolling(5, min_periods=1).mean()),

        rolling_shots=lambda x:
            x.groupby(['season', 'team'])['shots']
             .transform(lambda s: s.rolling(5, min_periods=1).mean()),
        
        rolling_shots_ot=lambda x:
            x.groupby(['season', 'team'])['shots_on_target']
             .transform(lambda s: s.rolling(5, min_periods=1).mean())
             )
        )
    
    # attacking metric
    attacking_metric_selector = alt.param(
    bind=alt.binding_select(options=['goals_for', 'corners', 'shots', 'shots_on_target'], 
                           name='Select Attacking Metric: '),
    value='goals_for',
    name='selected_attack_metric')
    #season dropdown
    selectSeason = alt.param(
    name= 'Select_Season',
    bind=alt.binding_radio(options=['2023-2024', '2024-2025'],
                           name='Season: '),
    value = '2023-2024')
    
    # team selector
    team_list = sorted(attack_df['team'].unique().tolist())
    team_dropdown = alt.selection_point(fields=['team'],
                                    bind=alt.binding_select(options=team_list + [None],
                                                            labels=team_list + ['All'],
                                                            name='Highlight Team: '),
                                    name='highlight_team'
    )
    
    attacks = alt.Chart(
    attack_df,
    title="Attack Performance by Team"
    ).mark_line().transform_calculate(
    target_val= 'datum[selected_attack_metric]'
    ).transform_filter(
    "datum.season == Select_Season"
    ).encode(
    x=alt.X('matchweek:Q',title= "Match Week"),
    y=alt.Y('target_val:Q', title = 'Attack Metric'),
    color=alt.Color('team:N', title= 'Teams'),
    opacity=alt.when(team_dropdown).then(alt.value(1)).otherwise(alt.value(0))
    ).add_params(
    attacking_metric_selector, selectSeason, team_dropdown
    ).properties(
    width=700,
    height=500,
    )
    return attacks

def chart_home_adv(df: pd.DataFrame) -> alt.Chart:
    
    home_away_df = (df.groupby(['season', 'team', 'home_away'])['points'].sum().reset_index())
    home_away = (home_away_df.pivot(index=['season', 'team'],
                                columns='home_away',
                                values='points').reset_index())
    
    brush = alt.selection_interval(empty='all')
    
    scatter = alt.Chart(
    home_away).mark_circle(size=100).encode(
    x=alt.X('home:Q', title='Home Points'),
    y=alt.Y('away:Q', title='Away Points'),
    color=alt.condition(brush, 'team:N', alt.value('lightgray'), title = 'Team'),
    tooltip=['team', 'season', 'home', 'away']).add_params(
    brush).properties(
    width=400,
    height=600,
    title="Team's Home Advantage"
    )
    return scatter


def bar_chart(df: pd.DataFrame) -> alt.Chart:
    
    home_away_df = (df.groupby(['season', 'team', 'home_away'])['points'].sum().reset_index())
    home_away = (home_away_df.pivot(index=['season', 'team'],
                                columns='home_away',
                                values='points').reset_index())
    
    brush = alt.selection_interval(empty='all')
    
    scatter = alt.Chart(
    home_away).mark_circle(size=100).encode(
    x=alt.X('home:Q', title='Home Points'),
    y=alt.Y('away:Q', title='Away Points'),
    color=alt.condition(brush, 'team:N', alt.value('lightgray'), title = 'Team'),
    tooltip=['team', 'season', 'home', 'away']).add_params(
    brush).properties(
    width=400,
    height=400,
    title="Team's Home Advantage"
    )
    
    bar = alt.Chart(
    home_away).transform_filter(
    brush).transform_fold(
    ['home', 'away'],
    as_=['location', 'points']).mark_bar().encode(
    x=alt.X('team:N', title='Team'),
    y=alt.Y('points:Q', title='Points'),
    color=alt.Color('location:N', title='Team'),
    xOffset='location:N',
    tooltip=['team:N','season:N','location:N','points:Q']).properties(
    width=600,
    height=400,
    title="Home vs Away Points by Team"
    )
    
    return scatter | bar
