import streamlit as st
import pandas as pd


st.title("Data Plotter")

# Display a file uploader widget
xlsx_file = st.file_uploader("Upload XLSX file", type=["xlsx"])

if xlsx_file is not None:
    # Read the XLSX file into a DataFrame
    df = pd.read_excel(xlsx_file)

    # Display the DataFrame in Streamlit
    st.write(df)

