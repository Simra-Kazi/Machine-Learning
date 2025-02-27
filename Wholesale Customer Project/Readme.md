# Wholesale Customer Segmentation

## Project Overview
The **Wholesale Customer Segmentation** project uses machine learning techniques to segment wholesale customers based on their purchasing behaviors. The goal is to help businesses identify different customer groups and tailor marketing strategies accordingly.

## Dataset
The dataset used for this project includes information about wholesale customers, with features such as:
- **Fresh** (Annual spending on fresh products)
- **Milk** (Annual spending on milk products)
- **Grocery** (Annual spending on grocery items)
- **Frozen** (Annual spending on frozen products)
- **Detergents_Paper** (Annual spending on detergents and paper)
- **Delicassen** (Annual spending on delicatessen items)
- **Channel** (Hotel/Restaurant/Café or Retail)
- **Region** (Lisbon, Oporto, or Other)

## Technologies Used
- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn
- **Machine Learning Models:** K-Means Clustering, Hierarchical Clustering, DBSCAN
- **Framework:** Streamlit (if deployed as a web app)

## Data Preprocessing
1. Handling missing values
2. Encoding categorical variables (e.g., region, channel)
3. Feature scaling (Standardization)
4. Exploratory data analysis (EDA) for insights

## Model Training
Various clustering techniques were used to segment customers:
- **K-Means Clustering**: Optimal clusters determined using the Elbow Method
- **Hierarchical Clustering**: Dendrogram analysis for customer segmentation
- **DBSCAN**: Used for detecting outliers and density-based clustering

## Results
- The model successfully segmented customers into **X clusters**.
- Feature importance analysis revealed that **Grocery and Fresh spending** played a significant role in customer segmentation.
- Visualization tools like **pair plots and heatmaps** were used for analysis.

## Deployment (Optional)
The model can be deployed using **Streamlit** to provide an interactive interface where users can input customer details and view their segment classification.

## How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/Simra-Kazi/Machine-Learning/tree/main/Wholesale%20Customer%20Project
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the clustering script:
   ```bash
   python main.py
   ```
4. If using Streamlit, run:
   ```bash
   streamlit run app.py
   ```

## Future Enhancements
- Improve clustering accuracy with additional data features
- Use advanced techniques like Gaussian Mixture Models (GMM)
- Deploy as a web or mobile application

## Contributors
Contributions are welcome! Feel free to fork the repository and submit pull requests

## License
This project is licensed under the MIT License.


