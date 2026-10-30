import streamlit as st
import base64

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

#BGS
set_background("bgs.jpg")


st.title("☆≧ SOCIAL MEDIA ≦☆")
st.markdown("""
        <style>
        a[data-testid="stPageLink-NavLink"] {
            background-color: #1a4a6b !important;
            color: #1a4a6b !important;
            border-radius: 10px;
            padding: 0.5rem 1rem;
        }
        a[data-testid="stPageLink-NavLink"]:hover {
            background-color: #1a4a6b !important;
            color: #1a4a6b !important;
        }
        </style>
        """, unsafe_allow_html=True)
st.page_link("app.py", label="Back to Home", icon="🏠")

st.write(" Ayo gass!!! Ikuti akun media sosial saya di bawah ini:")

st.divider()

with st.container(border=True):
    st.subheader("🔗 Tautan Sosial Media")
    
        #link Instagram
    st.link_button("Instagram", "https://www.instagram.com/rchqiii?mdxt=Mnp3MnBycHlpdG9r", use_container_width=True)
        
        #link X
    st.link_button("X", "https://x.com/Okn1297438", use_container_width=True)
        
        # link tiktok
    st.link_button("TikTok", "https://www.tiktok.com/@shiahyeon8?_r=1&_t=ZS-9AxsxiGuRfw", use_container_width=True)

st.write("Terima kasih sudah berkunjung!")