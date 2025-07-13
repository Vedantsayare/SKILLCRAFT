import streamlit as st
import os
import time
from datetime import datetime

LOG_FILE = "keylog.txt"

st.set_page_config(page_title="Keylogger", layout="centered")
st.title("Real-Time Keylogger Log Viewer")

# Clear log button
if st.button("Clear Log File"):
    open(LOG_FILE, "w").close()
    st.success("Log file has been cleared.")

log_box = st.empty()

if os.path.exists(LOG_FILE):
    with open(LOG_FILE, "r") as f:
        st.download_button("Download Log", data=f.read(), file_name="keylog.txt", mime="text/plain")

def format_log_with_timestamp():
    if not os.path.exists(LOG_FILE):
        return "Log file not found."

    with open(LOG_FILE, "r") as f:
        lines = f.readlines()

    formatted = ""
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            timestamp, key = line.split("::")
            dt = datetime.fromtimestamp(float(timestamp)).strftime("%Y-%m-%d %H:%M:%S")
            formatted += f"[{dt}] {key}\n"
        except:
            formatted += line + "\n"
    return formatted

while True:
    log_content = format_log_with_timestamp()
    log_box.text_area("Live Keystroke Log:", log_content, height=400, key="log_text", disabled=True)

    st.markdown("---")
    st.markdown("<p style='text-align: center; color: gray;'>Created by <b>Vedant Sayare</b></p>", unsafe_allow_html=True)

    time.sleep(2)
    st.experimental_rerun()
