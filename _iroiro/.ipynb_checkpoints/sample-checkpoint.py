import streamlit as st
import altair as alt
import pandas as pd

st.title('Steamlitの基本的な使い方')

col1,col2 = st.columns(2)

with col1:
   num = st.slider('選択してください', min_value=0, max_value=100, value=30)
   st.write(f'選択した値：{num}ですですですですですですですですです')
with col2:
   val = st.selectbox('選択してください', ['a','b','c'])
