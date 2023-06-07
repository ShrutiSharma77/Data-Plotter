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
    
    for i in range(0,len(column_values)-1,2):
        avg = (column_values[i]+column_values[i+1])/2
        print(column_values[i+1])
        averages.append(avg)

    avg_dia = np.array(averages)   
    
    averages_flattened = avg_dia.flatten()

    j = 1

    st.write("Averages:")
    for value in averages_flattened:
        st.write(f"{j}.",value)
        j = j + 1

    range = st.number_input("Enter the range", min_value=0, max_value=100, value=0, step=1)

    st.write("Range:", range)