from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    review_text = data.get('review')

    if not review_text:
        return jsonify({'error': 'No review text provided'}), 400

    blob = TextBlob(review_text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = 'Positive'
    elif polarity == 0:
        sentiment = 'Neutral'
    else:
        sentiment = 'Negative'

    return jsonify({
        'sentiment': sentiment,
        'score': polarity
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
