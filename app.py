import streamlit as st
import pandas as pd
import numpy as np


st.title("Data Plotter")

xlsx_file = st.file_uploader("Upload XLSX file", type=["xlsx"])

if xlsx_file is not None:
    df = pd.read_excel(xlsx_file)
    st.write(df)
    column_values = df.to_numpy()

    averages = []
    
    for i in range(0,len(column_values)-1):
        avg = column_values[i]+column_values[i+1]
        averages.append(avg)
        
        
    st.write("Column Values:", column_values)
    st.write("Averages:",averages)
