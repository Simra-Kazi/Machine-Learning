import streamlit as st
import pickle
import pandas as pd

# Load the trained model and scaler from pickle files
def load_model_and_scaler(model_filename='iris_model.pkl', scaler_filename='iris_scaler.pkl'):
    """Loads the trained model and scaler from pickle files."""
    with open(r'C:\Users\IICET 20\Desktop\Simra kazi\Machine Learning\Iris Project\log_reg_model.pickle', 'rb') as model_file:
        model = pickle.load(model_file)
    
    with open(r'C:\Users\IICET 20\Desktop\Simra kazi\Machine Learning\Iris Project\scaler.pkl', 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
    
    return model, scaler

# Function to preprocess the input data (features for sepal length, width, petal length, and petal width)
def preprocess_input(input_data, scaler):
    """Preprocess the input data: scale it using the loaded scaler."""
    input_df = pd.DataFrame([input_data])
    input_scaled = scaler.transform(input_df)
    return input_scaled

# Predict the Iris species using the trained model
def predict_iris_species(input_data):
    """Predicts the species of the Iris flower (Setosa, Versicolor, or Virginica)."""
    # Load the model and scaler
    model, scaler = load_model_and_scaler()
    
    # Preprocess the input data (scale it)
    input_scaled = preprocess_input(input_data, scaler)
    
    # Make the prediction using the trained model
    prediction = model.predict(input_scaled)
    
    # Map the prediction to the Iris species names
    species_map = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
    predicted_species = species_map[prediction[0]]
    
    return predicted_species

# Streamlit frontend
def main():
    st.title("Iris Species Prediction")
    
    # Input fields for the features
    sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, value=5.1)
    sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, value=3.5)
    petal_length = st.number_input("Petal Length (cm)", min_value=0.0, value=1.4)
    petal_width = st.number_input("Petal Width (cm)", min_value=0.0, value=0.2)

    # Button to predict
    if st.button("Predict"):
        # Prepare the input data
        input_data = {
            'sepal length (cm)': sepal_length,
            'sepal width (cm)': sepal_width,
            'petal length (cm)': petal_length,
            'petal width (cm)': petal_width
        }

        # Get the prediction result
        result = predict_iris_species(input_data)

        # Display the prediction result
        st.write(f"The predicted species is: {result}")

# Run the Streamlit app
if __name__ == "__main__":
    main()
