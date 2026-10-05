import streamlit as st
from PIL import Image

# 1. Konfigurasi Halaman Website
st.set_page_config(
    page_title="IMKS Cirebon",
    page_icon="🔴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS dengan Latar Belakang Utama MERAH MAROON & Teks Kontras Tinggi
custom_css = """
<style>
    /* Mengubah latar belakang seluruh aplikasi menjadi Merah Maroon */
    .stApp {
        background-color: #700000 !important;
        color: #ffffff !important;
    }
    
    /* Mengubah latar belakang Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #4a0000 !important;
    }
    
    /* Memastikan semua judul dan teks umum berwarna putih/terang */
    h1, h2, h3, h4, h5, h6, p, span, label, div {
        color: #ffffff !important;
    }

    /* Radio Button & Navigasi di Sidebar agar jelas terbaca */
    div[data-testid="stRadio"] label {
        color: #f1f1f1 !important;
        font-weight: 500;
    }

    /* Hero Section / Banner Utama */
    .hero-container {
        background: linear-gradient(135deg, #500000 0%, #800000 100%);
        color: white;
        padding: 35px 20px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 25px;
        border: 2px solid #a00000;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
    }
    
    .hero-title {
        font-size: 2.6rem;
        font-weight: 800;
        margin-bottom: 5px;
        color: #ffffff !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .hero-slogan {
        font-size: 1.4rem;
        font-style: italic;
        color: #ffdd77 !important; /* Warna Emas */
        margin-top: 10px;
        font-weight: bold;
    }

    /* Style Kartu Konten (Background Maroon Gelap dengan Teks Putih) */
    .card {
        background-color: #580000 !important;
        padding: 25px;
        border-radius: 12px;
        border: 1px solid #900000;
        border-left: 6px solid #ffdd77 !important; /* Akses Emas */
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        margin-bottom: 20px;
    }

    .card h2, .card h3, .card h4 {
        color: #ffdd77 !important; /* Judul dalam kartu berwarna emas agar menonjol */
        margin-top: 0;
    }

    /* Style Badge Divisi */
    .badge-divisi {
        background-color: #900000;
        color: #ffffff !important;
        padding: 5px 12px;
        border-radius: 6px;
        font-size: 0.85rem;
        font-weight: bold;
        display: inline-block;
        border: 1px solid #c00000;
    }

    /* Custom Input Form (Agar terlihat jelas di background gelap) */
    .stTextInput input, .stTextArea textarea {
        background-color: #4a0000 !important;
        color: #ffffff !important;
        border: 1px solid #a00000 !important;
    }

    /* Kustomisasi Tombol */
    div.stButton > button {
        background-color: #ffdd77 !important;
        color: #500000 !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 12px 24px !important;
        font-weight: bold !important;
        font-size: 1rem !important;
        width: 100%;
        transition: 0.3s;
    }
    
    div.stButton > button:hover {
        background-color: #ffffff !important;
        color: #800000 !important;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. Sidebar Navigation & Branding
with st.sidebar:
    # Menampilkan Logo IMKS
    try:
        logo = Image.open("Logo IMKS.jpeg")
        st.image(logo, use_column_width=True)
    except Exception:
        st.warning("📌 Simpan logo sebagai 'Logo IMKS.jpeg' di folder proyek.")

    st.markdown("<h2 style='text-align: center; color: #ffdd77 !important;'>IMKS CIREBON</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 0.9rem;'>Kabinet Perjuangan</p>", unsafe_allow_html=True)
    st.write("---")
    
    menu = st.radio(
        "Navigasi Utama:",
        ["Beranda", "Profil & Struktur", "Program Kerja", "Pendaftaran Anggota", "Kontak"]
    )
    
    st.write("---")
    st.caption("© 2026 Ikatan Mahasiswa Subang Cirebon")

# 4. Halaman: BERANDA
if menu == "Beranda":
    # Hero Section
    st.markdown("""
        <div class="hero-container">
            <div class="hero-title">IKATAN MAHASISWA SUBANG CIREBON</div>
            <p style="font-size: 1.2rem; margin-top: 10px; color: #f1f1f1 !important;">Wadah Silaturahmi dan Perjuangan Mahasiswa Asal Subang di Cirebon</p>
            <div class="hero-slogan">"Silih Asah, Silih Asih, Silih Asuh"</div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
            <div class="card">
                <h2>Selamat Datang di Portal IMKS Cirebon</h2>
                <p>Ikatan Mahasiswa Subang Cirebon (IMKS) merupakan organisasi daerah yang menghimpun seluruh mahasiswa asal Kabupaten Subang yang sedang menempuh pendidikan perguruan tinggi di wilayah Cirebon dan sekitarnya.</p>
                <p>Melalui semangat kebersamaan dan berasaskan kekeluargaan, IMKS hadir untuk membina potensi mahasiswa, menjaga budaya daerah, serta berkontribusi nyata bagi kemajuan daerah Subang dan Cirebon.</p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="card" style="text-align: center;">
                <h3>Ketua Umum</h3>
                <div style="width: 90px; height: 90px; background-color: #ffdd77; border-radius: 50%; color: #500000; display: flex; align-items: center; justify-content: center; margin: 10px auto 15px auto; font-size: 2.2rem; font-weight: bold;">
                    👨‍💼
                </div>
                <h4 style="margin: 0; color: #ffffff !important;">Muhammad Imam Mahdi</h4>
                <p style="color: #ffdd77 !important; font-size: 0.9rem; margin-top: 5px;">Ketua Umum IMKS Cirebon</p>
            </div>
        """, unsafe_allow_html=True)

# 5. Halaman: PROFIL & STRUKTUR
elif menu == "Profil & Struktur":
    st.markdown("<h2 style='color: #ffdd77 !important;'>Profil & Struktur Organisasi</h2>", unsafe_allow_html=True)
    st.write("---")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            <div class="card">
                <h3>Visi</h3>
                <p>Mewujudkan IMKS Cirebon sebagai wadah pemersatu mahasiswa Subang yang proaktif, berintegritas, serta berkontribusi aktif bagi masyarakat.</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="card">
                <h3>Misi</h3>
                <ul>
                    <li>Mempererat tali silaturahmi antar mahasiswa Subang di Cirebon.</li>
                    <li>Pengembangan potensi akademik dan non-akademik anggota.</li>
                    <li>Pengabdian masyarakat berbasis kearifan lokal.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<h3 style='color: #ffdd77 !important; margin-top: 20px;'>Pengurus Harian</h3>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Ketua Umum", "Muhammad Imam Mahdi")
    with c2:
        st.metric("Sekretaris Umum", "Ahmad Fauzi")
    with c3:
        st.metric("Bendahara Umum", "Siti Nurhaliza")

# 6. Halaman: PROGRAM KERJA
elif menu == "Program Kerja":
    st.markdown("<h2 style='color: #ffdd77 !important;'>Program Kerja Unggulan</h2>", unsafe_allow_html=True)
    st.write("---")

    proker_list = [
        {"nama": "Makrab & Makesta Anggota Baru", "divisi": "Kaderisasi", "desc": "Kegiatan penyambutan dan pengakraban mahasiswa baru asal Subang."},
        {"nama": "IMKS Mengabdi", "divisi": "Pengabdian Masyarakat", "desc": "Bakti sosial dan pendampingan pendidikan di desa terpencil Subang/Cirebon."},
        {"nama": "Subang Cultural Festival", "divisi": "Seni & Budaya", "desc": "Pentas seni dan kebudayaan khas Subang di kampus-kampus Cirebon."},
        {"nama": "Kajian & Diskusi Isu Daerah", "divisi": "Humas & Kajian", "desc": "Diskusi rutin membahas perkembangan dan kebijakan di Kabupaten Subang."}
    ]

    for pk in proker_list:
        st.markdown(f"""
            <div class="card">
                <h3 style="margin-bottom: 8px;">{pk['nama']}</h3>
                <span class="badge-divisi">Divisi: {pk['divisi']}</span>
                <p style="margin-top: 12px; font-size: 1.05rem; color: #f1f1f1 !important;">{pk['desc']}</p>
            </div>
        """, unsafe_allow_html=True)

# 7. Halaman: PENDAFTARAN ANGGOTA
elif menu == "Pendaftaran Anggota":
    st.markdown("<h2 style='color: #ffdd77 !important;'>Formulir Pendaftaran Anggota Baru</h2>", unsafe_allow_html=True)
    st.write("Mari bergabung menjadi bagian dari keluarga besar IMKS Cirebon!")
    st.write("---")

    with st.form("form_pendaftaran"):
        nama_lengkap = st.text_input("Nama Lengkap")
        kampus = st.text_input("Perguruan Tinggi / Kampus di Cirebon")
        jurusan = st.text_input("Jurusan & Angkatan")
        asal_kecamatan = st.text_input("Asal Kecamatan di Subang")
        no_hp = st.text_input("No. WhatsApp")
        alasan = st.text_area("Alasan Ingin Bergabung")
        
        submitted = st.form_submit_button("Kirim Pendaftaran")
        
        if submitted:
            if nama_lengkap and kampus and no_hp:
                st.success(f"Terima kasih {nama_lengkap}, data pendaftaran Anda telah diterima!")
            else:
                st.error("Mohon lengkapi formulir wajib terlebih dahulu.")

# 8. Halaman: KONTAK
elif menu == "Kontak":
    st.markdown("<h2 style='color: #ffdd77 !important;'>Hubungi Kami</h2>", unsafe_allow_html=True)
    st.write("---")

    st.markdown("""
        <div class="card">
            <h3>Sekretariat IMKS Cirebon</h3>
            <p>📍 Jl. Perjuangan No. 45, Sunyaragi, Kesambi, Kota Cirebon, Jawa Barat</p>
            <p>📧 Email: official@imkscirebon.org</p>
            <p>📱 WhatsApp: +62 812-3456-7890</p>
            <p>📸 Instagram: @imks_cirebon</p>
        </div>
    """, unsafe_allow_html=True)