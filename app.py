import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📊 Hypermarket Sales Report Dashboard")

uploaded_file = st.file_uploader("Upload Sales Excel File", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    st.subheader("Raw Data")
    st.dataframe(df)

    total_sales = df["Sales"].sum()
    total_qty = df["Qty"].sum()

    col1, col2 = st.columns(2)

    col1.metric("Total Sales (OMR)", round(total_sales, 3))
    col2.metric("Total Quantity", int(total_qty))

    st.subheader("Sales by Category")
    category_summary = df.groupby("Category")["Sales"].sum()
    st.bar_chart(category_summary)

    st.subheader("Daily Sales Trend")
    daily_summary = df.groupby("Date")["Sales"].sum()
    st.line_chart(daily_summary)

    st.success("Report Generated Successfully ✅")
