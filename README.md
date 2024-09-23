# Review_Stentiment_analyisis
Sentiment Analysis Web App This project is a Flask-based web application that performs sentiment analysis on customer reviews. The app allows users to upload a .csv file containing reviews, analyzes the sentiments (positive/negative), and visualizes the results using a pie chart. It uses a machine learning model for sentiment classification.
Features
Upload Reviews: Users can upload .csv files containing customer reviews.
Sentiment Analysis: The app processes the uploaded reviews and classifies them as either positive or negative.
Percentage Calculation: The app calculates the percentage of positive and negative reviews.
Visualization: Results are visualized with a pie chart displaying the sentiment distribution.
# Technologies Used
Backend: Flask (Python)
Frontend: HTML, JavaScript, CSS
Machine Learning: Sklearn, Pandas, Nltk 
Data Visualization: Chart.js
Deployment: Localhost (Flask) – Can be deployed to any cloud service (e.g., Heroku, AWS)
Getting Started
# Prerequisites
Python 3.x
Flask
Required Python libraries (Install via requirements.txt)
Installing
Clone the repository:

# Clone Project
git clone https://github.com/nizamthakur/sentiment-analysis-webapp.git
cd sentiment-analysis-webapp
Install the required Python packages:

# Install the requirements 
pip install -r requirements.txt
Run the Flask application:

# Run project 
python app.py
Open your browser and go to http://127.0.0.1:5000/ to access the app.

# Project Structure

.
├── static
│   ├── css
│   └── js
├── templates
│   └── index.html
├── app.py
├── sentiment_model.py
├── README.md
└── requirements.txt

app.py: The main Flask application script.
sentiment_model.py: Contains the sentiment analysis logic and machine learning model.
static/: Contains static assets like CSS and JavaScript files.
templates/: HTML templates for rendering the frontend.
Usage
On the home page, upload a CSV file containing reviews.
After the file is uploaded, the app processes the reviews and classifies them as positive or negative.
The results, including the percentage of positive and negative reviews, are displayed in both text format and a pie chart.
Example CSV Format
The CSV file should contain at least one column named review where each row is a review text.

Example:

review
"The service was excellent!"
"I did not enjoy the food."
"Great atmosphere and friendly staff."

# Future Enhancements :

Add support for neutral sentiment classification.
Improve the UI with better animations and design.
Enable export of analysis results to PDF/CSV.
Integrate with social media platforms to analyze real-time reviews.
# License
This project is licensed under the MIT License.

# Contributing
Feel free to submit issues or pull requests if you want to contribute to this project.
