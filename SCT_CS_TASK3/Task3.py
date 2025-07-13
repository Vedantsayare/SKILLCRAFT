import streamlit as st
import re

def check_password_strength(password):
    score = 0
    remarks = []

    if len(password) >= 8:
        score += 1
        remarks.append("Good length (8+ characters)")
    else:
        remarks.append("Too short (should be at least 8 characters)")

    if re.search(r"[A-Z]", password):
        score += 1
        remarks.append("Contains uppercase letters")
    else:
        remarks.append("Missing uppercase letters")

    if re.search(r"[a-z]", password):
        score += 1
        remarks.append("Contains lowercase letters")
    else:
        remarks.append("Missing lowercase letters")

    if re.search(r"[0-9]", password):
        score += 1
        remarks.append("Contains digits")
    else:
        remarks.append("Missing digits")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
        remarks.append("Contains special characters")
    else:
        remarks.append("Missing special characters")

    if score == 5:
        strength = "Very Strong"
        color = "green"
    elif score >= 3:
        strength = "Moderate"
        color = "orange"
    else:
        strength = "Weak"
        color = "red"

    return strength, remarks, color

st.set_page_config(page_title="Password Strength Checker", layout="centered")
st.title("Password Strength Checker")

with st.form("password_form"):
    password = st.text_input("Enter your password", type="password", placeholder="Type your password...")
    submitted = st.form_submit_button("Check Password")

if submitted:
    if password:
        strength, feedback, color = check_password_strength(password)
        st.markdown(f"### Strength: :{color}[{strength}]")
        st.markdown("#### Criteria Check:")
        for remark in feedback:
            st.write(remark)
    else:
        st.warning("Please enter a password before checking.")

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Created by <b>Vedant Sayare</b></p>", unsafe_allow_html=True)
