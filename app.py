import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model_kualitas_air.pkl")

st.set_page_config(
    page_title="Prediksi Kualitas Air",
    page_icon="💧"
)

st.title("💧 Sistem Prediksi Kualitas Air")
st.subheader("Berbasis Machine Learning Random Forest")
st.markdown("### Kelompok")
st.write("Adolfince Dormina Yapen")
st.write("Nur Anisa Jamil")
st.write("Raysha Imania Siswandi")
st.write("Siti Septiani")
st.write("Widya Ohibor")
st.info(
    "Website ini digunakan untuk memprediksi kualitas air berdasarkan parameter lingkungan menggunakan algoritma Random Forest."
)

st.write("Masukkan parameter kualitas air untuk mengetahui apakah air aman digunakan.")

temperatur = st.number_input("Temperatur", value=0.0)
tds = st.number_input("TDS", value=0.0)
tss = st.number_input("TSS", value=0.0)
ph = st.number_input("pH", value=0.0)
bod = st.number_input("BOD", value=0.0)
cod = st.number_input("COD", value=0.0)
do = st.number_input("DO", value=0.0)
curah_hujan = st.number_input("Curah Hujan", value=0.0)
if st.button("Prediksi"):

    data = pd.DataFrame([[
        temperatur,
        tds,
        tss,
        ph,
        bod,
        cod,
        do,
        curah_hujan
    ]], columns=[
        "Temperatur ",
        "TDS",
        "TSS",
        "pH",
        "BOD",
        "COD",
        "DO",
        "CurahHujan"
    ])

    hasil = model.predict(data)[0]

    st.subheader("Hasil Prediksi")
    st.write("Nilai Prediksi:", hasil)

    if hasil == 5:
        st.success("✅ Sangat Baik")

    elif hasil == 4:
        st.success("✅ Baik")

    elif hasil == 3:
        st.warning("⚠️ Cukup Baik")

    else:
        st.error("❌ Tidak Layak Digunakan")
