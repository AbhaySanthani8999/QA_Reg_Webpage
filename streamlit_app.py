import streamlit as st
from datetime import date
import re

st.set_page_config(page_title="QA Test Registration", layout="centered")
st.title("Registration Form")

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

    submitted = st.form_submit_button("Register")

    if submitted:
        errors = []
        if not first_name: errors.append("First name is required.")
        if not last_name: errors.append("Last name is required.")
        if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email): errors.append("Valid email is required.")
        if not password: errors.append("Password is required.")
        if password != confirm_password: errors.append("Passwords do not match.")
        if not gender: errors.append("Gender is required.")
        if not country: errors.append("Country is required.")
        if not terms: errors.append("You must accept the terms and conditions.")

        if errors:
            for error in errors:
                st.error(error)
        else:
            st.success("✅ Registration successful!")
            st.json({
                "full_name": f"{first_name} {last_name}",
                "email": email,
                "gender": gender,
                "dob": dob.strftime("%Y-%m-%d"),
                "country": country
            })
