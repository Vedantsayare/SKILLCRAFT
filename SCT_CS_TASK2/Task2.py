import streamlit as st
from PIL import Image
import numpy as np
import math
import io

def process_image(img, key, mode):
    img = img.convert("RGB")
    w, h = img.size
    pix = np.array(img)

    if mode == "decrypt":
        pix = np.flipud(pix)

    for i in range(w):
        for j in range(h):
            r, g, b = pix[j, i]
            shift = int(30 * math.sin(i + key))

            if mode == "encrypt":
                r = ((r + shift) % 256) ^ (key % 256)
                g = ((g + 2 * shift) % 256) ^ ((key * 2) % 256)
                b = ((b + 3 * shift) % 256) ^ ((key * 3) % 256)
            else:
                r = ((r ^ (key % 256)) - shift) % 256
                g = ((g ^ ((key * 2) % 256)) - 2 * shift) % 256
                b = ((b ^ ((key * 3) % 256)) - 3 * shift) % 256

            pix[j, i] = (r, g, b)

    if mode == "encrypt":
        pix = np.flipud(pix)

    return Image.fromarray(pix.astype(np.uint8))

st.title("Image Encryption & Decryption Tool")
st.markdown("Secure your image using creative pixel manipulation and a numeric key")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
key = st.number_input("Enter a numeric key", min_value=0, max_value=999999, step=1)

col1, col2 = st.columns(2)

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)

    if col1.button("Encrypt"):
        enc_img = process_image(image, key, "encrypt")
        st.image(enc_img, caption="Encrypted Image", use_column_width=True)
        buf = io.BytesIO()
        enc_img.save(buf, format="PNG")
        st.download_button("Download Encrypted Image", buf.getvalue(), file_name="encrypted.png", mime="image/png")

    if col2.button("Decrypt"):
        dec_img = process_image(image, key, "decrypt")
        st.image(dec_img, caption="Decrypted Image", use_column_width=True)
        buf = io.BytesIO()
        dec_img.save(buf, format="PNG")
        st.download_button("Download Decrypted Image", buf.getvalue(), file_name="decrypted.png", mime="image/png")

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Created by <b>Vedant Sayare</b></p>", unsafe_allow_html=True)
