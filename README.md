```plain text
Air Quality Prediction using LSTMs


This project predicts Air Quality Index (AQI) using real-time sensor data.
The model is built with LSTM (Long Short-Term Memory) networks and deployed with Streamlit,
so you can easily enter sensor values and get instant predictions!

---

What This Project Does
-----------------------

- Uses machine learning (LSTM) to predict AQI based on past air quality data.
- Takes input from CO Level, Temperature, and Humidity sensors.
- Provides real-time predictions through an interactive web app using Streamlit.

---

Project Structure
------------------

├── app.py                  # Main Streamlit app for the web interface
├── model.py                # LSTM model definition and training code
├── data_preprocessing.py   # Data cleaning, preprocessing, and normalization
└── README.md               # Project documentation
```

---

Setup Instructions
------------------

### Install Dependencies
First, ensure you have Python 3.8+ installed. Then, install the required libraries:

```bash
pip install streamlit tensorflow numpy pandas joblib matplotlib seaborn scikit-learn
```

### Run the Web App
Once everything is installed, launch the AQI Prediction App with:

```bash
streamlit run app.py
```

This will open a web interface where you can input air quality values and get predictions.

---

How It Works
-------------

The app predicts AQI using an LSTM model trained on air quality data. It follows these key steps:

1. **Preprocessing the Data**
   - Cleans sensor readings (CO Level, Temperature, Humidity).
   - Normalizes values using MinMaxScaler.

2. **Building & Training the LSTM Model**
   - Uses 10 time steps to learn trends in air quality.
   - Optimized with the Adam optimizer & Mean Squared Error loss.

3. **Making Predictions**
   - Takes new sensor inputs.
   - Runs them through the trained model.
   - Outputs an estimated AQI value.

---

Using the App
-------------

1. Open the app by running:

   ```bash
   streamlit run app.py
   ```

2. Enter sensor values (CO Level, Temperature, Humidity).
3. Click "Predict AQI" and get an instant forecast.

---

Important Notes
----------------

- The original model was trained on 10 time-step sequences, but this app is adjusted to work with single-point inputs for simplicity.
- Predictions are based on past air quality trends, so real-time accuracy depends on how well the model generalizes.
