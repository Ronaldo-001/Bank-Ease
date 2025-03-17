import streamlit as st

st.set_page_config(page_title="AI-Powered Branch Manager", page_icon="🏦", layout="wide")


st.markdown("""
    <style>
        /* Background gradient for a professional look */
        .stApp {
            background: linear-gradient(135deg, #0F2027, #203A43, #2C5364);
            color: white;
            text-align: center;
        }

        /* Title styling */
        .title {
            font-size: 40px;
            font-weight: bold;
            color: #ffffff;
            margin-bottom: 15px;
        }

        /* Subtitle styling */
        .subtext {
            font-size: 18px;
            color: #dcdcdc;
            margin-bottom: 25px;
        }

        /* Button Styling */
        .button-container {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 20px;
        }
        .button {
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
        .button:hover {
            background: linear-gradient(135deg, #38ef7d, #11998e);
        }
    </style>
""", unsafe_allow_html=True)

# --- UI COMPONENTS ---
st.markdown("<div class='title'><h1>Welcome to AI-Powered Branch Manager</h1></div>", unsafe_allow_html=True)

st.markdown("<p class='subtext'>I'm here to assist you with your loan application process. Let's get started!</p>", unsafe_allow_html=True)

st.write("#### What type of loan would you like to apply for?")

# Buttons in a single row using HTML
st.markdown("""
    <div class='button-container'>
        <button class='button'>Home Loan</button>
        <button class='button'>Education Loan</button>
        <button class='button'>Vehicle Loan</button>
        <button class='button'>Personal Loan</button>
    </div>
""", unsafe_allow_html=True)
