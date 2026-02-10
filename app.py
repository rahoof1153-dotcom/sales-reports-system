import streamlit as st
import pandas as pd

# -----------------------
# PAGE SETTINGS
# -----------------------
st.set_page_config(page_title="Hypermarket Sales Dashboard", layout="wide")

st.title("📊 Hypermarket Sales Report Dashboard")

# -----------------------
# FILE UPLOAD
# -----------------------
uploaded_file = st.file_uploader(
    "Upload Sales Excel File",
    type=["xlsx"]
)

if uploaded_file:

    df = pd.read_excel(uploaded_file)

    # clean column spaces
    df.columns = df.columns.str.strip()

    st.subheader("Raw Data")
    st.dataframe(df, use_container_width=True)

    # -----------------------
    # TOTALS
    # -----------------------
    total_sales = df["Sales"].sum()
    total_qty = df["Qty"].sum()
    total_target = df["Daily Target"].sum()

    achievement = (total_sales / total_target) * 100

    c1, c2, c3 = st.columns(3)

    c1.metric("Total Sales (OMR)", round(total_sales, 2))
    c2.metric("Total Target (OMR)", round(total_target, 2))
    c3.metric("Achievement %", f"{achievement:.1f}%")

    # -----------------------
    # SALES BY CATEGORY
    # -----------------------
    st.subheader("Sales by Category")

    cat_summary = df.groupby("Category")["Sales"].sum()
    st.bar_chart(cat_summary)

    # -----------------------
    # DAILY TREND
    # -----------------------
    st.subheader("Daily Sales Trend")

    daily_summary = df.groupby("Date")["Sales"].sum()
    st.line_chart(daily_summary)

    # -----------------------
    # BRANCH FILTER
    # -----------------------
    st.subheader("Branch Sales")

    branch_summary = df.groupby("Branch")["Sales"].sum()
    st.bar_chart(branch_summary)

    st.success("Report Generated Successfully ✅")
