import streamlit as st
from utils.io import load_homeaway, load_longdf
from charts.charts import chart_home_adv, chart_attack, bar_chart

st.set_page_config(page_title="More Explorations", layout="wide")

long_match = load_longdf()
home, away = load_homeaway()

st.title("A Greater Exploratory View")
st.write("Use the interactive aspects of these two charts to explore team attack.")

st.altair_chart(chart_attack(home, away), use_container_width=True)

st.markdown("**Guided prompts:**")
st.write("- Filter to one team  (e.g., `Arsenal`) — does the pattern displayed here show across other teams, or other years?")
st.write("- Switch attack metrics -  how do the metric values shift for each team?")

st.title("Now")
st.write("Explore home advantage.")

st.altair_chart(chart_home_adv(long_match), use_container_width=True)
st.altair_chart(bar_chart(long_match), use_container_width=True)

st.markdown("**Guided prompts:**")
st.write("- Compare the linked overall points bar chart - is there home (green) advantage?")
st.write("- Brush a group of teams - is there still clear home advantage one way or another, or are certain sections prone to showing the reverse?")
