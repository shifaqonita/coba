import pickle
import streamlit as st

# Membaca model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# Judul web
st.title('Data Mining Prediksi Diabetes')

# Deskripsi singkat
st.write("""
Aplikasi ini akan memprediksi kemungkinan seseorang terkena diabetes berdasarkan beberapa parameter medis.
Silakan masukkan data pada kolom di bawah untuk melakukan prediksi.
""")

# Mengatur layout dengan dua kolom
with st.form(key='prediction_form'):
    col1, col2 = st.columns(2)

    with col1:
        Pregnancies = st.number_input('Input nilai Pregnancies', min_value=0, max_value=20, step=1)
        Glucose = st.number_input('Input nilai Glucose', min_value=0, max_value=300, step=1)
        BloodPressure = st.number_input('Input nilai Blood Pressure', min_value=0, max_value=200, step=1)
        Insulin = st.number_input('Input nilai Insulin', min_value=0, max_value=1000, step=1)
        DiabetesPedigreeFunction = st.number_input('Input nilai Diabetes Pedigree Function', min_value=0.0, max_value=3.0, step=0.01)

    with col2:
        SkinThickness = st.number_input('Input nilai Skin Thickness', min_value=0, max_value=100, step=1)
        BMI = st.number_input('Input nilai BMI', min_value=0.0, max_value=70.0, step=0.1)
        Age = st.number_input('Input nilai Age', min_value=0, max_value=120, step=1)

    # Tombol untuk prediksi di luar kolom
    submit_button = st.form_submit_button('Test Prediksi Diabetes')

    if submit_button:
        # Memeriksa jika semua input sudah benar
        inputs = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        
        # Prediksi
        diab_prediction = diabetes_model.predict([inputs])
        
        if diab_prediction[0] == 1:
            diab_diagnosis = 'Pasien terkena Diabetes'
            st.error(diab_diagnosis)
        else:
            diab_diagnosis = 'Pasien tidak terkena Diabetes'
            st.success(diab_diagnosis)
