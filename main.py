from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os
import logging
from book import Book, Category, load_books, save_books, load_categories, save_categories

logging.basicConfig(
    filename='logs.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s'
)

app = Flask(__name__)

@app.route('/')
def home():
    books = load_books()
    categories = load_categories()
    category = request.args.get('category')
    search = request.args.get('search', '').strip().lower()
    filtered_books = []
    for b in books:
        if category and str(b.get('category_id')) != str(category):
            continue
        if search not in b.get('title', '').lower() and search not in b.get('author', '').lower():
            continue
        filtered_books.append(b)
    if not filtered_books and search:
        flash('Ничего не найдено!')
    return render_template('index.html', books=filtered_books, categories=categories)

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    categories = load_categories()
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        author = request.form.get('author', '').strip()
        category_id = request.form.get('category_id')
        if title and author and category_id:
            books = load_books()
            new_id = max([b['id'] for b in books], default=0) + 1
            new_book = Book(new_id, title, author, int(category_id)).to_dict()
            books.append(new_book)
            save_books(books)
            flash(f"Книга '{title}' добавлена!")
            return redirect(url_for('home'))
    return render_template('add_form.html', categories=categories)

if __name__ == '__main__':
    app.run(debug=True)