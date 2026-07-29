import os
import streamlit as st

st.set_page_config(page_title="Qubee Afaan Oromoo", page_icon="🔤")

st.title("🔤 Qubee Afaan Oromoo Dubbisu")
st.write("Qubee tokko tokko xuqii sagalee isaa dhaggeeffadhu!")

qubeewwan = [
    "A", "B", "C", "CH", "D", "DH", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
    "N", "NY", "O", "P", "PH", "Q", "R", "S", "SH", "T", "U", "V", "W", "X", "Y", "Z"
]

cols = st.columns(4)
for i, q in enumerate(qubeewwan):
    with cols[i % 4]:
        if st.button(q, use_container_width=True):
            audio_path = f"audio/{q.lower()}.mp3"
            if os.path.exists(audio_path):
                st.audio(audio_path)
            else:
                st.warning(f"Sagaleen qubee '{q}' hin argamne!")
