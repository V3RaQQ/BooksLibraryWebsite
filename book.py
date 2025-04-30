class Category:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def to_dict(self):
        return {"name": self.name}


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