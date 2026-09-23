import streamlit as st
import pandas as pd

# Header information
st.title("Starbucks Explorer")
st.header("Calories by Category")
st.write("Pick a category to filter the menu")

# Manually create dataframe of category and calories
df = pd.DataFrame({
    "category": ["beverage", "food", "beverage", "food"],
    "calories": [150, 300, 90, 420]
})

# Show the dataframe in Streamlit
st.dataframe(df)

# Show a filtered dataframe
category = st.selectbox("category", df["category"].unique())
filtered = df[df["category"] == category]

st.dataframe(filtered)


