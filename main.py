from flask import Flask, render_template
import requests
import json
import os
import logging

logging.basicConfig(
    filename='logs.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s'
)

app = Flask(__name__)

def load_books():
    if os.path.exists('json/books.json'):
        with open('json/books.json', 'r') as file:
            logging.info('Loading books from books.json')
            return json.load(file)
    return []

def save_books(books):
    with open('json/books.json', 'w') as file:
        logging.info('Saving books to books.json')
        json.dump(books, file)

def load_categories():
    if os.path.exists('json/categories.json'):
        with open('json/categories.json', 'r') as file:
            logging.info('Loading categories from categories.json')
            return json.load(file)
    return []

def save_categories(categories):
    with open('json/categories.json', 'w') as file:
        logging.info('Saving categories to categories.json')
        json.dump(categories, file)

@app.route('/')
def home():
    return render_template('index.html', books=load_books(), categories=load_categories())

@app.route('/add')
def add_book():
    name = requests.form.get('name')
    author = requests.form.get('author')
    category = requests.form.get('category')

    books = load_books()
    categories = load_categories()
    if name and author and category:
        books.append({
            'name': name,
            'author': author,
            'category': category
        })
        save_books(books)
        logging.info(f'Book added: {name}, {author}, {category}')

    return render_template('add_form.html')

if __name__ == '__main__':
    app.run(debug=True)