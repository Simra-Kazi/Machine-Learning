# Pune House Price Prediction

## Project Overview
The **Pune House Price Prediction** project utilizes machine learning to predict the prices of houses based on various factors such as location, area, number of bedrooms, amenities, and more. The goal is to provide an accurate and efficient model that helps buyers and real estate agents make informed decisions.

## Dataset
The dataset used for this project consists of real estate listings from Pune, India. It includes features such as:
** availability **
** size **        
** society **      
** total_sqft **   
** bath **           
** balcony **     
** price  **       
** site_location ** 

## Technologies Used
- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn
- **Machine Learning Models:** Linear Regression, Decision Tree, Random Forest, Gradient Boosting
- **Framework:** Streamlit (if deployed as a web app)

## Data Preprocessing
1. Handling missing values
2. Encoding categorical variables (e.g., location)
3. Feature scaling (Normalization/Standardization)
4. Removing outliers
5. Splitting data into training and testing sets

## Model Training
Multiple machine learning models were trained and evaluated. The best-performing model was selected based on performance metrics such as:
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R-squared score (R²)

## Results
- The model achieved an R² score of **X.XX** on the test dataset.
- Feature importance analysis showed that **location and area size** are the most influential factors.

## Deployment (Optional)
The model can be deployed using **Streamlit** to provide an interactive interface where users can input house features and get price predictions.

## How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/Simra-Kazi/Machine-Learning/tree/main/PUNE%20HOUSE%20PROJECT
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the model script:
   ```bash
   python main.py
   ```
4. If using Streamlit, run:
   ```bash
   streamlit run app.py
   ```

## Future Enhancements
- Improve accuracy using advanced models like XGBoost
- Use real-time data for better predictions
- Deploy as a web or mobile application

## Contributors
- Contributions are welcome! Feel free to fork the repository and submit pull requests

## License
This project is licensed under the MIT License.


