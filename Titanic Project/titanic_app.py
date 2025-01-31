import streamlit as st
import pickle
import numpy as np

def infer_titanic_survival(model_path, scaler_path, input_features):
    """
    Perform inferencing on the Titanic dataset.

    Parameters:
    - model_path (str): Path to the saved model pickle file.
    - scaler_path (str): Path to the saved scaler pickle file.
    - input_features (list): List of input features in the order:
      [PassengerId, Pclass, Sex, Age, SibSp, Parch, Fare, Embarked]

    Returns:
    - str: "Survived" or "Not Survived" based on model prediction.
    """
    try:
        # Load the trained model and scaler
        with open(r'C:\Users\IICET 20\Desktop\Simra kazi\Machine Learning\Titanic Project\model.pickle', 'rb') as model_file:
            model = pickle.load(model_file)

        with open(r'C:\Users\IICET 20\Desktop\Simra kazi\Machine Learning\Titanic Project\scaler.pkl', 'rb') as scaler_file:
            scaler = pickle.load(scaler_file)

        # Ensure the input features are in the correct format
        input_array = np.array([input_features]).reshape(1, -1)

        # Scale the input features
        scaled_input = scaler.transform(input_array)

        # Predict survival
        prediction = model.predict(scaled_input)

        # Return result
        return "Survived" if prediction[0] == 1 else "Not Survived"

    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit App
st.title("Titanic Survival Prediction App")

# Sidebar inputs
st.sidebar.header("Input Features")
passenger_id = st.sidebar.number_input("Passenger ID", min_value=1, step=1)
pclass = st.sidebar.selectbox("Passenger Class (Pclass)", options=[1, 2, 3], format_func=lambda x: f"Class {x}")
sex = st.sidebar.selectbox("Sex", options=[0, 1], format_func=lambda x: "Male" if x == 1 else "Female")
age = st.sidebar.number_input("Age", min_value=0.0, step=0.1)
sibsp = st.sidebar.number_input("Number of Siblings/Spouses Aboard (SibSp)", min_value=0, step=1)
parch = st.sidebar.number_input("Number of Parents/Children Aboard (Parch)", min_value=0, step=1)
fare = st.sidebar.number_input("Fare", min_value=0.0, step=0.01)
embarked = st.sidebar.selectbox("Port of Embarkation", options=[0, 1, 2], format_func=lambda x: ["C", "Q", "S"][x])

# Model and scaler paths
model_path = r'C:\Users\IICET 20\Desktop\Simra kazi\Machine Learning\model.pickle'
scaler_path = r'C:\Users\IICET 20\Desktop\Simra kazi\Machine Learning\scaler.pkl'

# Predict button
if st.button("Predict Survival"):
    input_features = [passenger_id, pclass, sex, age, sibsp, parch, fare, embarked]
    result = infer_titanic_survival(model_path, scaler_path, input_features)
    st.write(f"Prediction: **{result}**")
