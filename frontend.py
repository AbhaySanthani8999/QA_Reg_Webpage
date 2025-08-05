import streamlit as st
import requests
from datetime import date

st.set_page_config(page_title="QA Test Registration", layout="centered")

st.title("🧪 QA Test Registration Form")

with st.form("reg_form"):
    col1, col2 = st.columns(2)
    first_name = col1.text_input("First Name")
    last_name = col2.text_input("Last Name")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    gender = st.selectbox("Gender", ["", "Male", "Female", "Other"])
    dob = st.date_input("Date of Birth", min_value=date(1900, 1, 1), max_value=date.today())
    country = st.selectbox("Country", ["", "India", "USA", "UK", "Germany", "Other"])
    terms = st.checkbox("I agree to the Terms and Conditions")

    submit = st.form_submit_button("Register")

    if submit:
        if not terms:
            st.warning("You must agree to the terms.")
        else:
            data = {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "password": password,
                "confirm_password": confirm_password,
                "gender": gender,
                "dob": dob.strftime("%Y-%m-%d"),
                "country": country,
                "terms": terms
            }

            try:
                res = requests.post("http://localhost:5000/register", json=data)
                if res.status_code == 200:
                    st.success(res.json().get("message", "Registration successful!"))
                    st.json(res.json()["data"])
                else:
                    st.error(res.json().get("message", "Registration failed."))
            except Exception as e:
                st.error(f"Could not connect to server: {e}")
