import streamlit as st
import numpy as np
import joblib
from tensorflow.keras.models import load_model

# Load trained model and scaler
model = load_model("air_quality_model.h5")
scaler = joblib.load("scaler.pkl")

st.title("Air Quality Index Prediction")
st.write("Enter sensor data to predict AQI.")

# User input fields
co_level = st.number_input("CO Level", value=0.0, format="%.2f")
temperature = st.number_input("Temperature (°C)", value=25.0, format="%.2f")
humidity = st.number_input("Humidity (%)", value=50.0, format="%.2f")

if st.button("Predict AQI"):
    # Create a single input array
    new_input = np.array([[co_level, temperature, humidity]])

    # Scale input data
    new_input_scaled = scaler.transform(new_input)

    # Reshape to match LSTM expected input: (batch_size=1, time_steps=1, features=3)
    reshaped_input = new_input_scaled.reshape(1, 1, 3)  # (1, 1, 3) instead of (1, 10, 3)

    # Predict AQI
    prediction = model.predict(reshaped_input)[0][0]
    st.success(f"Predicted AQI: {prediction:.2f}")
















