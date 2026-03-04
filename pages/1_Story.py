import streamlit as st
import altair as alt
from utils.io import load_epl
from charts.charts import base_theme, chart_season_comp

st.set_page_config(page_title="A Sports Story", layout="wide")

alt.themes.register("project", base_theme)
alt.themes.enable("project")

team_season = load_epl()


st.title("A Data Story: English Premier League")
st.write("We start with a simple chart with a dropdown menu to build a view of team performance across two seasons and different metrics.")

st.header("1) EPL Team Season Comparison")
st.markdown("**Central question:**")
st.markdown("*How does team performance differ between the two seasons?*")

st.altair_chart(chart_season_comp(team_season), use_container_width=True)
st.caption("Takeaway: ..")