import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("📊 Exploratory Data Analysis (EDA) App")

# Upload dataset
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # Dataset Shape
    st.subheader("🔹 Dataset Shape")
    st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

    # Dataset Info (without io)
    st.subheader("🔹 Dataset Info")
    info_df = pd.DataFrame({
        "Column": df.columns,
        "Non-Null Count": df.count().values,
        "Dtype": df.dtypes.values
    })
    st.write(info_df)

    # First 5 rows
    st.subheader("🔹 First 5 Rows")
    st.write(df.head())

    # Summary statistics
    st.subheader("🔹 Summary Statistics")
    st.write(df.describe())

    # Missing values
    st.subheader("🔹 Missing Values")
    st.write(df.isnull().sum())

    # Correlation heatmap
    st.subheader("🔹 Correlation Heatmap")
    plt.figure(figsize=(8,5))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
    st.pyplot(plt)
    plt.clf()

    # Histogram
    st.subheader("🔹 Histogram")
    hist_col = st.selectbox("Select column for histogram", df.select_dtypes(include=['float64','int64']).columns)
    plt.figure(figsize=(8,5))
    sns.histplot(df[hist_col], kde=True, bins=30)
    st.pyplot(plt)
    plt.clf()

    # Scatter plot
    st.subheader("🔹 Scatter Plot")
    x_axis = st.selectbox("Select X-axis", df.select_dtypes(include=['float64','int64']).columns)
    y_axis = st.selectbox("Select Y-axis", df.select_dtypes(include=['float64','int64']).columns)
    plt.figure(figsize=(8,5))
    sns.scatterplot(x=df[x_axis], y=df[y_axis])
    st.pyplot(plt)
    plt.clf()

    # Violin plot
    st.subheader("🔹 Violin Plot")
    num_col = st.selectbox("Select numeric column", df.select_dtypes(include=['float64','int64']).columns)
    cat_col = st.selectbox("Select categorical column", df.select_dtypes(include=['object']).columns)
    plt.figure(figsize=(8,5))
    sns.violinplot(x=df[cat_col], y=df[num_col])
    st.pyplot(plt)
    plt.clf()

    # Boxplot
    st.subheader("🔹 Boxplot")
    num_col_box = st.selectbox("Select numeric column for boxplot", df.select_dtypes(include=['float64','int64']).columns)
    plt.figure(figsize=(8,5))
    sns.boxplot(y=df[num_col_box])
    st.pyplot(plt)
    plt.clf()
