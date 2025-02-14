# Diabetes Prediction using Machine Learning  

## Overview  
This project is a **machine learning classification model** that predicts whether a person has diabetes based on medical attributes. The model is integrated into a **Streamlit web application** for user-friendly interaction.  

## Dataset  
The dataset used in this project includes various medical features such as:  
- Glucose Level  
- Blood Pressure  
- BMI  
- Insulin Level  
- Age  
- Diabetes Pedigree Function  
- Other relevant factors  

## Technologies Used  
- **Python**  
- **Pandas, NumPy** (Data Preprocessing)  
- **Scikit-Learn** (Machine Learning)  
- **Matplotlib, Seaborn** (Visualization)  
- **Streamlit** (Web App)  

## Model Details  
The classification model is trained using different algorithms, including:  
- Logistic Regression  
- Random Forest Classifier  
- Support Vector Machine (SVM)  
- Decision Tree  
- K-Nearest Neighbors (KNN)  

The best-performing model is selected based on evaluation metrics like **accuracy, precision, recall, and F1-score**.  

## Installation  
To run this project locally, follow these steps:  

1. Clone the repository:  
   ```bash
   git clone https://github.com/Simra-Kazi/Machine-Learning.git
   
2. Install dependencies:
  pip install -r requirements.txt

3. Run the Streamlit app:
   streamlit run app.py
* Usage
  Open the Streamlit web app.
  Enter the required medical details in the input fields.
  Click Predict to get the result.
  The app will display whether the person is predicted to have diabetes or not.
  
* Results & Performance
  The model achieved an accuracy of XX% (based on evaluation).
  Confusion matrix, ROC curve, and other performance metrics are available for analysis.
  
* Future Improvements
  Enhance feature selection for better accuracy.
  Integrate deep learning models.
  Deploy the app on cloud services like Heroku or AWS
  
* Contributing
  Contributions are welcome! Feel free to fork the repository and submit pull requests
  
License
This project is licensed under the MIT License.
