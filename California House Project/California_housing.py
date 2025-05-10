import streamlit as st
import pickle
import numpy as np

def infer_california_housing(model_path, input_features):
    """
    Perform inferencing on the California housing regression model.

    Parameters:
    - model_path (str): Path to the saved regression model pickle file.
    - input_features (list): List of input features (same order as used for training):
      [MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude]

    Returns:
    - float: Predicted median house value.
    """
    try:
        # Load the trained regression model
        with open(model_path, 'rb') as file:
            model = pickle.load(file)

        # Ensure the input features are in the correct format
        input_array = np.array([input_features]).reshape(1, -1)

        # Predict median house value
        prediction = model.predict(input_array)[0]

        return prediction

    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit App
st.title("California Housing Price Prediction")
st.write("Provide the details below to predict the median house value:")

# Input fields
med_inc = st.number_input("Median Income (MedInc)", min_value=0.0, step=0.1)
house_age = st.number_input("House Age (HouseAge)", min_value=0, step=1)
ave_rooms = st.number_input("Average Number of Rooms (AveRooms)", min_value=0.0, step=0.1)
ave_bedrms = st.number_input("Average Number of Bedrooms (AveBedrms)", min_value=0.0, step=0.1)
population = st.number_input("Population", min_value=0, step=1)
ave_occup = st.number_input("Average Occupancy (AveOccup)", min_value=0.0, step=0.1)
latitude = st.number_input("Latitude", min_value=-90.0, max_value=90.0, step=0.1)
longitude = st.number_input("Longitude", min_value=-180.0, max_value=180.0, step=0.1)

# Path to the model
model_path = 'californiaHousing_model.pkl'

# Predict button
if st.button("Predict"):
    # Create a list of input features
    input_features = [med_inc, house_age, ave_rooms, ave_bedrms, population, ave_occup, latitude, longitude]

    # Perform inference
    result = infer_california_housing(model_path, input_features)

    # Display the prediction
    if isinstance(result, float):
        st.success(f"Predicted Median House Value: ${result:.2f}")
    else:
        st.error(result)
