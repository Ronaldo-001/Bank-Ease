import streamlit as st

page_name = "Upload Page"
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

st.sidebar.title(page_name)


st.title("DOCUMENT UPLOAD")


enable = st.checkbox("Enable camera")
picture = st.camera_input("Take a picture", disabled=not enable)

if picture:
    st.image(picture)

audio_value = st.audio_input("Record a voice message")

if audio_value:
    st.audio(audio_value)

col1, col2, col3 = st.columns(3)

with col1:
    uploaded_file = st.file_uploader(
        "UPLOAD AADHAR CARD",
        type=["png", "jpg", "jpeg"],
        key="file1",
    )
    if uploaded_file is not None:
        st.image(uploaded_file)
        st.success(f"File uploaded: {uploaded_file.name}")

with col2:
    uploaded_file2 = st.file_uploader(
        "UPLOAD PAN CARD",
        type=["png", "jpg", "jpeg"],
        key="file2",
    )

    if uploaded_file2 is not None:
        st.image(uploaded_file2)
        st.success(f"File uploaded: {uploaded_file.name}")

with col3:
    uploaded_file3 = st.file_uploader(
        "UPLOAD INCOME PROOF",
        type=["png", "jpg", "jpeg"],
        key="file3",
    )

    if uploaded_file is not None:
        st.image(uploaded_file3)
        st.success(f"File uploaded: {uploaded_file.name}")

video_file = open("IntroductionVideoPersonalLoan.webm", "rb")
video_bytes = video_file.read()

st.video(video_bytes)

col1, col2 = st.columns(2)

with col1:
    if st.button("Home"):
        st.switch_page("Home.py")

with col2:
    if st.button("OK"):
        st.switch_page("PersonalLoan.py")
