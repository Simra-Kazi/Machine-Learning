# 🎬  Movie Recommendation System

## Overview

This project is a **movie recommendation system** that uses **Cosine Similarity** to recommend similar movies based on a given movie title. The system takes a movie name as input and returns a list of similar movies from the dataset. It is implemented using **machine learning** and **data preprocessing** techniques, and deployed as a web application using **Gradio**.

---

## Dataset

The dataset used in this project is the **TMDB Movie Dataset**. Key features include:

* Movie Title
* Vote Average (`vote_average`)
* Genres (`genres`)
* Original Language (`original_language`)
* Adult Content (`adult`)
* Runtime (`runtime`)
* Popularity
* Revenue
* Budget

---

## Technologies Used

* **Python**
* **Pandas, NumPy** (Data preprocessing)
* **Scikit-learn** (Cosine similarity, preprocessing)
* **Matplotlib, Seaborn** (Data visualization)
* **Gradio** (Web app deployment)
* **Jupyter Notebook** (Development and testing)

---

## Model Details

The recommendation system is based on **Cosine Similarity**, which measures the similarity between movies based on their features. After preprocessing the dataset:

* **Genres** are one-hot encoded using **MultiLabelBinarizer**.
* **Adult Content** and **Language** features are one-hot encoded using **OneHotEncoder**.
* The dataset is normalized using **StandardScaler** to improve model performance.

The system computes the cosine similarity between a user-provided movie and all others in the dataset, and returns the most similar movies.

---

## Installation

To run this project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/Simra-Kazi/Machine-Learning/edit/main/Movies%20recommendation%20Project
   cd Movie recommendation Project
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Gradio app:

   ```bash
   python app.py
   ```

---

## Usage

* Open the **Gradio web app**.
* Enter a movie title (e.g., "The Dark Knight") in the **Movie Name** input field.
* Specify the number of recommendations you want (e.g., 5).
* Click **Submit** to get the recommended similar movies based on the dataset.

---

## Results & Performance

* The system returns a list of recommended movies based on their cosine similarity scores.
* Results are sorted and displayed for easy access to top movie recommendations.

---

## Future Improvements

* Add more advanced recommendation techniques like **Collaborative Filtering** or **Content-Based Filtering**.
* Improve recommendation accuracy with **deep learning models** or **hybrid models**.
* Deploy the app to cloud platforms like **Heroku** or **AWS**.

---

## Contributing

Contributions are welcome! 

---

## License

This project is licensed under the **MIT License**.

---


