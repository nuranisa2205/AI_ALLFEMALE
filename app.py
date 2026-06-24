import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model_kualitas_air.pkl")

st.set_page_config(
    page_title="Prediksi Kualitas Air",
    page_icon="💧"
)

st.title("💧 Prediksi Kualitas Air")

st.write("Masukkan parameter kualitas air untuk mengetahui apakah air aman digunakan.")

temperatur = st.number_input("Temperatur", value=28.0)
tds = st.number_input("TDS", value=300.0)
tss = st.number_input("TSS", value=50.0)
ph = st.number_input("pH", value=7.0)
bod = st.number_input("BOD", value=10.0)
cod = st.number_input("COD", value=25.0)
do = st.number_input("DO", value=4.0)
curah_hujan = st.number_input("Curah Hujan", value=5.0)

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

    if hasil >= 4:
        st.success("✅ Air Aman Digunakan")
    else:
        st.error("⚠️ Air Tidak Aman Digunakan")
