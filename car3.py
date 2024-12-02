import streamlit as st
import pandas as pd
import joblib

# Streamlit ilovasi nomi
st.title("Mashina narxini bashorat qilish")

# Modelni yuklash
model = joblib.load('car_price_predictor.pkl')

# Foydalanuvchidan kiritish ma'lumotlarini olish
st.header("Mashina ma'lumotlarini kiriting")
mashina_nomi = st.selectbox(
    "Mashina nomi",
    ['Polo', 'Gentra', 'Spark', 'Sportage', 'Sonata', 'K5', 'Lacetti',
     'Nexia', 'Tiguan', 'Camry', 'Corolla', 'Tucson', 'Cobalt', 'Rio',
     'Elantra']
)
year = st.slider("Mashina chiqarilgan yili", min_value=2000, max_value=2024, value=2022, step=1)
mileage = st.number_input("Yurgan masofasi (km)", min_value=0, max_value=300000, value=50000, step=1000)
condition = st.selectbox("Holati", ["New", "Like New", "Used", "Damaged"])
region = st.selectbox("Hududi", ['Tashkent', 'Khiva', 'Namangan', 'Samarkand', 'Andijan', 'Fergana', 'Bukhara'])

# Bashorat qilish tugmasi
if st.button("Narxni aniqlash"):
    # Kiritilgan ma'lumotlar DataFrame'ga o‘tkaziladi
    input_data = pd.DataFrame({
        "CarName": [mashina_nomi],
        "Year": [year],
        "Mileage": [mileage],
        "Condition": [condition],
        "Region": [region]
    })

    try:
        # Model yordamida bashorat qilish
        predicted_price = model.predict(input_data)
        st.success(f"Mashinaning taxminiy narxi: {predicted_price[0]:,.2f} $")
    except Exception as e:
        st.error(f"Error making prediction: {str(e)}")
