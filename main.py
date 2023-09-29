import streamlit as st 
import requests
from bs4 import BeautifulSoup
import webbrowser
import time

st.set_page_config(page_title="Unsplash Web Scraper", page_icon='./favicon.png')

def download_func():
  print('working')

st.markdown(r"""
<style>
footer { visibility: hidden; }
h1 {text-align:center}
</style>
""", unsafe_allow_html=True)

st.title('Unsplash Web Scraper')

with st.form('Search'):
   keyword = st.text_input('Enter Keyword to Scrape') 
   search = st.form_submit_button('Search')

if keyword:
    print(keyword)
    page = requests.get(f"https://unsplash.com/s/photos/{keyword}")
    print(page.status_code)
    soup = BeautifulSoup(page.content , 'lxml')
    rows = soup.find_all("div" , class_= "MorZF")
    col1 , col2 = st.columns(2)

    for i in range(0,20):
      image = rows[i].find('img')['src']
      print(rows)
      anchor = rows[i].find("a")
      print(anchor)
      
      if i%2 == 0:
        col1.image(image)
        btn = col1.button("Download", key=i)
        if btn:
          webbrowser.open_new_tab(image)
      else:
       col2.image(image)
       btn = col2.button("Download" , key=i)
       if btn :
              webbrowser.open_new_tab(image)


