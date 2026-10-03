import uuid

class Collection:
    def __init__(self):
        self.collection = []

    # search by book, series, author
    def search(self, value):
        if not value.strip():
            raise ValueError("Search by book, series, author.")
        value = value.strip().lower()
        matches = []

        for item in self.collection:
            if isinstance(item, Book):
                title = item.title.strip().lower()
                author = item.author.strip().lower()
            elif isinstance(item, Series):
                title = item.name.strip().lower()
                author = item.author.strip().lower()
            else:
                continue
            if value in title or value in author:
                    matches.append(item)

        if not matches:
            return f"No search result for '{value.capitalize()}'."
        
        result = f"Search result for '{value.capitalize()}':\n"

        for i, item in enumerate(matches, 1):
            result += f"{i}. {item}\n"

        return result.rstrip()


    # add a book or a series
    def add(self, item):
        if not isinstance(item, (Book,Series)):
            return "Only Book or Series can be added."
        self.collection.append(item)

    # add books to a series
    def add_book_to_series(self, series:Series, book:Book):
        series.add_book(book)
        if book not in self.collection:
            self.collection.append(book)


    def update(self, item_id):
        pass

    def delete_book(self, book_id):
        pass

    def delete_series(self, series_id):
        pass

    def get_books(self):
        return [book for book in self.collection if isinstance(book, Book)]

    def get_series(self):
        return [book for book in self.collection if isinstance(book, Series)]

    def show_books_by_genre(self, genre):
        genre = genre.strip().lower()

        matches = [
            item for item in self.collection
            if isinstance(item, Book) and genre in [g.strip().lower() for g in item.genres]
            ]
        if not matches:
            return f"No books found for '{genre.capitalize()}'."

        result = f"Genre '{genre.capitalize()}' ({len(matches)}):\n"
        for i, item in enumerate(matches, 1):
            result+=f"{i}. {item}\n"

        return result.rstrip()

    def sort(self):
        pass

    def __str__(self):
        if not self.collection:
            return "Your collection is empty. Add some books."
        
        books = self.get_books()
        series = self.get_series()

        result = f"\n---------- MY COLLECTION ----------\n"
        if books:
            result += f"\n===== BOOK ({len(books)}) =====\n"
            for i, book in enumerate(books, 1):
                result += f"{i}. {book}\n"
        if series:
            result += f"\n===== SERIES ({len(series)}) =====\n"
            for i, ser in enumerate(series, 1):
                result += f"{i}. {ser}\n"

        return result



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
        self.year = year
        self.rating = rating

    def __str__(self):
        year = f"({self.year}) " if not self.year is None else ''
        rating = f"{self.rating}" if not self.rating is None else ''
        return f"{self.title} {year}by {self.author} | Rating: {rating}/10"

    def __repr__(self):
        return str(self)

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
                return "Only Books can be added."
        self.books.append(book)

    def update_book(self, book_id):
        pass

    def delete_book(self, book_id):
        pass

    def __str__(self):
        rating = f"{self.rating}" if not self.rating is None else ''
        result = f"{self.name} ({len(self.books)} books) by {self.author} | Rating: {rating}/10"
        for book in self.books:
            result += f"\n      - {book}"
        return result

    def __repr__(self):
        return str(self)

def main():
    collection = Collection()

    #----- BOOK -----#
    alchemist = Book("The Alchemist", "Paulo Cuelho", ["Philosophy"], rating=9)
    twilight_of_the_idols = Book("Twilight of the Idols", "Friedrich Nietzsche", ["Philosophy"], rating=7)

    collection.add(alchemist)
    collection.add(twilight_of_the_idols)

    #----- SERIES -----# 
    series1 = Series("Series One", "XYZ", ['Sci-fi', "Action", "Adventure", "Philosophy"], 7.5)
    collection.add(series1)
    a = Book("Book A", "Random", ['Sci-fi', "Philosophy"], 7.5)
    b = Book("Book B", "Random", ['Action', "Adventure"], 7.5)
    c = Book("Book C", "Random", ['Action', "Espionage"], 7.5)
    for book in (a,b,c):
        collection.add_book_to_series(series1, book)

    # print(collection)

    #----- SHOW BOOKS BY GENRE -----#
    # print(collection.show_books_by_genre("pHiloSOpHy"))

    #----- SEARCH -----#
    print(collection.search("hey"))
    print(collection.search("light"))

if __name__ == '__main__':
    main()