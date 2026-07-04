import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📊 EDA Automation App")

file = st.file_uploader("Upload CSV", type=["csv"])

if file:
    df = pd.read_csv(file)

    st.subheader("Dataset Shape")
    st.write(df.shape)

    st.subheader("Columns")
    st.write(df.columns.tolist())

    st.subheader("Missing Values")
    st.write(df.isnull().sum())

    st.subheader("Data Types")
    st.write(df.dtypes)

    st.subheader("Summary")
    st.write(df.describe())

    numeric_cols = df.select_dtypes(include=['number']).columns

    if len(numeric_cols) > 0:
        st.subheader("Histogram")
        fig, ax = plt.subplots()
        ax.hist(df[numeric_cols[0]])
        st.pyplot(fig)

        st.subheader("Boxplot")
        fig, ax = plt.subplots()
        sns.boxplot(y=df[numeric_cols[0]], ax=ax)
        st.pyplot(fig)

        st.subheader("Heatmap")
        fig, ax = plt.subplots()
        sns.heatmap(df[numeric_cols].corr(), annot=True)
        st.pyplot(fig)