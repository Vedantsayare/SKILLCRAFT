import streamlit as st

def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            if mode == "Encrypt":
                result += chr((ord(char) - start + shift) % 26 + start)
            else:
                result += chr((ord(char) - start - shift) % 26 + start)
        else:
            result += char
    return result

def brute_force_decrypt(text):
    all_attempts = []
    for shift in range(1, 26):
        decrypted = caesar_cipher(text, shift, "Decrypt")
        all_attempts.append((shift, decrypted))
    return all_attempts

st.set_page_config(page_title="Caesar Cipher Tool", layout="centered")

st.title("Caesar Cipher Web App")
st.write("Encrypt, Decrypt or Brute-force Caesar cipher text.")

message = st.text_area("Enter your message", height=150)

mode = st.selectbox("Mode", ["Encrypt", "Decrypt", "Brute Force Decrypt"])

if mode != "Brute Force Decrypt":
    shift = st.number_input("Enter shift (1-25)", min_value=1, max_value=25, step=1)

if st.button("Process"):
    if not message.strip():
        st.warning("Please enter a message.")
    else:
        if mode == "Brute Force Decrypt":
            st.subheader("Brute Force Results:")
            attempts = brute_force_decrypt(message)
            for s, result in attempts:
                st.write(f"**Shift {s:2}:** {result}")
        else:
            result = caesar_cipher(message, shift, mode)
            st.success("Operation Completed")
            st.code(result, language="text")

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Created by <b>Vedant Sayare</b></p>", unsafe_allow_html=True)
