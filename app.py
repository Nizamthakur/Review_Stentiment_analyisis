from flask import Flask, request, jsonify, render_template
import pandas as pd
import pickle

app = Flask(__name__)

# Load model and vectorizer
with open('sentiment_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Home Route (Root URL)
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload_reviews', methods=['POST'])
def upload_reviews():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Process the CSV file
    df = pd.read_csv(file)

    total_reviews = len(df)
    positive_count = 0
    negative_count = 0

    # Update with the correct column name, assuming it's 'review'
    for review in df['review']:  # Replace 'class' with the actual column name
        sentiment = analyze_sentiment(review)
        if sentiment == "Positive":
            positive_count += 1
        else:
            negative_count += 1

    # Calculate percentages
    positive_percentage = (positive_count / total_reviews) * 100 if total_reviews > 0 else 0
    negative_percentage = (negative_count / total_reviews) * 100 if total_reviews > 0 else 0

    # Format percentages to 2 decimal places and add percentage sign
    positive_percentage_formatted = f"{positive_percentage:.2f}%"
    negative_percentage_formatted = f"{negative_percentage:.2f}%"

    # Return as JSON response
    return jsonify({
        'positive_percentage': positive_percentage_formatted,
        'negative_percentage': negative_percentage_formatted
    })


def analyze_sentiment(review):
    # Vectorize the review
    review_vector = vectorizer.transform([review])
    # Predict sentiment
    prediction = model.predict(review_vector)
    return "Positive" if prediction == 1 else "Negative"

if __name__ == '__main__':
    app.run(debug=True)
