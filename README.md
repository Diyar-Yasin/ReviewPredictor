# Book Review Predictor
Using a precurated list of book reviews off of my [bookreviewwebsite](https://diyar-yasin.github.io/bookreviewwebsite-v2/) I take the first
n-5 ( where n is the total number of reviews ) reviews as Examples for the Cohere classifier model. 

The reviews contain 2 important parameters: content and rating.
- Content is the actual book review.
- Rating is an integer between [1, 5] 

## How To Try It Out Yourself
Clone the repository \
Create a .env with COHERE_API_KEY='your-api-key' \
Run python3 main.py

Using my current book reviews ( as of Jan. 12, 2024 ) this is what the program outputs: \
`Based on the previous reviews, we are able to guess with 80.0% accuracy what you would rate other books based on the review content!`

That means the Cohere classifier was able to correctly guess what rating my last 5 book reviews would be given based on the review content alone!

## Improvements
In the future I would love to inject this project directly into my [bookreviewwebsite-v2 repository](https://github.com/Diyar-Yasin/bookreviewwebsite-v2).
Then, whenever I add a new book review my classifier automatically predicts what rating I would give said novel.
This would help analyse the consistency of my written word.
