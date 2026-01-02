
################### PB 711 #########################
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
st.set_page_config(page_title="Streamlit Example of PB",layout='wide')

name = st.text_input("Enter name")
age = st.slider("select age",10,100)
gender = st.radio("Choose Gender",['male','female','other'])
hobbies = st.multiselect(
"Select Hobbies",['Reading','Sports','music','travel','games','cooking'])
photo = st.file_uploader("Upload pofile pic",type = ['jpg','png','jpeg'])

if st.button("Submit Profile"):
    st.subheader("Profile Details")
    st.write("Name    -",name)
    st.write("Age     -",age)
    st.write("Gender  -",gender)
    st.write("hobbies -",", ".join(hobbies)) 
    if photo:
        st.image(photo,caption='profile pic',width=200)
