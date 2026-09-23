import streamlit as st
import pandas as pd

st.title("hello")
st.header("Calories by Category")

manual_data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [70000, 85000, 95000, 60000]
}
df = pd.DataFrame(manual_data)

st.dataframe(df)

category = st.selectbox("Name", df['Name'].unique())
filtered = df[df['Name'] == category]
st.dataframe(filtered)

col1, col2 = st.columns(2)
col1.metric("Items", len(filtered))

st.bar_chart(df.groupby("Name")['Salary'].mean())