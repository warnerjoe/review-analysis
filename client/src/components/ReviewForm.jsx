import { useState } from 'react';
import axios from 'axios';

export default function ReviewForm() {
  const [review, setReview] = useState('');
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/reviews/submit', {
        reviewText: review
      });
      setResult(response.data.data);
    } catch (error) {
      console.error('Error submitting review', error);
    }
  };

  return (
    <div className="p-4 max-w-md mx-auto">
      <h1 className="text-2xl font-bold mb-4">Submit a Review</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          value={review}
          onChange={(e) => setReview(e.target.value)}
          className="w-full p-2 border rounded"
          rows="4"
          placeholder="Enter your review here..."
        />
        <button type="submit" className="mt-2 px-4 py-2 bg-blue-500 text-white rounded">
          Analyze
        </button>
      </form>

      {result && (
        <div className="mt-4 p-4 bg-gray-100 rounded">
          <h2 className="text-xl font-semibold">Sentiment: {result.sentiment}</h2>
          <p>Score: {result.score.toFixed(2)}</p>
          <p>Review: {result.reviewText}</p>
        </div>
      )}
    </div>
  );
}
