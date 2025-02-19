import streamlit as st
import joblib
import numpy as np

# Load the trained ML model (make sure the path to your model is correct)
model = joblib.load("Ecosystem_helth_calculator.pkl")

# Streamlit application
def main():
    st.set_page_config(page_title="Ecosystem Health Prediction", page_icon="🌿", layout="wide")
    st.title("🌿 Ecosystem Health Prediction with ML Model")
    
    st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.sidebar.header("Input Parameters")
    
    # Input fields for user to provide data
    with st.sidebar.expander("Provide the following details:"):
        water_quality = st.number_input("Water Quality (0-100)", min_value=0.0, max_value=100.0, value=50.0)
        aqi = st.number_input("Air Quality Index (AQI)", min_value=0.0, max_value=500.0, value=160.0)
        bdi = st.number_input("Biodiversity Index (0-1)", min_value=0.0, max_value=1.0, value=0.6)
        vegetation_cover = st.number_input("Vegetation Cover (%)", min_value=0.0, max_value=100.0, value=65.0)
        soil_ph = st.number_input("Soil pH", min_value=3.5, max_value=9.0, value=6.0)

    # Button to trigger prediction
    if st.sidebar.button("Predict Ecosystem Health"):
        # Prepare the data for prediction (make sure it matches the format the model expects)
        input_data = np.array([[water_quality, aqi, bdi, vegetation_cover, soil_ph]])
        
        # Make the prediction using the loaded model
        prediction = model.predict(input_data)
        
        # Display the result
        st.markdown("## Prediction Result")
        if prediction == 0:
            st.subheader("🌱 Ecosystem Health: Degraded")
        elif prediction == 1:
            st.subheader("🌳 Ecosystem Health: Healthy")
        else:
            st.subheader("🌾 Ecosystem Health: At risk")

if __name__ == "__main__":
    main()