import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(
    page_title="BankEase : AI-Powered Branch Manager", page_icon="🏦", layout="wide"
)
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)
x = st.slider("x")  # 👈 this is a widget
st.write(x, "squared is", x * x)

st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name


st.write(st.session_state.name, "is a god", x * x)
if st.checkbox("Show dataframe"):
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

    chart_data

uploaded_file = st.file_uploader(
    "You can only upload txt excel png and jpg pigga",
    type=["txt", "xlsx", "png", "jpg"],
)

if uploaded_file is not None:
    st.success(f"File uploaded: {uploaded_file.name}")


st.title("Upload an MP4 Video")

uploaded_file = st.file_uploader(
    "You can  only Choose an MP4 video piggaFuc", type=["mp4"]
)

if uploaded_file is not None:
    st.video(uploaded_file)
    st.success(f"Uploaded: {uploaded_file.name}")

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?", ("Email", "Home phone", "Mobile phone")
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))


left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button("TOUCH me and see what HAPPENS LAVADEE!")

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio("MVP", ("Abhi", "Adit", "hemanth", "Sreesh", "Ronaldo"))
    st.write(f"God In Human Flesh Is {chosen}!")

st.title("What Type Of Loan Are You Looking For?")

if st.button("Personal Loan"):
    st.switch_page("pages/page_1.py")
if st.button("Home Loan"):
    st.switch_page("pages/page_1.py")
if st.button("Education Loan"):
    st.switch_page("pages/page_1.py")
if st.button("Vehicle Loan"):
    st.switch_page("pages/page_1.py")
