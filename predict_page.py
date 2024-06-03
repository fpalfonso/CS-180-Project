import streamlit as st
import pickle
import pandas as pd


def load_model():
    with open('saved_model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

model_loaded = data["model"]

def show_predict_page():
    st.title("Predictive Maintenance System for Automotive Vehicles")

    st.write("""### We need some information to predict what needs to be maintained""")

    vehicles = (
        "Honda Jazz Petrol",
        "Honda Jazz Diesel",
        "Honda Amaze Petrol",
        "Honda Amaze Diesel",
        "Honda City Petrol",
        "Honda City Diesel",
        "Toyota Fortuner Diesel",
    )

    vehicle = st.selectbox("Vehicle", vehicles)
    mileage = st.number_input("Mileage", min_value = 10000, max_value = 100000)

    ok = st.button("Calculate prediction")
    if ok:
        if vehicle == "Honda Jazz Petrol":
            X = {'mileage_range': [round(mileage, -4)], 'mileage': [mileage], 'is_HondaJazzPetrol': [1], 'is_HondaJazzDiesel': [0],
                'is_HondaAmazePetrol': [0], 'is_HondaAmazeDiesel': [0], 'is_HondaCityPetrol': [0], 'is_HondaCityDiesel': [0],
                'is_ToyotaFortunerDiesel': [0]}
        elif vehicle == "Honda Jazz Diesel":
            X = {'mileage_range': [round(mileage, -4)], 'mileage': [mileage], 'is_HondaJazzPetrol': [0], 'is_HondaJazzDiesel': [1],
                'is_HondaAmazePetrol': [0], 'is_HondaAmazeDiesel': [0], 'is_HondaCityPetrol': [0], 'is_HondaCityDiesel': [0],
                'is_ToyotaFortunerDiesel': [0]}
        elif vehicle == "Honda Amaze Petrol":
            X = {'mileage_range': [round(mileage, -4)], 'mileage': [mileage], 'is_HondaJazzPetrol': [0], 'is_HondaJazzDiesel': [0],
                'is_HondaAmazePetrol': [1], 'is_HondaAmazeDiesel': [0], 'is_HondaCityPetrol': [0], 'is_HondaCityDiesel': [0],
                'is_ToyotaFortunerDiesel': [0]}
        elif vehicle == "Honda Amaze Diesel":
            X = {'mileage_range': [round(mileage, -4)], 'mileage': [mileage], 'is_HondaJazzPetrol': [0], 'is_HondaJazzDiesel': [0],
                'is_HondaAmazePetrol': [0], 'is_HondaAmazeDiesel': [1], 'is_HondaCityPetrol': [0], 'is_HondaCityDiesel': [0],
                'is_ToyotaFortunerDiesel': [0]}
        elif vehicle == "Honda City Petrol":
            X = {'mileage_range': [round(mileage, -4)], 'mileage': [mileage], 'is_HondaJazzPetrol': [0], 'is_HondaJazzDiesel': [0],
                'is_HondaAmazePetrol': [0], 'is_HondaAmazeDiesel': [0], 'is_HondaCityPetrol': [1], 'is_HondaCityDiesel': [0],
                'is_ToyotaFortunerDiesel': [0]}
        elif vehicle == "Honda City Diesel":
            X = {'mileage_range': [round(mileage, -4)], 'mileage': [mileage], 'is_HondaJazzPetrol': [0], 'is_HondaJazzDiesel': [0],
                'is_HondaAmazePetrol': [0], 'is_HondaAmazeDiesel': [0], 'is_HondaCityPetrol': [0], 'is_HondaCityDiesel': [1],
                'is_ToyotaFortunerDiesel': [0]}
        elif vehicle == "Toyota Fortuner Diesel":
            X = {'mileage_range': [round(mileage, -4)], 'mileage': [mileage], 'is_HondaJazzPetrol': [0], 'is_HondaJazzDiesel': [0],
                'is_HondaAmazePetrol': [0], 'is_HondaAmazeDiesel': [0], 'is_HondaCityPetrol': [0], 'is_HondaCityDiesel': [0],
                'is_ToyotaFortunerDiesel': [1]}
        
        input = pd.DataFrame(data=X)
        prediction = model_loaded.predict(input)
        st.subheader(f"Need maintenance for these: ")
        
        if prediction[0][0]:
            st.subheader("Oil filter")
        if prediction[0][1]:
            st.subheader("Engine oil")
        if prediction[0][2]:
            st.subheader("Washer plug drain")
        if prediction[0][3]:
            st.subheader("Dust and pollen filter")
        if prediction[0][4]:
            st.subheader("Wheel alignment and balancing")
        if prediction[0][5]:
            st.subheader("Air clean filter")
        if prediction[0][6]:
            st.subheader("Fuel filter")
        if prediction[0][7]:
            st.subheader("Spark plug")
        if prediction[0][8]:
            st.subheader("Break fluid")
        if prediction[0][9]:
            st.subheader("Break and clutch oil")
        if prediction[0][10]:
            st.subheader("Transmission fluid")
        if prediction[0][11]:
            st.subheader("Break pads")
        if prediction[0][12]:
            st.subheader("Clutch")
        if prediction[0][13]:
            st.subheader("Coolant")