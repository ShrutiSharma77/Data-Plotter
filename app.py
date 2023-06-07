import streamlit as st
import pandas as pd
import numpy as np


st.title("Data Plotter")

xlsx_file = st.file_uploader("Upload XLSX file", type=["xlsx"])

if xlsx_file is not None:
    df = pd.read_excel(xlsx_file)
    st.write(df)
    column_values = df.to_numpy()

    i = 0

    for i in column_values:
        sum = column_values[i]+column_values[i+1]
        st.write(sum)
        sum = 0
        i = i + 2
    
    st.write("Column Values:", column_values)
