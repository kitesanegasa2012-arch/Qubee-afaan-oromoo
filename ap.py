import os
import streamlit as st

st.set_page_config(page_title="Qubee Afaan Oromoo", page_icon="🔤", layout="centered")

# Dizaayinii fi Miidhagina (CSS Styling)
st.markdown("""
<style>
    /* Background gadi fagoo fi miidhagaa */
    .stApp {
        background: linear-gradient(135deg, #0b0f19 0%, #1e293b 100%);
        color: #f8fafc;
    }

    /* Mata-Duree (Title) */
    h1 {
        color: #fef08a !important;
        text-align: center;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-shadow: 0 2px 10px rgba(212,175,55,0.3);
    }

    p {
        text-align: center;
        color: #cbd5e1;
        font-size: 16px;
    }

    /* Button-wwan qubeewwanii (Border, Gradient fi Hover effect) */
    div.stButton > button {
        background: linear-gradient(135deg, #1e3a8a, #2563eb);
        color: white;
        border-radius: 14px;
        border: 2px solid rgba(212, 175, 55, 0.4);
        font-size: 22px;
        font-weight: bold;
        padding: 16px 0px;
        width: 100%;
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease-in-out;
    }

    /* Yeroo Mouse irra buusu (Hover) */
    div.stButton > button:hover {
        transform: translateY(-4px);
        background: linear-gradient(135deg, #2563eb, #3b82f6);
        border-color: #fef08a;
        box-shadow: 0 10px 20px rgba(59, 130, 246, 0.4);
    }

    /* Yeroo tuqu (Active) */
    div.stButton > button:active {
        transform: scale(0.96);
    }
</style>
""", unsafe_allow_html=True)

st.title("🔤 Qubee Afaan Oromoo Dubbisu")
st.write("Qubee tokko tokko xuqii sagalee isaa dhaggeeffadhu!")
st.write("") 

qubeewwan = [
    "A", "B", "C", "CH", "D", "DH", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
    "N", "NY", "O", "P", "PH", "Q", "R", "S", "SH", "T", "U", "V", "W", "X", "Y", "Z"
]

cols = st.columns(4)
for i, q in enumerate(qubeewwan):
    with cols[i % 4]:
        if st.button(q, key=f"btn_{q}", use_container_width=True):
            audio_path = f"{q.lower()}.mp3"
            if os.path.exists(audio_path):
                st.audio(audio_path)
            else:
                st.warning(f"Sagaleen qubee '{q}' hin argamne!") 
