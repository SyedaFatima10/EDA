import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ✅ Streamlit page configuration
st.set_page_config(page_title="EDA Dashboard", layout="wide")

# ✅ App title
st.title("📊 Exploratory Data Analysis App")

# ✅ File upload section (now allows both CSV and Excel)
uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx", "xls"])

if uploaded_file is not None:
    # ✅ Detect file type automatically
    file_name = uploaded_file.name.lower()

    if file_name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    elif file_name.endswith((".xlsx", ".xls")):
        # Use openpyxl engine for Excel files
        df = pd.read_excel(uploaded_file, engine="openpyxl")
    else:
        st.error("❌ Please upload a valid CSV or Excel file.")
        st.stop()

    # ✅ Data preview
    st.subheader("🔍 Data Preview (head)")
    st.dataframe(df.head())

    # ✅ Data shape
    st.subheader("📐 Data Shape")
    st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

    # ✅ Column names
    st.subheader("🧾 Column Names")
    st.write(df.columns.tolist())

    # ✅ Summary statistics
    st.subheader("📊 Summary Statistics")
    st.write(df.describe())

    # ✅ Missing values
    st.subheader("🧼 Missing Values")
    st.write(df.isnull().sum())

    # ✅ Correlation heatmap
    st.subheader("📈 Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

    # ✅ Box plot
    st.subheader("📦 Box Plot")
    num_cols = df.select_dtypes(include='number').columns
    if len(num_cols) > 0:
        num_col = st.selectbox("Select a numeric column", num_cols)
        fig, ax = plt.subplots()
        sns.boxplot(y=df[num_col], ax=ax)
        st.pyplot(fig)
    else:
        st.warning("No numeric columns found for box plot.")

    # ✅ Count plot
    st.subheader("📊 Count Plot")
    cat_cols = df.select_dtypes(include='object').columns
    if len(cat_cols) > 0:
        cat_col = st.selectbox("Select a categorical column", cat_cols)
        fig, ax = plt.subplots()
        sns.countplot(x=df[cat_col], order=df[cat_col].value_counts().index, ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)
    else:
        st.warning("No categorical columns found for count plot.")

else:
    st.info("📤 Please upload a CSV or Excel file to begin your analysis.")
