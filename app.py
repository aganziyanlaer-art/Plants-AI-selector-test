import streamlit as st
import pandas as pd

# Load dataset
url = "https://raw.githubusercontent.com/aganziyanlaer-art/Plants-AI-selector-test/main/plants.csv"
plants = pd.read_csv(url)

st.title("🌱 Vibe Plant Selector")

# User filter options
sun = st.selectbox("☀️ Sun Requirement", plants["Sun"].unique())
soil = st.selectbox("🌍 Soil Type", plants["Soil Type"].unique())
drought = st.selectbox("💧 Drought Tolerance", plants["Drought Tolerant"].unique())
size = st.slider("🌳 Mature Size (m)", 0, 50, 10)
flower_color = st.selectbox("🌸 Flower Color", plants["Flower Color"].unique())
bloom_season = st.selectbox("🌼 Blooming Season", plants["Blooming Season"].unique())

# Filter plants
filtered = plants[
    (plants["Sun"] == sun) &
    (plants["Soil Type"] == soil) &
    (plants["Drought Tolerant"] == drought) &
    (plants["Mature Size (m)"] <= size) &
    (plants["Flower Color"] == flower_color) &
    (plants["Blooming Season"] == bloom_season)
]

st.write("✅ Suggested Plants:")
st.dataframe(filtered)
