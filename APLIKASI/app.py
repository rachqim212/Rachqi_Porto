import base64
import streamlit as st

st.set_page_config(
    page_title="Rachqi Mulkan Portofolio",
    page_icon="👻",
    layout="wide"
)

def set_background(image_file):
  with open(image_file, "rb") as f:
    encoded_string = base64.b64encode(f.read()).decode()

    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

#BG
set_background("APLIKASI/bg2.jpg")

col1, col2, col3 = st.columns([6, 3, 3])

with col1:
    st.title("☆(≧ MY PORTOFOLIO ≦)☆")
    st.subheader("Selamat datang di porofolio saya! Di sini, Anda dapat menemukan banyak informasi tentang saya! Selamat menjelajah!!!")
    st.markdown("""
        <style>
        a[data-testid="stPageLink-NavLink"] {
            background-color: #8e44ad !important;
            color: #ffffff !important;
            border-radius: 10px;
            padding: 0.5rem 1rem;
        }
        a[data-testid="stPageLink-NavLink"]:hover {
            background-color: #6c3483 !important;
            color: #ffffff !important;
        }
        </style>
        """, unsafe_allow_html=True)
    
    st.page_link("pages/profile.py", label="Profile", icon="👤")
    st.page_link("pages/skill_and_ability.py", label="Abilities", icon="⚡")
    st.page_link("pages/social_media.py", label="Social Media", icon="🌐")


with col2:
    st.image("fto2.jpg", width=200)
    st.image("fto1.jpg", width=200)

with col3:
    st.video("xidio.mp4", format="video/mp4", start_time=0, width=300, autoplay=True, loop=True)
    
