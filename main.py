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
app.secret_key = 'оченьоченьсекретно'  # для флешей?

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

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    categories = load_categories()
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        author = request.form.get('author', '').strip()
        category_id = request.form.get('category_id')
        if name and author and category_id:
            books = load_books()
            new_id = max([b['id'] for b in books], default=0) + 1
            new_book = Book(new_id, name, author, int(category_id)).to_dict()
            books.append(new_book)
            save_books(books)
            flash(f"Книга '{name}' добавлена!")
            return redirect(url_for('home'))
    return render_template('add_book.html', categories=categories)

@app.route('/add_category', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        if name:
            categories = load_categories()
            new_id = max([c['id'] for c in categories], default=0) + 1
            new_category = Category(new_id, name).to_dict()
            categories.append(new_category)
            save_categories(categories)
            flash(f"Категория '{name}' добавлена!")
            return redirect(url_for('home'))
    return render_template('add_category.html')

if __name__ == '__main__':
    app.run(debug=True)