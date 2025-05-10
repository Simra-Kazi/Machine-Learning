# 🎮 Anime Recommendation System using Collaborative Filtering

## Overview

This project builds an **Anime Recommendation System** that utilizes **Collaborative Filtering** to recommend anime based on user ratings. The system uses user-item interaction data to find patterns and suggest personalized anime titles. It is implemented using **Matrix Factorization** and **Cosine Similarity** for predicting ratings and generating recommendations.

---

## Dataset

The project uses the **Anime Recommendation Database** which includes:

* **Anime ID** and **Anime Title**
* **User ID**
* **User Rating for Anime**
* **Genres and Tags**

---

## Technologies Used

* **Python**
* **Pandas, NumPy** (Data preprocessing and manipulation)
* **Scikit-learn** (Collaborative filtering, similarity metrics)
* **Cosine Similarity** (For measuring similarity between users or items)
* **Matplotlib, Seaborn** (Data visualization)
* **Surprise** (For building collaborative filtering models)

---

## Recommendation Approach

The recommendation system is built using **Collaborative Filtering**, with two main approaches:

* **User-based Collaborative Filtering**: Recommends anime based on the similarity between users’ ratings.
* **Item-based Collaborative Filtering**: Recommends anime based on the similarity between the anime themselves.

The **Cosine Similarity** metric is used to calculate similarity between users or items. Additionally, the system is optimized with **Matrix Factorization** to improve recommendation accuracy.

---

## Installation

To run this project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/Simra-Kazi/Machine-Learning/new/main/Anime%20recommender%20collaborative%20filtering
 

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the recommendation script:

   ```bash
   python recommendation_system.py
   ```

---

## Usage

* Input a **User ID** or **Anime Title**.
* The system will recommend **Top 5 Anime** based on the input.
* Results will be displayed with **anime names** and a brief **description**.

---

## Results & Performance

* The collaborative filtering model provides personalized anime recommendations based on user preferences.
* Evaluation metrics like **Precision** and **Recall** can be used to assess the recommendation quality.
* Visualizations such as **rating distributions**, **top-rated anime**, and **similarity heatmaps** can be accessed for further analysis.

---

## Future Improvements

* Integrate **content-based filtering** for more diverse recommendations.
* Enhance the system with **Deep Learning** models for better accuracy.
* Deploy the app with **Flask** or **Streamlit** for user-friendly interaction.
* Incorporate **real-time user data** for dynamic recommendations.

---

## Contributing

Contributions are welcome! 

---

## License

This project is licensed under the **MIT License**.

---


