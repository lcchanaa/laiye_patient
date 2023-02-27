import streamlit as st

st.set_page_config(page_title="Patient Info System", layout="wide")
st.title("Patient Info System")

col1, col2 = st.columns(2)
patient_name = col1.text_input("Patient Name", key="patient_name")
country = col1.text_input("Country", key="country")
age = col1.text_input("Age", key="age")
genre = col1.radio("Gender", ("M", "F"), key="gender")
division = col1.selectbox("Division", ("<Please choose>", "Dermatology", "General Practice", "Orthopedics", "Physiotherapy", "Surgery"), key="division")
waiting_time = col1.text_input("Waiting Time", key="waiting_time")
visit_time = col1.text_input("Visit Time", key="visit_time")
report_date = col1.text_input("Report Date", key="report_date")

if st.button("Submit"):
    st.write("Patient record submitted")