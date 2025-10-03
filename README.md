# 🎬 Movie Recommendation System (Content-Based)

A content-based movie recommendation system that suggests similar movies based on movie features like genres, cast, crew, keywords, and overview. This system uses machine learning techniques to analyze movie attributes and provide personalized recommendations.

## 📸 Screenshots

### Movie Recommendations

![image](https://github.com/user-attachments/assets/d2278dcb-fa12-4707-a443-7da0def13128)

## 🎯 Overview

This project implements a content-based filtering approach to recommend movies. Unlike collaborative filtering that relies on user behavior, content-based filtering recommends items similar to those a user has liked in the past, based on the item's attributes.

The system analyzes various movie features such as:
- **Genres**: Action, Comedy, Drama, etc.
- **Cast & Crew**: Actors, Directors
- **Keywords**: Plot-related keywords
- **Overview**: Movie description/summary

## ✨ Features

- **Content-Based Recommendations**: Get movie suggestions based on movie attributes
- **Similarity Calculation**: Uses cosine similarity to find similar movies
- **User-Friendly Interface**: Simple and intuitive web interface built with Streamlit
- **Movie Posters**: Displays movie posters fetched from TMDB API
- **Fast Processing**: Efficient vectorization and similarity computation
- **Scalable**: Can handle large movie datasets

## 🛠 Technologies Used

- **Python 3.x**: Core programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Scikit-learn**: Machine learning algorithms (CountVectorizer, Cosine Similarity)
- **NLTK**: Natural Language Processing for text preprocessing
- **Streamlit**: Web application framework
- **Requests**: API calls to fetch movie posters
- **Pickle**: Model serialization

## 📊 Dataset

This project uses the **TMDB 5000 Movie Dataset** which includes:
- `tmdb_5000_movies.csv`: Contains movie details like budget, genres, homepage, id, keywords, original language, overview, popularity, production companies, release date, revenue, runtime, status, tagline, title, vote average, and vote count.
- `tmdb_5000_credits.csv`: Contains movie cast and crew information.

**Dataset Source**: [Kaggle - TMDB 5000 Movie Dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata)

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ombhandwalkar/Movie-recommendation-system-content_based.git
   cd Movie-recommendation-system-content_based
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLTK data** (if required)
   ```python
   import nltk
   nltk.download('stopwords')
   nltk.download('punkt')
   ```

5. **Get TMDB API Key**
   - Sign up at [The Movie Database (TMDB)](https://www.themoviedb.org/)
   - Go to Settings → API → Request an API Key
   - Add your API key to the application

## 💻 Usage

### Running the Jupyter Notebook

1. Open the Jupyter notebook:
   ```bash
   jupyter notebook
   ```

2. Navigate to the notebook file and run all cells to:
   - Load and preprocess the data
   - Create the recommendation model
   - Generate similarity matrices
   - Save the processed data and model

### Running the Streamlit App

1. Start the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. The app will open in your browser at `http://localhost:8501`

3. Select a movie from the dropdown menu

4. Click the "Recommend" button to get similar movie suggestions

## 🔍 How It Works

### 1. Data Preprocessing
- Load movie and credits datasets
- Merge datasets on movie title/id
- Extract relevant features: genres, keywords, cast, crew, overview
- Handle missing values
- Convert JSON-like strings to proper format

### 2. Feature Engineering
- Combine all relevant text features into a single "tags" column
- Clean and preprocess text (lowercase, remove spaces)
- Apply stemming to reduce words to their root form

### 3. Vectorization
- Use `CountVectorizer` or `TfidfVectorizer` to convert text to numerical vectors
- Set maximum features (typically 5000) to limit dimensionality
- Remove common English stop words

### 4. Similarity Calculation
- Compute cosine similarity between all movie vectors
- Create a similarity matrix showing how similar each movie is to every other movie

### 5. Recommendation Generation
- For a given movie, find the most similar movies from the similarity matrix
- Sort by similarity score in descending order
- Return top N recommendations (typically 5-10)

### Mathematical Representation

**Cosine Similarity Formula**:
```
similarity(A, B) = (A · B) / (||A|| × ||B||)
```

Where:
- A and B are feature vectors for two movies
- A · B is the dot product
- ||A|| and ||B|| are the magnitudes of the vectors

## 📁 Project Structure

```
Movie-recommendation-system-content_based/
│
├── app.py                          # Streamlit web application
├── Movie_Recommendation.ipynb      # Jupyter notebook with model development
├── requirements.txt                # Python dependencies
│
├── data/                           # Dataset folder (not included in repo)
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
├── models/                         # Saved models and data
│   ├── movie_list.pkl             # Processed movie list
│   └── similarity.pkl             # Similarity matrix
│
├── images/                         # Screenshots and images
│
└── README.md                       # Project documentation
```

## 📧 Contact

**Om Bhandwalkar**

- GitHub: [@Ombhandwalkar](https://github.com/Ombhandwalkar)
- Project Link: [https://github.com/Ombhandwalkar/Movie-recommendation-system-content_based](https://github.com/Ombhandwalkar/Movie-recommendation-system-content_based)

---

### ⭐ If you found this project helpful, please give it a star!








































