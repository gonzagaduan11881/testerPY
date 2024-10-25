import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Tutorial Desain Streamlit UTS ML 24/25",
                            ['Klasifikasi',
                            'Regresi','Catatan'],
                            default_index=0)

if selected == 'Klasifikasi':
    st.title('Klasifikasi')
    
    st.write('Untuk Inputan File dataset (csv) bisa menggunakan st.file_uploader')
    file = st.file_uploader("Masukkan File", type=["csv", "txt"])
    st.write('Untuk usia bisa menggunakan st.slider')
    Age = st.slider("Age", 0, 100)
    st.write('Untuk jenis kelamin bisa menggunakan st.radio')
    Sex = st.radio("Gender", ["Female", "Male"])
    st.write('Untuk nama kolom bisa menggunakan st.selectbox')
    nama_kolom = st.selectbox("Nama Kolom", ["Under", "Normal", "Over"])
    st.write('Untuk input manual bisa menggunakan st.number_input')
    panjang = st.number_input("Masukan Nilai Panjang")
    lebar = st.number_input("Masukan Nilai Lebar")
    
    jawban = st.number_input("Masukan Jawaban Anda", min_value=0)
    st.write('Tombol button(Menggunakan st.button)')
    hitung = st.button("Prediksi")
    
    if hitung:
        luas_benar = panjang * lebar
        st.write(f"Panjang: {panjang}, Lebar: {lebar}")
        jawaban = st.number_input("Masukkan Jawaban Anda", min_value=0)
        if st.button("Tombol Cek"):
            if jawaban == luas_benar:
                st.success(f"Benar! Luas Persegi Panjang adalah {luas_benar}.")
            else:
                st.error(f"Salah! Luas Persegi Panjang yang benar adalah {luas_benar}.")

if selected == 'Regresi':
    st.title('Regresi')
    
    st.write('Untuk Inputan File dataset (csv) bisa menggunakan st.file_uploader')
    file = st.file_uploader("Masukkan File", type=["csv", "txt"])
    st.write('Untuk usia bisa menggunakan st.slider')
    Age = st.slider("Age", 0, 100)
    st.write('Untuk jenis kelamin bisa menggunakan st.radio')
    Sex = st.radio("Gender", ["Female", "Male"])
    st.write('Untuk nama kolom bisa menggunakan st.selectbox')
    nama_kolom = st.selectbox("Nama Kolom", ["Under", "Normal", "Over"])
    st.write('Untuk input manual bisa menggunakan st.number_input')
    panjang = st.number_input("Masukan Nilai Panjang")
    lebar = st.number_input("Masukan Nilai Lebar")
    alas = st.number_input("Masukan Nilai Alas", 0, 100)
    tinggi = st.slider("Masukkan Nilai Tinggi", 0, 100)
    hitung = st.button("Menggunakan st.button")

    if hitung:
        luas = 0.5 * alas * tinggi
        st.write(f"Luas Segitiga Adalah", luas)

if selected == 'Catatan':
    st.title('Catatan')
    st.write('''1. Untuk memunculkan sidebar agar tidak error ketika di run, Silahkan install library streamlit option menu di terminal dengan perintah "pip install streamlit-option-menu".''')
    st.write('2. Terdapat 3 Menu yaitu Klasifikasi dan Regresi.')
    st.write('3. Isi code streamlit.py, sesuaikan dengan arsitektur root code anda pada notebook.')
    st.write('4. Untuk run streamlit dapat di akses pada https://streamlit.io/')
    st.write('5. Library pandas, numpy dll dapat diakses pada https://apputsc-f6gzfv1uidiyib9j&hnfk7r.streamlit.app/')
    st.write('6. Link pada catatan ini sangat disarankan digunakan untuk deploy online di github ada 5 yaitu streamlit, pandas, numpy, scikit-learn, streamlit-option-menu.''')