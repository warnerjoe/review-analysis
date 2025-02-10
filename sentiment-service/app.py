from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    review_text = data.get('review')


    if not review_text:
        return jsonify({'error': 'No review text provided'}), 400

    print(f"Review text received: {review_text}")

    # Perform sentiment analysis on the entire review
    blob = TextBlob(review_text)
    polarity = blob.sentiment.polarity * 10000

    # Determine sentiment category
    if polarity > 5:
        sentiment = 'Positive'
    elif polarity < -5:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    return jsonify({
        'sentiment': sentiment,
        'score': round(polarity, 4)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
