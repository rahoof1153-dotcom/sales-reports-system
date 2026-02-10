import streamlit as st
import pandas as pd

# ---------------------------
# PAGE SETTINGS
# ---------------------------
st.set_page_config(page_title="Hypermarket Sales Dashboard", layout="wide")

st.title("📊 Hypermarket Sales Report Dashboard")

# ---------------------------
# FILE UPLOAD
# ---------------------------
uploaded_file = st.file_uploader("Upload Sales Excel File", type=["xlsx"])

if uploaded_file:

    df = pd.read_excel(uploaded_file)

    # clean column spaces
    df.columns = df.columns.str.strip()

    st.subheader("Raw Data")
    st.dataframe(df, use_container_width=True)

    # ---------------------------
    # COLUMN NAMES (MATCH YOUR EXCEL)
    # ---------------------------
    SALES_COL = "Sales"
    QTY_COL = "Qty"
    TARGET_COL = "Daily Target"
    DATE_COL = "Date"
    CATEGORY_COL = "Category"
    BRANCH_COL = "Branch"

    # ---------------------------
    # SIDEBAR FILTERS
    # ---------------------------
    st.sidebar.header("Filters")

    branch_filter = st.sidebar.multiselect(
        "Select Branch",
        options=df[BRANCH_COL].unique(),
        default=df[BRANCH_COL].unique()
    )

    category_filter = st.sidebar.multiselect(
        "Select Category",
        options=df[CATEGORY_COL].unique(),
        default=df[CATEGORY_COL].unique()
    )

    df = df[
        (df[BRANCH_COL].isin(branch_filter)) &
        (df[CATEGORY_COL].isin(category_filter))
    ]

    # ---------------------------
    # EQUATIONS (FORMULAS)
    # ---------------------------

    total_sales = df[SALES_COL].sum()
    total_qty = df[QTY_COL].sum()
    total_target = df[TARGET_COL].sum()

    if total_target > 0:
        achievement = (total_sales / total_target) * 100
    else:
        achievement = 0

    # ---------------------------
    # KPI CARDS
    # ---------------------------
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Sales (OMR)", round(total_sales, 2))
    col2.metric("Total Qty", int(total_qty))
    col3.metric("Target (OMR)", round(total_target, 2))
    col4.metric("Achievement %", f"{achievement:.1f}%")

    # ---------------------------
    # SALES BY CATEGORY
    # ---------------------------
    st.subheader("Sales by Category")

    cat_summary = df.groupby(CATEGORY_COL)[SALES_COL].sum()
    st.bar_chart(cat_summary)

    # ---------------------------
    # SALES BY BRANCH
    # ---------------------------
    st.subheader("Sales by Branch")

    branch_summary = df.groupby(BRANCH_COL)[SALES_COL].sum()
    st.bar_chart(branch_summary)

    # ---------------------------
    # DAILY TREND
    # ---------------------------
    st.subheader("Daily Sales Trend")

    df[DATE_COL] = pd.to_datetime(df[DATE_COL])
    daily = df.groupby(DATE_COL)[SALES_COL].sum()
    st.line_chart(daily)

    # ---------------------------
    # MONTHLY TREND
    # ---------------------------
    st.subheader("Monthly Sales")

    df["Month"] = df[DATE_COL].dt.to_period("M").astype(str)
    monthly = df.groupby("Month")[SALES_COL].sum()
    st.bar_chart(monthly)

    # ---------------------------
    # DOWNLOAD REPORT
    # ---------------------------
    summary_df = pd.DataFrame({
        "Total Sales": [total_sales],
        "Total Qty": [total_qty],
        "Target": [total_target],
        "Achievement %": [round(achievement, 2)]
    })

    st.download_button(
        "Download Summary CSV",
        summary_df.to_csv(index=False),
        file_name="sales_summary.csv",
        mime="text/csv"
    )

    st.success("Report Generated Successfully ✅")