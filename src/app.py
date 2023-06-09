import time, av, cv2
import streamlit as st
from streamlit_webrtc import webrtc_streamer

st.title("STREAMLIT DEMO APP")
st.write("AUTH: hida.yusuke@gmail.com")

origin, canny = st.columns(2)

with origin:
    pass
with canny:
    threshold1 = st.slider("Canny1", min_value=0, max_value=150, step=1, value=100)
    threshold2 = st.slider("Canny2", min_value=0, max_value=150, step=1, value=100)

def canny_edge(frame):
    img = frame.to_ndarray(format="bgr24")
    img = cv2.cvtColor(cv2.Canny(img, threshold1, threshold2), cv2.COLOR_GRAY2BGR)
    
    return av.VideoFrame.from_ndarray(img, format="bgr24")


with origin:
    webrtc_streamer(key="origin")
with canny:
    pass
    #webrtc_streamer(key="S4u3MrURVcCJKyC5rBA2Vsv2uPbemRx8", video_frame_callback=canny_edge)
    
