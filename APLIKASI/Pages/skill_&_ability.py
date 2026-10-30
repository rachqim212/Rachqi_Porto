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

#BGA
set_background("bga.jpg")

st.title("☆≧ ABILITIES ≦☆")

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

st.header("Halo, saya Rachqi Mulkan!")
st.write("Selamat datang di halaman tentang diri saya.")

st.divider()

col1, col2 = st.columns([3, 3])

with col1:
    
    with st.container(border=True):
        st.subheader("Tentang Saya")
        st.write("Saya adalah seseorang yang senang belajar hal baru.")
    
    with st.container(border=True):
        st.subheader("Minat Saya")
        st.markdown("""
        - Saya tertarik dengan teknologi dan komputer
        - Saya juga tertarik dengan dunia pemrograman
        """)

    with st.container(border=True):
         st.subheader("Kemampuan Saya")
         st.write("Saya sedang mengembangkan kemampuan dalam beberapa hal:")
         st.markdown("""
            - Dasar-dasar pemrograman
            - Basic aplikasi perkantoran (Word & Excel)
            - Editing
        """)

    st.image("fto3.jpg", width=380)
    st.audio("dracula.mp3", format="audio/mp3", autoplay=True, loop=True)

with col2:
    with st.container(border=True):
        st.video("kidio.mp4", format="video/mp4", start_time=0, width=300, autoplay=True, loop=True)
        st.write("**Bahasa Indonesia**")
        st.progress(95, text="95%")
        
        st.write("**Bahasa Inggris**")
        st.progress(85, text="85%")

        st.write("**Bahasa Asing Yang Lain**")
        st.progress(30, text="30%")

        st.write("**Basa Basi**")
        st.progress(80, text="80%")

    with st.container(border=True):
        st.subheader("Tujuan Saya")
        st.write("Saya ingin terus belajar, menambah pengalaman, dan menggunakan kemampuan saya untuk hal yang bermanfaat dan berguna di masa depan.")

st.markdown("<br>", unsafe_allow_html=True)