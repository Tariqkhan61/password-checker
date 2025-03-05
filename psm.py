# Project 02: Password Strength Meter Sir Zia Project 3
# Objective:
# Build a password strength meter in python that evaluates a user's password based on security rules.
# The program will

# Analyze password based on length, character types, and patterns.
# Assign a strength score (weak, Moderate, Strong).
# Provide feedback to improve weak passwords.
# Use control flow, type casting, strings, and functions.

# REQUIREMENTS
# 1- Password Strength Crieteria

# A strong password should:
# ✅ Be atleast 8 character long.
# ✅ Contain Prepration and lower case letter.
# ✅ Include atleast one digit(0-9).
# ✅ Include atleast one special character (!@#$%&^).

# 2- Scoring system

# Weak (score: 1-2) -> short, missing key elements.
# Moderate (score: 3-4) -> Good but missing some security features.
# Strong (score: 5) -> meets all criteria.

# 3- Feedback system

# If the password is weak, suggest improvements.
# If the password is strong,display a success message.

# ****************   Start Coding    **************



import re
import streamlit as st

# Page Style
st.set_page_config(page_title="Password Strength Checker by Muhammad Tariq Mahboob", page_icon="🔑", layout="centered")

# Custom CSS
st.markdown(""" 
<style>
.main {text-align: center;}
.stTextInput {width: 60% !important; margin: auto;}
.stButton button {width: 50%; background-color: rgb(62, 7, 242); color: white; font-size: 18px;}
.stButton button:hover {background-color: red; color: white;}
</style>
""", unsafe_allow_html=True)

# Page Title and Description
st.title("🔒 Password Strength Evaluator")
st.write("Please enter your password below to verify its security strength.. 🔍")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **at least 8 characters long**.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **both uppercase (A-Z) and lowercase (a-z)**.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one number (0-9)**.")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one special character (!@#$%^&*)**.")

    # Display Password strength result
    if score == 4:
        st.success("✅ **Strong Password** - Your Password is secure.")
    elif score == 3:
        st.info("☢️ **Moderate Password** - Consider improving security by adding more features.")
    else:
        st.error("❌ **Weak Password** - Follow the suggestions below to strengthen it.")

    # Feedback
    if feedback:
        with st.expander("🔍 **Improve your password**"):
            for item in feedback:
                st.write(item)

password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong 🔒")

# Button Working
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")  # Show warning if password is empty
