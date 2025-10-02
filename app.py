import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Streamlit page configuration
st.set_page_config(page_title="EDA Dashboard", layout="wide")

# Title
st.title("📈 Exploratory Data Analysis App")

# Upload CSV
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Show basic info
    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())

    st.subheader("📐 Data Shape")
    st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

    st.subheader("🧮 Summary Statistics")
    st.write(df.describe())

    st.subheader("🧼 Missing Values")
    st.write(df.isnull().sum())

    # Correlation heatmap
    st.subheader("📊 Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

    # Histogram
    st.subheader("📉 Histogram")
    num_col = st.selectbox("Select a numeric column", df.select_dtypes(include='number').columns)
    fig, ax = plt.subplots()
    sns.histplot(df[num_col], kde=True, ax=ax)
    st.pyplot(fig)

    # Scatter plot
    st.subheader("📌 Scatter Plot")
    col1 = st.selectbox("X-axis", df.select_dtypes(include='number').columns, key="x")
    col2 = st.selectbox("Y-axis", df.select_dtypes(include='number').columns, key="y")
    fig, ax = plt.subplots()
    sns.scatterplot(x=df[col1], y=df[col2], ax=ax)
    st.pyplot(fig)

else:
    st.info("Please upload a CSV file to begin your analysis.")
