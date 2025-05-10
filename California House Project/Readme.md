# 🏡 California Housing Price Prediction using Machine Learning

## Overview

This project is a **machine learning regression model** that predicts the **median house value** in California districts based on demographic and geographic data. The trained model is deployed using a **Streamlit web application** for easy interaction.

---

## Dataset

The dataset includes various features from the **California Housing dataset**, such as:

* Median Income (`MedInc`)
* House Age (`HouseAge`)
* Average Rooms (`AveRooms`)
* Average Bedrooms (`AveBedrms`)
* Population
* Average Occupancy (`AveOccup`)
* Latitude
* Longitude

---

## Technologies Used

* **Python**
* **Pandas, NumPy** (Data preprocessing)
* **Scikit-Learn** (Machine learning)
* **Matplotlib, Seaborn** (Visualization)
* **Streamlit** (Web app deployment)

---

## Model Details

The regression model is trained using multiple algorithms, including:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* XGBoost Regressor
* LightGBM Regressor

The best-performing model is selected based on evaluation metrics like **R² score, MAE, MSE, and RMSE**.

---

## Installation

To run this project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/Simra-Kazi/Machine-Learning/new/main/California%20House%20Project
   cd California House Project
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run California_housing.py
   ```

---

## Usage

* Open the Streamlit web app.
* Enter the required district features in the input fields.
* Click **Predict** to get the result.
* The app will display the **predicted median house value** for the given inputs.

---

## Results & Performance

* The selected model achieved an R² score of **XX** (based on testing).
* Visualizations such as residual plots and feature importance charts are available for evaluation.

---

## Future Improvements

* Add feature scaling and outlier detection for better performance.
* Integrate more advanced models or ensemble methods.
* Deploy the app to platforms like **Heroku**, **Render**, or **AWS**.

---

## Contributing

Contributions are welcome! 

---

## License

This project is licensed under the **MIT License**.

---

