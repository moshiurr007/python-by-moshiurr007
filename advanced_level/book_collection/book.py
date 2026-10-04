### python by moshiurr007 --> advanced_level ###

# book collection --> books.py #

import uuid

class Book:
    def __init__(self, title, author, genres, rating, year=None):
        if not title.strip():
            raise ValueError('Title is required.')
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
        self.title = title
        self.author = author
        self.genres = genres
        self.rating = rating
        self.year = year

    def update(self, title=None, author=None, genres=None, rating=None, year=None):
            new_title = title if not title is None else self.title
            new_author = author if not author is None else self.author
            new_genres = genres if not genres is None else self.genres
            new_rating = rating if not rating is None else self.rating
            new_year = year if not year is None else self.year

            Book(new_title, new_author, new_genres, new_rating, new_year)

            self.title = new_title
            self.author = new_author
            self.genres = new_genres
            self.rating = new_rating
            self.year = new_year

    def __str__(self):
        year = f"({self.year}) " if not self.year is None else ''
        rating = f"{self.rating}" if not self.rating is None else ''
        return f"{self.title} {year}by {self.author} | Rating: {rating}/10"

    def __repr__(self):
        return str(self)
