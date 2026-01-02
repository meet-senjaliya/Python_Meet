
import streamlit as st
st.set_page_config(page_title="Hello Streamlit",layout='centered')

st.title("welcom to streamlit 😁😁")

#### IMAGE DISPLAY

st.header("Web Image Display")
st.image("https://picsum.photos/600/300",
        caption = "Random Image",
        use_container_width = True) 


st.header("Local Image Display")
st.image("python.jpg",
        caption = "python Image",
        use_container_width = True) 

#### AUDIO
st.header("audio files")
st.audio("sampleaudio.mp3") 
         
### VIDEO
st.header("video files")
st.video("samplevideo.mp4") 


### DATA DISPLAY
import pandas as pd
st.header("Displaying Data")
data = {
    "student" : ['A','B','C','D'],
    "Marks" : [85,92,76,24],
    "Passed" : [True,True,True,False]
}

df = pd.DataFrame(data)

st.subheader("st.dataframe")
st.dataframe(df)

st.subheader("st.table")
st.table(df)

st.subheader("Json - Javascript object natation")
st.json(data)

### STATUS ELEMENTS
import time
st.info("Useful information")
if st.button("start long run"):
    progress = st.progress(0)
    with st.spinner("processing"):
        for i in range(100):
            time.sleep(0.03)
            progress.progress(i+1)
    st.success("Task Completed")
    st.balloons()
    
    
### MATPLOTLIB CHARTS
import matplotlib.pyplot as plt
import numpy as np

st.subheader("Line chart")
x = np.arange(1,11)
y  =np.random.randint(50,100,size=10)

plt.figure(figsize = (6,4))
plt.plot(x,y,"o")
plt.xlabel("X label")
plt.ylabel("Y label")
plt.title("Matplotlib based linechart")

st.pyplot(plt)

### STREAMLIT NATIVE CHARTS
st.subheader("Streamlit based charts")
df1 = pd.DataFrame({
    "student":x,
    "Marks" :y
})
st.line_chart(df1)
