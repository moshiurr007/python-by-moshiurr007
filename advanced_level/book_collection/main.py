### python by moshiurr007 --> advanced_level ###

# book collection --> main.py #

from collection import Collection
from book import Book
from series import Series

def main():
    collection = Collection()

    #----- BOOK -----#
    alchemist = Book("The Alchemist", "Paulo Cuelho", ["Philosophy"], rating=9)
    twilight_of_the_idols = Book("Twilight of the Idols", "Friedrich Nietzsche", ["Philosophy"], rating=7)

    collection.add(alchemist)
    collection.add(twilight_of_the_idols)

    #----- SERIES -----# 
    series1 = Series("Series One", "XYZ", ['Sci-fi', "Action", "Adventure", "Philosophy"], 7.5)
    fav_history_series = Series("Fav History Series", "Multiple Authors", ['History', 'War'], 8)

    collection.add(series1)
    collection.add(fav_history_series)

    a = Book("Book A", "Karim", ['Sci-fi', "Philosophy"], 7.5)
    b = Book("Book B", "Karim", ['Action', "Adventure"], 7.5)
    c = Book("Book C", "Karim", ['Action', "Thriller"], 7.5)
    
    for book in (a,b,c):
        collection.add_book_to_series(series1, book)

    h = Book("Book H", "Rahim", ['War', "History"], 8)
    collection.add_book_to_series(fav_history_series, h)

    # print(collection)

    #----- SHOW BOOKS BY GENRE -----#
    # print(collection.show_books_by_genre("pHiloSOpHy"))

    #----- SEARCH -----#
    # print(collection.search("hey"))
    # print(collection.search("light"))

    #----- DELETE -----#
    # print(collection.delete_series(fav_history_series.id))
    # print(collection.delete_book(b.id))
    # print(collection)

if __name__ == '__main__':
    main()