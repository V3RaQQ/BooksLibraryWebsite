import os
import json
import logging

class Category:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def to_dict(self):
        return {"id": self.id, "name": self.name}

class Book:
    def __init__(self, id: int, name: str, author: str, category_id: int):
        self.id = id
        self.name = name
        self.author = author
        self.category_id = category_id

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "author": self.author,
            "category_id": self.category_id
        }

def load_categories():
    if os.path.exists('json/categories.json'):
        with open('json/categories.json', 'r', encoding='utf-8') as file:
            logging.info('Loading categories from categories.json')
            return json.load(file)
    return []

def save_categories(categories):
    with open('json/categories.json', 'w', encoding='utf-8') as file:
        logging.info('Saving categories to categories.json')
        json.dump(categories, file, ensure_ascii=False, indent=2)

def load_books():
    if os.path.exists('json/books.json'):
        with open('json/books.json', 'r', encoding='utf-8') as file:
            logging.info('Loading books from books.json')
            books = json.load(file)
            if isinstance(books, dict):
                books = list(books.values())
            return books
    return []

def load_categories():
    if os.path.exists('json/categories.json'):
        with open('json/categories.json', 'r', encoding='utf-8') as file:
            logging.info('Loading categories from categories.json')
            categories = json.load(file)
            if isinstance(categories, dict):
                categories = list(categories.values())
            return categories
    return []

def save_books(books):
    with open('json/books.json', 'w', encoding='utf-8') as file:
        logging.info('Saving books to books.json')
        json.dump(books, file, ensure_ascii=False, indent=2)