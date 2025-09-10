from flask import Flask, render_template, request
import pickle

# Load popular books
popular_books = pickle.load(open('notebook/popular_books.pkl','rb'))

app = Flask(__name__)

# Home page showing popular books
@app.route('/')
def home():
    return render_template(
        'index.html',
        book_name=list(popular_books['Book-Title'].values),
        author=list(popular_books['Book-Author'].values),
        image=list(popular_books['Image-URL-M'].values),
        votes=list(popular_books['rating_count'].values),
        rating=list(popular_books['avg_rating'].values)
    )

# Search route to handle book search
@app.route('/search', methods=['POST'])
def search():
    query = request.form['book_name'].lower()
    
    # Filter popular_books for titles containing the query (case-insensitive)
    results = popular_books[popular_books['Book-Title'].str.lower().str.contains(query)]

    return render_template(
        'recommend.html',
        query=query,
        book_name=list(results['Book-Title'].values),
        author=list(results['Book-Author'].values),
        image=list(results['Image-URL-M'].values),
        votes=list(results['rating_count'].values),
        rating=list(results['avg_rating'].values)
    )

if __name__ == '__main__':
    app.run(debug=True)
