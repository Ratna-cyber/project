import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Solar-Power-Generation App")
st.write("Enter the environmental parameters:")

# REALISTIC DEFAULT VALUES
distance_to_solar_noon = st.number_input("distance-to-solar-noon", value=0.8)
temperature = st.number_input("temperature", value=32.0)
wind_direction = st.number_input("wind-direction", value=180.0)
wind_speed = st.number_input("wind-speed", value=3.5)
sky_cover = st.number_input("sky-cover", value=20.0)
visibility = st.number_input("visibility", value=10.0)
humidity = st.number_input("humidity", value=55.0)
avg_wind_speed = st.number_input("average-wind-speed-(period)", value=4.0)
avg_pressure = st.number_input("average-pressure-(period)", value=1010.0)

# Create DF with EXACT SAME column names used during training
df = pd.DataFrame([{
    "distance-to-solar-noon": distance_to_solar_noon,
    "temperature": temperature,
    "wind-direction": wind_direction,
    "wind-speed": wind_speed,
    "sky-cover": sky_cover,
    "visibility": visibility,
    "humidity": humidity,
    "average-wind-speed-(period)": avg_wind_speed,
    "average-pressure-(period)": avg_pressure
}])

if st.button("Predict"):
    pred = model.predict(df)[0]
    st.success(f"Predicted Power Generated: {pred:.2f} Joules")
