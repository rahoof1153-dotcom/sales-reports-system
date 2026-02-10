import streamlit as st
import pandas as pd

# ------------------------------------------------
# PAGE SETTINGS
# ------------------------------------------------
st.set_page_config(page_title="Hypermarket Sales Dashboard", layout="wide")

st.title("📊 Hypermarket Sales Report Dashboard")

# ------------------------------------------------
# FILE UPLOAD
# ------------------------------------------------
uploaded_file = st.file_uploader(
    "Upload Sales Excel File",
    type=["xlsx"]
)

if uploaded_file:

    df = pd.read_excel(uploaded_file)

    st.subheader("Raw Data")
    st.dataframe(df, use_container_width=True)

    # ------------------------------------------------
    # COLUMN NAMES (MUST MATCH YOUR EXCEL)
    # ------------------------------------------------
    SALES_COL = "Sales Amount (OMR)"
    TARGET_COL = "Target Amount (OMR)"

    # ------------------------------------------------
    # SIDEBAR FILTERS
    # ------------------------------------------------
    st.sidebar.header("Filters")

    branch = st.sidebar.multiselect(
        "Select Branch",
        df["Branch"].unique(),
        default=df["Branch"].unique()
    )

    category = st.sidebar.multiselect(
        "Select Category",
        df["Category"].unique(),
        default=df["Category"].unique()
    )

    df = df[
        (df["Branch"].isin(branch)) &
        (df["Category"].isin(category))
    ]

    # ------------------------------------------------
    # KPI CALCULATIONS
    # ------------------------------------------------
    total_sales = df[SALES_COL].sum()
    total_target = df[TARGET_COL].sum()

    achievement = 0
    if total_target > 0:
        achievement = (total_sales / total_target) * 100

    # ------------------------------------------------
    # KPI CARDS
    # ------------------------------------------------
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Sales (OMR)", f"{total_sales:,.2f}")
    col2.metric("Target (OMR)", f"{total_target:,.2f}")
    col3.metric("Achievement %", f"{achievement:.1f}%")

    # ------------------------------------------------
    # SALES BY CATEGORY
    # ------------------------------------------------
    st.subheader("Sales by Category")

    cat_summary = (
        df.groupby("Category")[SALES_COL]
        .sum()
        .sort_values(ascending=False)
    )

    st.bar_chart(cat_summary)

    # ------------------------------------------------
    # SALES BY BRANCH
    # ------------------------------------------------
    st.subheader("Sales by Branch")

    branch_summary = df.groupby("Branch")[SALES_COL].sum()
    st.bar_chart(branch_summary)

    # ------------------------------------------------
    # DAILY TREND
    # ------------------------------------------------
    st.subheader("Daily Sales Trend")

    daily = df.groupby("Date")[SALES_COL].sum()
    st.line_chart(daily)

    # ------------------------------------------------
    # MONTHLY SUMMARY
    # ------------------------------------------------
    st.subheader("Monthly Summary")

    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.to_period("M").astype(str)

    monthly = df.groupby("Month")[SALES_COL].sum()

    st.bar_chart(monthly)

    # ------------------------------------------------
    # DOWNLOAD SUMMARY
    # ------------------------------------------------
    st.subheader("Download Summary")

    summary_df = pd.DataFrame({
        "Total Sales": [total_sales],
        "Target": [total_target],
        "Achievement %": [round(achievement, 2)]
    })

    st.download_button(
        "Download Report CSV",
        summary_df.to_csv(index=False),
        file_name="sales_summary.csv",
        mime="text/csv"
    )

    st.success("✅ Report Generated Successfully!")