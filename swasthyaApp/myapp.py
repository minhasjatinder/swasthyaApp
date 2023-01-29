import streamlit as st
import pandas as pd
import numpy as np


m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #90EE90;
    color:##000000;
    margin:12px 2px ; 
    width : 140px;
    height :50px;
    border-radius : 20%;
    font-size: 20px;
}

div.stButton > button:second-child {
    background-color: #90EE90;
    color:##000000;
    width : 20px;
    height :70px;
    border-radius : 20%;
    font-size: 20px;
}


div.stButton > button:hover {
    background-color: #90EE90;
    color:#000000;
    }

</style>""", unsafe_allow_html=True)
# Using object notation

add_selectbox = st.sidebar.button("""LIVER""")
add_selectbox = st.sidebar.button("""Cancer""")
add_selectbox = st.sidebar.button("""Kidney""")
add_selectbox = st.sidebar.button("""Dataset""")
add_selectbox = st.sidebar.button("""Live Cases""")
add_selectbox = st.sidebar.button("""Contact Us""")
st.sidebar.image("insta.jpg", caption='' , width = 50)
st.sidebar.image("linkedin.png", caption='', width = 50)
st.sidebar.image("logo-Meta.png", caption='', width = 50)
st.sidebar.image("twitter.png", caption='', width = 50)

from PIL import Image
image = Image.open(r"download.png")

st.image(image, caption='Sunrise by the mountains')
with st.container():
          
          with st.container():
                    
                    
            with st.form("my_form"):
                    col1, col2 , col3  = st.columns([1,3,1])

                    with col2:
                                st.markdown("""# 🩸Liver CIRRHOSIS🩸""")
                                st.subheader("Drop HERE Patient's record files")
                                uploaded_file = st.file_uploader("")
                                if uploaded_file is not None:
                                        # To read file as bytes:
                                        bytes_data = uploaded_file.getvalue()
                                        st.write(bytes_data)

                                        # To convert to a string based IO:
                                        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
                                        st.write(stringio)

                                        # To read file as string:
                                        string_data = stringio.read()
                                        st.write(string_data)

                                        # Can be used wherever a "file-like" object is accepted:
                                        dataframe = pd.read_csv(uploaded_file)
                                        st.write(dataframe)
                                title = st.text_input('Name', 'Your Name Here')
                                title = st.text_input('Age', 'Your Age Here')
                                title = st.text_input('Gender', 'Your Gender Here')
                                submitted = st.form_submit_button("Submit")
                    
                                    
          
          
                    

   # You can call any Streamlit command, including custom components:
   





# Using "with" notation
