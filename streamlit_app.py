"""
# My first app
Here's our first attempt at using data to create a table:
"""



import streamlit as st

st.write("Hello world....")


import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 4099999] 
}) 


# test out some charts - read from data file and display


df