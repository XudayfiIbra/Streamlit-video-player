import streamlit as st
import tempfile
import os

st.title("EASTCODE VIDEO PLAYER")
uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "mov"])

if uploaded_file is not None:
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(uploaded_file.read())
    st.video(temp_file.name)

    st.write(f"Filename: {uploaded_file.name}")
    st.write(f"File Size: {uploaded_file.size / (1024*1024):.2f} MB")

    temp_file.close()
    os.remove(temp_file.name)
