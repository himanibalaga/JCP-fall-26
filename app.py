import streamlit as st
import pandas as pd 

st.title("starbucks explorer")
st.header("Calories by category")
st.write("pick a category to filter the menu")

df = pd.DataFrame ({
    "category": ["beverage","food", "beverage", "food"],
    "calories" : [150, 300, 90, 420]
})

st.dataframe(df)

category = st.selectbox("category", df['category'].unique())
filtered = df[df["category"] == category]
st.dataframe(filtered)

col1, col2 = st.coolumns(2)
col1.metric("Items", len(filtered))
col2.metric("Average calories", round(filtered["calories"].mean(),1))

#bar chart 
st.bar_chart(df.groupby("category")["calories"].mean())

#DICTIONARY SYNTAX 
#dict=example = {"key": ['value1', 'value2']}
#cities = {
#    "san jose": ['story road', 'walnut road']
#    "milpitas": ['calaveras', 'anything','values for differnet keys do not need to be same lengths']
#}