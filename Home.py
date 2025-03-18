import streamlit as st

st.set_page_config(
    page_title="AI-Powered Branch Manager", page_icon="🏦", layout="wide"
)

st.sidebar.title("Welome Home!")

# Adding custom CSS for styling the page
st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(135deg, #0F2027, #203A43, #2C5364);
            color: white;
            text-align: center;
        }

        .title {
            font-size: 40px;
            font-weight: bold;
            color: #ffffff;
            margin-bottom: 25px;
        }

        .subtext {
            font-size: 18px;
            color: #dcdcdc;
            margin-bottom: 25px;
        }

        .button-container {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 20px;
        }
        .stButton>button {
            background: linear-gradient(135deg, #11998e, #38ef7d);
            color: white;
            border: none;
            padding: 15px 25px;
            font-size: 18px;
            font-weight: bold;
            border-radius: 10px;
            cursor: pointer;
            transition: 0.3s;
            min-width: 180px;
        }
        .stButton>button:hover {
            background: linear-gradient(135deg, #38ef7d, #11998e);
        }
    </style>
""",
    unsafe_allow_html=True,
)

# Title and subtitle
st.markdown(
    "<div class='title'><h1>🏦 Welcome to AI-Powered Branch Manager 🏦</h1></div>",
    unsafe_allow_html=True,
)

st.markdown(
    "<p class='subtext'>I'm here to assist you with your loan application process. Let's get started!</p>",
    unsafe_allow_html=True,
)

st.write("#### What type of loan would you like to apply for?")


col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Home Loan"):
        st.switch_page("pages/Upload.py")

with col2:
    if st.button("Education Loan"):
        st.switch_page("pages/Upload.py")

with col3:
    if st.button("Vehicle Loan"):
        st.switch_page("pages/Upload.py")

with col4:
    if st.button("Personal Loan"):
        st.switch_page("pages/Upload.py")


st.divider()
st.divider()

import streamlit as st
import os
from speechToText import (
    transcribe_audio,
)  # Assuming the speechToText.py file is in the same directory

# Streamlit UI for uploading .wav files
uploaded_file = st.file_uploader("Upload Audio File", type=["wav"], key="file1")

if uploaded_file is not None:
    # Save the uploaded file temporarily
    temp_file_path = "uploaded_audio.wav"
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"File uploaded: {uploaded_file.name}")
    st.audio(
        uploaded_file, format="audio/wav"
    )  # Display audio player for the uploaded file

    # Call the transcribe function
    try:
        st.write("🎙 Processing the audio... Please wait.")
        transcribe_audio(temp_file_path)

        # You can add more UI elements here to display the transcription (after it has been saved)
        with open("transcription.txt", "r") as transcription_file:
            transcription_text = transcription_file.read()

        st.text_area("Transcription:", transcription_text, height=300)
    except Exception as e:
        st.error(f"❌ Error during transcription: {str(e)}")
