import streamlit as st
import pandas as pd

st.title("starbucks explorer")
st.header("Calories by category")
st.write("pick a category to filter the menu")

df = pd.DataFrame({
    "category" : ["bev", "food", "bev", "food"],
    "cals" : [150, 300, 90, 420]
})

st.dataframe(df)

category = st.selectbox("category", df["category"].unique())
filtered = df[df["category"] == category]
st.dataframe(filtered)
