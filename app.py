import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit page config
st.set_page_config(page_title="EDA Dashboard", layout="wide")

# Title
st.title("📊 Exploratory Data Analysis App")

# Upload CSV
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Data preview
    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())

    # Data shape
    st.subheader("📐 Data Shape")
    st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

    # Summary statistics
    st.subheader("🧮 Summary Statistics")
    st.write(df.describe())

    # Missing values
    st.subheader("🧼 Missing Values")
    st.write(df.isnull().sum())

    # Correlation heatmap
    st.subheader("📊 Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

    # Box plot
    st.subheader("📦 Box Plot (Detect Outliers)")
    num_col = st.selectbox("Select a numeric column", df.select_dtypes(include='number').columns)
    fig, ax = plt.subplots()
    sns.boxplot(y=df[num_col], ax=ax)
    st.pyplot(fig)

    # Count plot
    st.subheader("📊 Count Plot (Categorical Frequency)")
    cat_col = st.selectbox("Select a categorical column", df.select_dtypes(include='object').columns)
    fig, ax = plt.subplots()
    sns.countplot(x=df[cat_col], order=df[cat_col].value_counts().index, ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

else:
    st.info("Please upload a CSV file to begin your analysis.")
