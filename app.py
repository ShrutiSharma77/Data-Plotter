import streamlit as st
import pandas as pd
import numpy as np


st.title("Data Plotter")

xlsx_file = st.file_uploader("Upload XLSX file", type=["xlsx"])

if xlsx_file is not None:
    df = pd.read_excel(xlsx_file)
    st.write(df)
    row_index = 0
    row_values = df.iloc[row_index].to_numpy()
    
    st.write("Row Values:", row_values)

