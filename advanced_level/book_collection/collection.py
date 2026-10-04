### python by moshiurr007 --> advanced_level ###

# book collection --> collection.py #

from book import Book
from series import Series

class Collection:
    def __init__(self):
        self.collection = []

    # get only books from the collection
    def get_books(self):
        return [book for book in self.collection if isinstance(book, Book)]

    # get only series from the collection
    def get_series(self):
        return [book for book in self.collection if isinstance(book, Series)]

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
        if not item in self.collection:
            self.collection.append(item)

    # add books to a series
    def add_book_to_series(self, series:Series, book:Book):
        series.add_book(book)
        if book not in self.collection:
            self.collection.append(book)

    # update a book or a series
    def update(self, item_id, **fields):
        for item in self.collection:
            if item.id == item_id:
                item.update(**fields)
                return f"Updated: {item}"
        raise ValueError("No book or series found with that ID.")

    # delete a book from the collection & its series
    def delete_book(self, book_id):
        for book in self.get_books():
            if book.id == book_id:
                self.collection.remove(book)

                # also delete the book from its series
                for series in self.get_series():
                    if book in series.books:
                        series.delete_book(book_id)
                
                return f"Deleted: {book}"
        raise ValueError("No book found with that ID.")

    # delete a series from the collection
    def delete_series(self, series_id):
        for series in self.get_series():
            if series.id == series_id:
                self.collection.remove(series)
                return f"Deleted: {series.name}\n{len(series.books)} books stay in the collection."
        raise ValueError("No series found with that ID.")

    # show books by genre
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
