
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📊 Sales Data Dashboard")
st.write("Upload a CSV file to visualize and analyze your data.")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.write("### Preview of Uploaded Data", df.head())

        col_options = df.select_dtypes(include='object').columns.tolist()
        num_options = df.select_dtypes(include='number').columns.tolist()

        if col_options and num_options:
            x_col = st.selectbox("Select X-axis (categorical)", col_options)
            y_col = st.selectbox("Select Y-axis (numerical)", num_options)

            fig = px.bar(df, x=x_col, y=y_col, title=f"{y_col} by {x_col}")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Your file must contain at least one text and one numeric column.")
    except Exception as e:
        st.error(f"Error loading file: {e}")
else:
    st.info("Awaiting file upload...")
