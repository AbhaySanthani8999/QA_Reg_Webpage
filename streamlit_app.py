import streamlit as st
from datetime import date
import re

st.set_page_config(page_title="QA Test Registration", layout="centered")
st.title("Registration Form")

with st.form("reg_form"):
    col1, col2 = st.columns(2)
    first_name = col1.text_input("First Name", "")
    last_name = col2.text_input("Last Name", "")

    email = st.text_input("Email", "")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    gender = st.selectbox("Gender", ["", "Male", "Female", "Other"])
    dob = st.date_input("Date of Birth", min_value=date(1900, 1, 1), max_value=date.today())
    country = st.selectbox("Country", ["", "India", "USA", "UK", "Germany", "Other"])
    terms = st.checkbox("I agree to the Terms and Conditions")

    submitted = st.form_submit_button("Register")

    if submitted:
        errors = []

        # Required field validations
        if not first_name.strip():
            errors.append("First Name is required.")
        if not last_name.strip():
            errors.append("Last Name is required.")
        if not email.strip():
            errors.append("Email is required.")
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            errors.append("Enter a valid email address.")
        if not password:
            errors.append("Password is required.")
        if not confirm_password:
            errors.append("Confirm Password is required.")
        if password and confirm_password and password != confirm_password:
            errors.append("Passwords do not match.")
        if not gender:
            errors.append("Please select your gender.")
        if not country:
            errors.append("Please select a country.")
        if not terms:
            errors.append("You must agree to the Terms and Conditions.")

        # Show errors or success
        if errors:
            for error in errors:
                st.error(error)
        else:
            st.success("✅ Registration successful!")
            st.json({
                "Full Name": f"{first_name} {last_name}",
                "Email": email,
                "Gender": gender,
                "Date of Birth": dob.strftime("%Y-%m-%d"),
                "Country": country
            })
