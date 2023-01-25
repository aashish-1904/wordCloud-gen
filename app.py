import streamlit as st

import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
# import sys, os

st.title("Word Cloud Generator")

text = st.text_area("Paste your text here")
stopwords = STOPWORDS
# st.write(stopwords)
col = st.color_picker('pick a background color')
h = st.number_input('Height (in pixels)', min_value=100, step=100)
w = st.number_input('Width (in pixels)', min_value=100, step=100)

btn = st.button("Generate WordCloud")

if(btn):
    if(len(text)!=0):
        wc = WordCloud(
        background_color=col,
        stopwords=stopwords,
        height = h,
        width = w
        )
        if  wc.generate(text):
            pic = wc.to_image()
            st.image(pic)
            # st.download_button("Downlaod as '.png'", pic)
        else:
            st.error("Text is in improper format")      
    else:
        st.error("Need some text to generate a WordCloud")


