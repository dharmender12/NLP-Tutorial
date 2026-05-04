import streamlit as st
from pickle import load

# Load the label encoder and tfidf vectorizer
label_encoder = load(open('label_encoder.pkl', 'rb'))
tfidf_vectorizer = load(open('tfidf_vectorizer.pkl', 'rb'))

# Load the trained models
logistic_regression_model = load(open('logistic_regression_model.pkl', 'rb'))
decision_tree_model = load(open('decision_tree_model.pkl', 'rb'))


def predict_sentiment(text, model):
    # Transform the input text using the tfidf vectorizer
    text_vectorized = tfidf_vectorizer.transform([text])
    
    # Predict the sentiment using the selected model
    if model == 'Logistic Regression':
        prediction = logistic_regression_model.predict(text_vectorized)
    else:
        prediction = decision_tree_model.predict(text_vectorized)
    
    # Decode the predicted label
    sentiment = label_encoder.inverse_transform(prediction)[0]
    
    return sentiment


def main():
    st.title("Sentiment Analysis App")
    
    # Input text from the user
    user_input = st.text_area("Enter text to analyze sentiment:")
    
    # Model selection
    model_option = st.selectbox("Select Model", ("Logistic Regression", "Decision Tree"))
    
    if st.button("Predict Sentiment"):
        if user_input:
            sentiment = predict_sentiment(user_input, model_option)
            st.write(f"Predicted Sentiment: {sentiment}")
        else:
            st.write("Please enter some text to analyze.")
    
if __name__ == "__main__":
    main()