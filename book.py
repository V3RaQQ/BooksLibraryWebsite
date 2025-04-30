import os
import json
import logging

class Category:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def to_dict(self):
        return {"name": self.name}
    
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


class Book:
    def __init__(self, id: int, title: str, author: str, category_id: int):
        self.id = id
        self.title = title
        self.author = author
        self.category_id = category_id

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "category_id": self.category_id
        }

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