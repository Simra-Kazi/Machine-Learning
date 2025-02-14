# Titanic Survival Prediction using Machine Learning  

## Overview  
This project is a **machine learning classification model** that predicts whether a passenger on the Titanic survived or not based on various attributes. The model is integrated into a **Streamlit web application** for user-friendly interaction.  

## Dataset  
The dataset used in this project includes the following features:  
- **Passenger Class (Pclass)** – Ticket class (1st, 2nd, or 3rd)  
- **Name** – Passenger's name  
- **Sex** – Gender of the passenger  
- **Age** – Passenger's age  
- **SibSp** – Number of siblings/spouses aboard the Titanic  
- **Parch** – Number of parents/children aboard the Titanic  
- **Ticket** – Ticket number  
- **Fare** – Passenger fare  
- **Cabin** – Cabin number  
- **Embarked** – Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)  
- **Survived (Target Variable)** – 1 = Survived, 0 = Did not survive  

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
   git clone git clone https://github.com/Simra-Kazi/Machine-Learning.git

2. Install dependencies:
  pip install -r requirements.txt
3. Run the Streamlit app:
   streamlit run app.py
## Usage
Open the Streamlit web app.
Enter passenger details (age, gender, class, fare, etc.).
Click Predict to get the result.
The app will display whether the passenger is predicted to survive or not.
## Results & Performance
The model achieved an accuracy of XX% (based on evaluation).
Confusion matrix, classification report, and visualization plots are available for analysis.
## Future Improvements
Improve feature engineering and data preprocessing.
Deploy the app on cloud platforms like Heroku or AWS.
Add more interactive visualizations.
## Contributors
Contributions are welcome! Feel free to fork the repository and submit pull requests
## License
This project is licensed under the MIT License.
