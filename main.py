import streamlit as st
import pandas as pd
import re
import random

#open data.csv
df = pd.read_csv('data3.csv')

#choose random 3 rows from the dataframe
df1 = df.sample(n=3)
#show card with title and text
st.title('YEE PICTIONARY. Pick a charracter to draw :)')
st.text('Click the button to shuffle')

#3 columns
col1, col2, col3 = st.columns(3)

#write the first column
with col1:
    #streamlit.write the dataframe
    st.write(df1.iloc[0]["fs14"])
    st.write(df1.iloc[0]["title"])
    #link to the website
    l1 = df1.iloc[0]["lazyloaded src"]
    st.write(
        f'<iframe src={l1}></iframe>'.format(l1=l1),
        unsafe_allow_html=True,
    )
    #st.markdown(df1.iloc[0]["fl-l href"], unsafe_allow_html=True)
#write the second column
with col2:
    #streamlit.write the dataframe
    st.write(df1.iloc[1]["fs14"])
    st.write(df1.iloc[1]["title"])
    #link to the website
    l1 = df1.iloc[1]["lazyloaded src"]
    st.write(
        f'<iframe src={l1}></iframe>'.format(l1=l1),
        unsafe_allow_html=True,
    )
#write the third column
with col3:
    #streamlit.write the dataframe
    st.write(df1.iloc[2]["fs14"])
    st.write(df1.iloc[2]["title"])
    #link to the website
    l1 = df1.iloc[2]["lazyloaded src"]
    st.write(
        f'<iframe src={l1}></iframe>'.format(l1=l1),
        unsafe_allow_html=True,
    )

#streamlit.write the dataframe

#add a button
if st.button('Shuffle'):
    #choose random 3 rows from the dataframe
    df1 = df.sample(n=3)
    #streamlit.write the dataframe
    #st.write(df1)