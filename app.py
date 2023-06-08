import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

st.title("Data Plotter")

xlsx_file = st.file_uploader("Upload XLSX file", type=["xlsx"])

if xlsx_file is not None:
    df = pd.read_excel(xlsx_file)
    st.write(df)
    column_values = df.to_numpy()

    averages = []

    for i in range(0, len(column_values) - 1, 2):
        avg = (column_values[i] + column_values[i + 1]) / 2
        averages.append(avg)

    avg_dia = np.array(averages)

    averages_flattened = avg_dia.flatten()

    j = 1

    st.write("Averages:")
    for value in averages_flattened:
        st.write(f"{j}.", value)
        j = j + 1

    range_value = st.number_input("Enter the range", min_value=0, max_value=100, value=0, step=1)

    st.write("Range:", range_value)

    max_value = np.max(avg_dia)

    st.write("The maximum value in the array is:", max_value)

    rounded_value = math.ceil(max_value / 10) * 10

    st.write("Rounded value:", rounded_value)

    lower_bound = 0
    upper_bound = rounded_value

    x = []

    while lower_bound < upper_bound:
        range_label = f"{lower_bound}-{lower_bound+range_value}"
        x.append(range_label)
        lower_bound += range_value

    x_new = np.array(x)

    st.write("X-axis:", x_new)

    num_ranges = upper_bound // range_value

    count_array = [0] * num_ranges

    for value in avg_dia:
        lower_bound = int(value) // range_value * range_value
        upper_bound_range = min(lower_bound + range_value, upper_bound)

        range_index = lower_bound // range_value
        count_array[range_index] += 1


    y_new = np.array(count_array)

    st.write("Number of grains:",y_new)


    y = y_new/len(avg_dia)

    st.write("Y-axis:",y)


    