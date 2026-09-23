import streamlit as st
import pandas as pd

st.title("Starbucks explorer")
st.header("Calories by Category")
st.write("Choose a category to filter the menu:")

df = pd.DataFrame({
    "category": ["beverage", "food", "beverage", "food"],
    "calories": [150, 300, 90, 420]
})

st.dataframe(df)

#create sleectbox to filter by category
category = st.selectbox("Select a category:", df["category"].unique())
filtered_df = df[df["category"] == category]
st.dataframe(filtered_df)

col1, col2 = st.columns(2)
col1.metric("Items", len(filtered_df))
col2.metric("Average Calories", round(filtered_df["calories"].mean(), 1))

#bar chart
st.bar_chart(df.groupby("category")["calories"].mean())

#DICTIONARY SYNTAX
dict_example = {"key": ['value1', 'value2']}
cities = {
    "san jose": ['story road', 'san jose state university'],
    'san francisco': ['golden gate bridge', 'fisherman wharf'],
}

st.header(cities["san jose"][0])