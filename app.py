import streamlit as st
import pandas as pd

st.set_page_config(page_title="Hypermarket Sales Dashboard", layout="wide")

st.title("📊 Hypermarket Sales Report Dashboard")

uploaded_file = st.file_uploader("Upload Sales Excel File", type=["xlsx"])

if uploaded_file:

    df = pd.read_excel(uploaded_file)
    df.columns = df.columns.str.strip()

    st.subheader("Raw Data")
    st.dataframe(df, use_container_width=True)

    # totals
    total_sales = df["Sales"].sum()
    total_qty = df["Qty"].sum()
    total_target = df["Daily Target"].sum()

    c1, c2, c3 = st.columns(3)
    c1.metric("Total Sales (OMR)", round(total_sales, 2))
    c2.metric("Total Qty", int(total_qty))
    c3.metric("Target (OMR)", round(total_target, 2))

    # charts
    st.subheader("Sales by Category")
    st.bar_chart(df.groupby("Category")["Sales"].sum())

    st.subheader("Daily Sales Trend")
    st.line_chart(df.groupby("Date")["Sales"].sum())

    st.success("Report Generated Successfully ✅")
