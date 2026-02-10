import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📊 Hypermarket Sales Report Dashboard")

uploaded_file = st.file_uploader("Upload Sales Excel File", type=["xlsx"])

if uploaded_file:

    df = pd.read_excel(uploaded_file)
    df.columns = df.columns.str.strip()

    st.subheader("Raw Data")
    st.dataframe(df)

    # auto detect sales column
    sales_col = None
    for col in df.columns:
        if "sale" in col.lower():
            sales_col = col
            break

    if not sales_col:
        st.error("Sales column not found in Excel")
        st.stop()

    total_sales = df[sales_col].sum()

    st.metric("Total Sales (OMR)", f"{total_sales:,.2f}")

    st.subheader("Branch Wise Sales")
    st.bar_chart(df.groupby("Branch")[sales_col].sum())

    st.subheader("Category Wise Sales")
    st.bar_chart(df.groupby("Category")[sales_col].sum())

    if "Date" in df.columns:
        st.subheader("Daily Trend")
        st.line_chart(df.groupby("Date")[sales_col].sum())

    st.success("Report Generated Successfully ✅")
