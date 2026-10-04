### python by moshiurr007 --> advanced_level ###

# book collection --> series.py #

import uuid

from book import Book

class Series():
    def __init__(self, name, author, genres, rating):
        if not name.strip():
            raise ValueError('Series name is required.')
        if not author.strip():
            raise ValueError('Author name is required.')
        if not isinstance(genres, list) or not genres:
            raise ValueError('At least one genre is required.')
        for genre in genres:
            if not genre.strip():
                raise ValueError('Genre cannot be empty.')
        if not rating:
            raise ValueError('Rating is required.')
        self.id = uuid.uuid4()
        self.name = name
        self.author = author
        self.genres = genres
        self.rating = rating

        self.books = []

    def add_book(self, book):
        if not isinstance(book, Book):
                raise TypeError("Only Books can be added.")
        if book not in self.books:
            self.books.append(book)

    # delete a book from a series
    def delete_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                return f"Removed from series: {book}"
        raise ValueError("No book with that ID in this series.")
    
    # update series info
    def update(self, name=None, author = None, genres = None, rating = None):
        new_name = self.name if name is None else name
        new_author = self.author if author is None else author
        new_genres = self.genres if genres is None else genres
        new_rating = self.rating if rating is None else rating

        Series(new_name, new_author, new_genres, new_rating)

        self.name = new_name
        self.author = new_author
        self.genres = new_genres
        self.rating = new_rating

    def __str__(self):
        rating = f"{self.rating}" if not self.rating is None else ''
        result = f"{self.name} ({len(self.books)} books) by {self.author} | Rating: {rating}/10"
        for book in self.books:
            result += f"\n      - {book}"
        return result

    def __repr__(self):
        return str(self)
