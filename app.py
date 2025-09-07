import streamlit as st
import pandas as pd

# Load dataset
plants = pd.read_csv("plants.csv")

st.title("🌱 Vibe Plant Selector")

# User filter options
sun = st.selectbox("☀️ Sun Requirement", plants["Sun"].unique())
soil = st.selectbox("🌍 Soil Type", plants["Soil Type"].unique())

# Filter plants
filtered = plants[(plants["Sun"] == sun) & (plants["Soil Type"] == soil)]

st.write("✅ Suggested Plants:")
st.dataframe(filtered)
