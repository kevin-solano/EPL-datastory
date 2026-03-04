import streamlit as st

st.set_page_config(page_title="Methods", layout="wide")

st.title("Methods & Limitations")
st.write("- Data source: `PL-season-2324.csv` and `PL-season-2425.csv` (sample datasets presented for HW3).")
st.write("- Variables used: `FTHG`: `goals_for`, `FTAG`: `goals_against`, `HS`: `shots`, `HST`: `shots_on_target`, `HF`: `fouls`, `HC`: `corners`, `HY`: `yellow`, `HR`: `red`, etc...")
st.subheader("Limitations")
st.write("- Two seasons; patterns might change, shift or disappear in a larger dataset (not representative of prior team history).")
st.write("- Some teams like Everton only have data present for one year, and might have more patterns to demonstrate, which are not illustrated here.")
st.write("- Variables like 'Referee' were not analyzed and might be highly correlated to others that were used, ie `goals_for` ")
