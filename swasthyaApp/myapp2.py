import streamlit as st
import pandas as pd
import numpy as np


m = st.markdown("""
<style>
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.css-163ttbj.e1fqkh3o11 > div.css-6qob1r.e1fqkh3o3 > div.css-1vq4p4l.e1fqkh3o4 > div > div:nth-child(1) > div > div:nth-child(7) > div > div > div > img{
  


}
div.stButton > button:first-child {
    background-color: #ADD8E6;
    color:##000000;
    margin:12px 2px ; 
    width : 140px;
    height :50px;
    border-radius : 20%;
    font-size: 20px;
}




div.stButton > button:hover {
    background-color: #90EE90;
    color:#000000;
    }
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.css-k1vhr4.egzxvld3 > div > div:nth-child(1) > div > div:nth-child(3) > div > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div > div > div > button{

    background-color: #90EE90;
    color:##000000;
    margin:12px 2px ; 
    width : 200px;
    height :100px;
    border-radius : 20%;
    font-size: 20px;

}

 #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.css-k1vhr4.egzxvld3 > div > div:nth-child(1) > div > div:nth-child(3) > div > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div > div > div > button{
    background-color: #90EE90;
    color:##000000;
    margin:12px 2px ; 
    width : 200px;
    height :100px;
    border-radius : 20%;
    font-size: 20px;
 
 }



#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.css-k1vhr4.egzxvld3 > div > div:nth-child(1) > div > div:nth-child(3) > div > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div > div > div > button{

    background-color: #90EE90;
    color:##000000;
    margin:12px 2px ; 
    width : 200px;
    height :100px;
    border-radius : 20%;
    font-size: 20px;



}

#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.css-k1vhr4.egzxvld3{

margin: 3px ; 
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
image = Image.open(r"C:\Users\Jatinder Kaur\Downloads\download.png")

st.image(image, caption='Swasthya App')
with st.container():
          
          
          with st.container():
                    
                    col1, col2 , col3  = st.columns([1,1,1])
                    with col1 :
                        st.button("Liver")
                    with col2 :
                        st.button("KIDNEY")
                    with col3 :
                        st.button("CANCER")
                    col1, col2   = st.columns([2,1])

                    choice= ""
                    with col2:
                        choice = st.text_input("Search:", key="choice")
                    col1 , col2 = st.columns([1 , 0.01])
                    with col1:
                        df = pd.DataFrame(
                            np.random.randn(5, 5),
                            columns=('col %d' % i for i in range(5)))

                            # Same as st.write(df)         
                        if choice == "":
                    #if nothing is inputed display pandas df as is
                    
                                            st.dataframe(data=df.head(50), height=300 ,width= 900)
                        else:
                                            df[df.apply(lambda r: any([kw in r[0] for kw in choice]), axis=1)]
    # You can call any Streamlit command, including custom components:
    





# Using "with" notation
