import streamlit as st
import pandas as pd
from bokeh.plotting import figure
import os

file_name_list = []
for i in os.listdir():
  if i.endswith('csv'):
    file_name_list.append(i)
  
st.write('Hello World')

df = pd.read_csv('Bastar Craton.csv')
st.dataframe(df)

el_list = df.columns.tolist()[27:80]
x_axis = st.selectbox('select element', el_list)

st.multiselect('select location', file_name_list, file_name_list [0])

x = df['el_list']/10000
y = df['el_list']/10000

p = figure(
    title='simple scatter example',
    x_axis_label='Mg' + wt%,
    y_axis_label='Si' + wt%

p.circle(x, y, legend_label='Trend', line_width=2)

st.bokeh_chart(p, use_container_width=True)
