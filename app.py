import streamlit as st
from PIL import Image

st.set_page_config(page_title="English Premier League (football)", layout="wide")

st.title("English Premier League (football) 2023 - 2025")
st.write(Image.open('images/EnglandPl202021.png'))
st.write("This project is meant to serve as a demonstration of the visualizations of the English Premier League\
         where charts are designed using Altair. This project is deployed using Streamlit.\n")
st.write(
    "To explore this visual data story, please navigate it through the pages in the sidebar:\n"
    "- **Central Narrative**: We begin by observing some of the statistics for teams over the two seasons.\n"
    "- **Exploration**: For a closer reader-driven exploration of the data, we provide a few interactive designs.\n"
    "- **Methodology**: We lay down some key details about our data and limitations to our analysis.\n"
)
st.info("Datasets: `PL-season-2324.csv` , `PL-season-2425.csv`")

