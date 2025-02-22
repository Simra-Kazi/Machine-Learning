import streamlit as st
import pickle
import numpy as np

# Function for model inference
def infer_wholesale_cluster(model_path, scaler_path, input_features):
    """
    Perform inferencing on the wholesale customer dataset using a classification model.

    Parameters:
    - model_path (str): Path to the saved classification model pickle file.
    - scaler_path (str): Path to the saved scaler pickle file.
    - input_features (list): List of input features in the order:
      [Channel, Region, Fresh, Milk, Grocery, Frozen, Detergents_Paper, Delicassen]

    Returns:
    - int: Predicted cluster category.
    """
    try:
        # Load the trained classification model
        with open(r'C:\Users\IICET 20\Desktop\Simra kazi\Machine Learning\Clustering\Wholesale Customer Project\wholesale_model.pkl', 'rb') as model_file:
            model = pickle.load(model_file)

        # Load the scaler
        with open(r'C:\Users\IICET 20\Desktop\Simra kazi\Machine Learning\Clustering\Wholesale Customer Project\scaler.pkl', 'rb') as scaler_file:
            scaler = pickle.load(scaler_file)

        # Ensure the input features are in the correct format
        input_array = np.array([input_features]).reshape(1, -1)

        # Scale the input features
        scaled_input = scaler.transform(input_array)

        # Predict the cluster category
        prediction = model.predict(scaled_input)[0]

        return f"Predicted Cluster: {prediction}"

    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit UI
st.title("Wholesale Customer Classification App")

st.sidebar.header("Input Features")

# User input fields
channel = st.sidebar.number_input("Channel", min_value=1, max_value=2, step=1)
region = st.sidebar.number_input("Region", min_value=1, max_value=3, step=1)
fresh = st.sidebar.number_input("Fresh", min_value=0, step=1)
milk = st.sidebar.number_input("Milk", min_value=0, step=1)
grocery = st.sidebar.number_input("Grocery", min_value=0, step=1)
frozen = st.sidebar.number_input("Frozen", min_value=0, step=1)
detergents_paper = st.sidebar.number_input("Detergents_Paper", min_value=0, step=1)
delicassen = st.sidebar.number_input("Delicassen", min_value=0, step=1)

# Model and scaler paths
model_path = "wholesale_model.pkl"
scaler_path = "scaler.pkl"

# Predict button
if st.button("Predict Cluster"):
    input_features = [channel, region, fresh, milk, grocery, frozen, detergents_paper, delicassen]
    result = infer_wholesale_cluster(model_path, scaler_path, input_features)
    st.write(f"### {result}")
