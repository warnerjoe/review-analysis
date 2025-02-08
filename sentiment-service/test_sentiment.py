from textblob import TextBlob
from nltk.corpus import stopwords
import nltk

# Download the NLTK stopwords if you haven't already
nltk.download('stopwords')

# Define a list of filler words (can customize further)
filler_words = [
    "um", "uh", "like", "you know", "actually", "basically", "literally", "seriously", 
    "honestly", "just", "so", "well", "totally", "kinda", "sorta", "actually"
]

# Combine NLTK stopwords with the filler words for more comprehensive filtering
stop_words = set(stopwords.words('english'))  # NLTK stopwords
stop_words.update(filler_words)  # Add filler words to the stopwords list

def remove_filler_words(text):
    words = text.split()
    cleaned_words = [word for word in words if word.lower() not in stop_words]
    return " ".join(cleaned_words)

# Longer review sample
review_text = """
I stayed at this Airbnb recently, and it was a complete disaster from start to finish. The place was filthy upon arrival—dust everywhere, stained sheets, and a bathroom that clearly hadn't been cleaned in weeks. The pictures online were a total misrepresentation; what was supposed to be a cozy, modern apartment was more like a rundown, cramped space that hadn’t seen a renovation in decades. To make matters worse, there were several broken appliances that made the stay even more uncomfortable. The lack of basic amenities, such as clean towels and functioning Wi-Fi, made it feel more like a nightmare than a vacation. Additionally, communication with the host was frustratingly poor. Despite multiple attempts to contact them about the issues we encountered, I received delayed and unhelpful responses, leaving us with no recourse during our stay. It became evident that the host's primary concern was getting paid, not ensuring a positive experience for guests. To top it all off, the neighborhood was noisy, and the promised "quiet retreat" was anything but. I would strongly advise against booking this place unless you want to ruin your trip. Save yourself the headache and look elsewhere.
"""

# Remove filler and stop words
cleaned_review = remove_filler_words(review_text)

# Analyze sentiment with TextBlob
blob = TextBlob(cleaned_review)
polarity = blob.sentiment.polarity
subjectivity = blob.sentiment.subjectivity

print(f"Cleaned Review: {cleaned_review}")
print(f"Sentiment Polarity: {polarity}")
print(f"Sentiment Subjectivity: {subjectivity}")
