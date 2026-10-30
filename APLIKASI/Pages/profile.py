import streamlit as st
import base64

st.title("☆≧ MY PROFILE ≦☆")
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

#BGP
set_background("bgp.jpg")

col1, col2, col3 = st.columns([4, 4, 4])

with col1:
    st.header("Halo Semuanya! Perkenalkan Nama Saya Adalah Rachqi Mulkan.")
    st.write("Saya merupakan mahasiswa semester 3 di Universitas Nurdin Hamzah Jambi, " \
             "Fakultas Ilmu Komputer, prodi Sistem Informasi. " \
             "Saya Lahir di Muara Sabak pada tanggal 8 maret 2007.")
    st.write("INI TAMPAK KECIL :")
    st.image("foto_k.jpg", width=300)
    st.write("Kegantengan")
    st.progress(10, text="10%")
    
    st.write("INI TAMPAK BESAR :")
    st.video("cidio.mp4", format="video/mp4", start_time=0, width=300)
    st.write("Kegantengan")
    st.progress(100, text="100%")

with col2:
    st.image("foto_bulan.png", width=380)
    st.header("Saya Memiliki Banyak Hobi, Diantaranya Adalah :")
    
    with st.container(border=True):
        st.write("1. Bermain Game")
        st.write("2. Membaca Buku")
        st.write("3. Menulis Cerita")
        st.write("4. Menonton Film")
        st.write("5. Mendengarkan Musik")
        st.write("6. Belajar Bahasa Asing")
        st.write("7. Menonton Bola")
    st.image("spot.jpg", width=380)
    st.image("foto_tangan.png", width=380)
    
with col3:
     with st.container(border=True):
        st.subheader("Kedokteran, hukum, bisnis, teknik—itu adalah tujuan yang mulia untuk mempertahankan hidup." \
                   "Tetapi puisi, kecantikan, romansa, cinta—itulah alasan kita tetap hidup.")
     st.image("fto8.jpg", width=380)
     st.audio("night_dancer.mp3", format="audio/mp3", autoplay=True, loop=True)

