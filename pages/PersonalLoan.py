import streamlit as st

st.sidebar.title("Welome Home!")


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
    "<div class='title'><h1>🏦 Question 1 of 3 For Personal Loan Approval 🏦</h1></div>",
    unsafe_allow_html=True,
)
