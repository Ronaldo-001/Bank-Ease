import streamlit as st
import easyocr
import re

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

# Function to extract Aadhaar details
def extract_aadhaar_details(image_path):
    recognition_results = reader.readtext(image_path, detail=0)
    extracted_text = " ".join(recognition_results)
    
    details = {}
    name, dob, aadhaar_number, sex = None, None, None, None

    # Determine gender
    if 'female' in extracted_text.lower():
        sex = "FEMALE"
    else:
        sex = "MALE"

    # Extract DOB
    try:
        dob = re.search(r'\d{2}/\d{2}/\d{4}', extracted_text).group()
    except:
        dob = "Not Found"

    # Extract Aadhaar Number
    try:
        aadhaar_number = re.search(r'\d{4}\s\d{4}\s\d{4}', extracted_text).group()
    except:
        aadhaar_number = "Not Found"

    # Extract Name
    lines = extracted_text.split(',')
    for line in lines:
        line_cleaned = line.strip().replace('\n', '').rstrip().lstrip()
        if re.search(r'[A-Za-z]+\s[A-Za-z]+', line_cleaned) and "DOB" not in line_cleaned and "Male" not in line_cleaned:
            name = line_cleaned
            break

    # Clean Name
    if name:
        name = re.sub('[^a-zA-Z ]+', '', name)
    else:
        name = "Not Found"

    details['Name'] = name
    details['Date of Birth'] = dob
    details['Aadhaar Number'] = aadhaar_number
    details['Sex'] = sex

    return details

# Function to extract PAN details
def extract_pan_details(image_path):
    recognition_results = reader.readtext(image_path, detail=0)
    extracted_text = " ".join(recognition_results)

    details = {}
    
    # Extract Name
    name_match = re.search(r'(?:Name|नाम)\s*[:\-]?\s*([A-Z\s]+)', extracted_text)
    
    # Extract Father's Name
    father_name_match = re.search(r"(?:Father's Name|पिता का नाम)\s*[:\-]?\s*([A-Z\s]+)", extracted_text)
    
    # Extract DOB
    dob_match = re.search(r'(?:Date of Birth|जन्म की तारीख)\s*[:\-]?\s*(\d{2}/\d{2}/\d{4})', extracted_text)
    
    # Extract PAN Number
    pan_number_match = re.search(r'[A-Z]{5}\d{4}[A-Z]', extracted_text)

    details['Name'] = name_match.group(1).strip() if name_match else "Not Found"
    details['Father\'s Name'] = father_name_match.group(1).strip() if father_name_match else "Not Found"
    details['DOB'] = dob_match.group(1).strip() if dob_match else "Not Found"
    details['PAN Number'] = pan_number_match.group(0).strip() if pan_number_match else "Not Found"

    return details

# Streamlit UI Code
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

col1, col2, col3 = st.columns(3)

with col1:
    uploaded_aadhaar_file = st.file_uploader(
        "UPLOAD AADHAAR CARD",
        type=["png", "jpg", "jpeg"],
        key="aadhaar_file",
    )
    
with col2:
    uploaded_pan_file = st.file_uploader(
        "UPLOAD PAN CARD",
        type=["png", "jpg", "jpeg"],
        key="pan_file",
    )

if uploaded_aadhaar_file is not None:
    st.image(uploaded_aadhaar_file, caption="Uploaded Aadhaar Card")
    
    with open("temp_aadhaar.jpg", "wb") as f:
        f.write(uploaded_aadhaar_file.getbuffer())
    
    aadhaar_details = extract_aadhaar_details("temp_aadhaar.jpg")
    
    st.subheader("Extracted Aadhaar Details:")
    st.json(aadhaar_details)

if uploaded_pan_file is not None:
    st.image(uploaded_pan_file, caption="Uploaded PAN Card")
    
    with open("temp_pan.jpg", "wb") as f:
        f.write(uploaded_pan_file.getbuffer())
    
    pan_details = extract_pan_details("temp_pan.jpg")
    
    st.subheader("Extracted PAN Details:")
    st.json(pan_details)