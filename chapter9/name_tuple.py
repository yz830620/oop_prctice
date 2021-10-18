from collections import namedtuple


Book = namedtuple("Book", "author title genre")

books = [
    Book("Pratchett", "Nightwatch", "fantasy"),
    Book("Pratchett", "Thief Of Time", "fantsy"),
    Book("LeGuin", "The Dispossessed", "scifi"),
    Book("LeGuin", "A Wizard Of Earthsea", "fantasy"),
    Book("Turner", "The Thief", "fantasy"),
    Book("Phillips", "Preston Diamond", "western"),
    Book("Phillips", "Twice Upon A Time", "scifi"),
]


fantasy_author = {b.author for b in books if b.genre == "fantasy"}
print("fantasy_author: ", fantasy_author)

fantasy_book = {b.title for b in books if b.genre == "fantasy"}
print('fantasy_book: ', fantasy_book)
