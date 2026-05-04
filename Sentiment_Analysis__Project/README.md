# Sentiment Analysis Application

A comprehensive sentiment analysis tool built to analyze Amazon product reviews across different countries. This application processes text data, extracts features using TF-IDF, encodes reviews, and provides sentiment classification with interactive visualizations.

## 📋 Project Overview

The Sentiment Analysis Application is designed to:
- Load and process Amazon product review data
- Perform text preprocessing and normalization
- Extract text features using TF-IDF vectorization
- Encode categorical variables (country, ratings)
- Analyze sentiment patterns by country and rating
- Generate visualizations and insights from review data

**Dataset**: Amazon Reviews containing reviews across multiple countries with ratings, review counts, and dates.

## 🎯 Features

- **Data Loading & Preprocessing**: Robust CSV parsing with error handling
- **Text Feature Engineering**: TF-IDF transformation for text analysis
- **Categorical Encoding**: One-Hot and Label Encoding for country and rating data
- **Sentiment Analysis**: Classification of reviews based on ratings
- **Data Visualization**: Multiple visualization types for insights
- **Statistical Analysis**: Country-wise and rating-wise sentiment distribution
- **Model Persistence**: Saved encoders and transformers for reuse

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Local Setup

1. Clone or download the project:
```bash
cd text_analytics
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

### Required Packages
```
pandas>=1.3.0
numpy>=1.21.0
scikit-learn>=1.0.0
matplotlib>=3.4.0
seaborn>=0.11.0
streamlit>=1.20.0
plotly>=5.0.0
```

## 🚀 Deployment on Streamlit

### Option 1: Local Streamlit Server

1. Ensure you're in the project directory and virtual environment is activated
2. Run the Streamlit app:
```bash
streamlit run app.py
```

3. The application will open in your default browser at `http://localhost:8501`

### Option 2: Deploy on Streamlit Cloud

#### Setup Steps:

1. **Prepare GitHub Repository**:
   - Push your project to GitHub
   - Ensure `requirements.txt` includes all dependencies
   - Include the `Amazon_Reviews.csv` data file or configure cloud storage

2. **Create Streamlit Account**:
   - Go to [Streamlit Cloud](https://streamlit.io/cloud)
   - Sign up with GitHub account

3. **Deploy Application**:
   - Click "New app"
   - Select your repository, branch, and main file (`app.py`)
   - Click "Deploy"

4. **Environment Variables** (if needed):
   - Set in Streamlit Cloud settings
   - Use `streamlit secrets` for sensitive data

#### Example `app.py` Structure:
```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

st.set_page_config(page_title="Sentiment Analysis", layout="wide")

st.title("🎯 Amazon Review Sentiment Analysis")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv('Amazon_Reviews.csv', encoding='utf-8', 
                       encoding_errors='replace', on_bad_lines='skip')

df = load_data()

# Display data
st.subheader("Dataset Overview")
st.dataframe(df.head())

# Sidebar filters
st.sidebar.header("Filters")
selected_country = st.sidebar.multiselect("Select Country", df['Country'].unique())

if selected_country:
    filtered_df = df[df['Country'].isin(selected_country)]
    st.subheader(f"Reviews from {', '.join(selected_country)}")
    st.dataframe(filtered_df)
    
    # Visualizations
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Rating Distribution")
        rating_counts = filtered_df['Rating'].value_counts()
        st.bar_chart(rating_counts)
    
    with col2:
        st.subheader("Average Review Count")
        avg_reviews = filtered_df.groupby('Country')['Review Count'].mean()
        st.line_chart(avg_reviews)

# Display statistics
st.sidebar.markdown("---")
st.sidebar.write(f"Total Reviews: {len(df)}")
st.sidebar.write(f"Countries: {df['Country'].nunique()}")
st.sidebar.write(f"Date Range: {df['Review Date'].min()} to {df['Review Date'].max()}")
```

### Option 3: Deploy on Other Platforms

#### AWS EC2
```bash
# Install Streamlit on EC2 instance
pip install streamlit
streamlit run app.py --server.port 80 --server.address 0.0.0.0
```

#### Heroku
```bash
# Create Procfile
echo "web: streamlit run app.py" > Procfile

# Deploy
heroku create your-app-name
git push heroku main
```

#### Docker Deployment
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

```bash
docker build -t sentiment-app .
docker run -p 8501:8501 sentiment-app
```

## 📊 Project Structure

```
text_analytics/
├── sentiment_analysis.ipynb      # Main analysis notebook
├── Amazon_Reviews.csv            # Dataset
├── app.py                        # Streamlit application
├── requirements.txt              # Python dependencies
├── README.md                     # This file
├── WIREFRAME.md                  # UI/UX Wireframe
├── label_encoder.pkl            # Saved label encoder
├── tfidf_vectorizer.pkl         # Saved TF-IDF vectorizer
└── data/
    ├── text_preprocessing.csv   # Preprocessed text data
    ├── bow_tfid.csv            # Bag-of-words TF-IDF data
    ├── ner.csv                 # Named Entity Recognition data
    └── n-grams.csv             # N-grams analysis data
```

## 🔧 Configuration

### Streamlit Configuration (`~/.streamlit/config.toml`):
```toml
[theme]
primaryColor = "#FF6B6B"
backgroundColor = "#F5F5F5"
secondaryBackgroundColor = "#E0E0E0"
textColor = "#262730"
font = "sans serif"

[server]
port = 8501
headless = true
runOnSave = true
```

## 📖 Usage

### Running the Jupyter Notebook
```bash
jupyter notebook sentiment_analysis.ipynb
```

### Using the Streamlit App
1. Select filters from the sidebar
2. Choose countries to analyze
3. View real-time visualizations
4. Download filtered data as needed

### Data Format
The application expects a CSV file with the following columns:
- `Country`: Country of the reviewer
- `Review Count`: Number of reviews by user
- `Rating`: Product rating (1-5)
- `Review Text`: The actual review text
- `Review Date`: Date of the review

## 🔬 Analysis Features

### Data Preprocessing
- Handling missing values
- Text cleaning and normalization
- Removal of special characters

### Feature Engineering
- TF-IDF vectorization
- Categorical encoding (One-Hot and Label)
- N-gram extraction

### Encoding Methods
- **Label Encoding**: For ordinal data (ratings)
- **One-Hot Encoding**: For categorical data (countries)

## 📈 Visualizations Included

- Rating distribution by country
- Review count trends over time
- Sentiment distribution pie charts
- Country-wise comparison bar charts
- Word frequency heatmaps
- Review date timeline analysis

## 🛠️ Development

### Running Tests
```bash
pytest tests/
```

### Code Quality
```bash
pylint sentiment_analysis.py
black sentiment_analysis.py
```

## 🐛 Troubleshooting

### Common Issues

**Issue**: Data encoding errors
```bash
# Solution: Ensure encoding='utf-8' with error handling
df = pd.read_csv('file.csv', encoding='utf-8', encoding_errors='replace')
```

**Issue**: Streamlit port already in use
```bash
streamlit run app.py --server.port 8502
```

**Issue**: Missing pickle files
```bash
# Regenerate encoders and save them
import pickle
pickle.dump(label_encoder, open('label_encoder.pkl', 'wb'))
```

## 📝 License

This project is created for educational purposes as part of the Text Analytics course (CSI324).

## 👨‍💻 Author

Created by: Dharmender (LPU, January 2026)

## 📚 References

- Pandas Documentation: https://pandas.pydata.org/
- Scikit-learn Documentation: https://scikit-learn.org/
- Streamlit Documentation: https://docs.streamlit.io/
- TF-IDF and NLP: https://en.wikipedia.org/wiki/Tf%E2%80%93idf

## 🤝 Support

For issues or questions:
1. Check the Jupyter notebook for detailed explanations
2. Review course materials in `CSI324_*.pdf`
3. Check the troubleshooting section above

---

**Last Updated**: January 2026  
**Version**: 1.0.0  
**Status**: Active Development
