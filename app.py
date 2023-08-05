from flask import Flask, render_template, request
import nltk
from textblob import TextBlob

nltk.download('punkt')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        text = request.form['text']
        blob = TextBlob(text)
        sentiment_score = blob.sentiment.polarity

        if sentiment_score > 0:
            sentiment = "positive"
            sentiment_emoji = "😃-Positive"
        elif sentiment_score < 0:
            sentiment = "negative"
            sentiment_emoji = "😔-Negative"
        else:
            sentiment = "neutral"
            sentiment_emoji = "😐-Neutral"

        result = {
            'sentiment_class': sentiment,
            'sentiment_emoji': sentiment_emoji,
            'sentiment_score': sentiment_score
        }

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=False)
