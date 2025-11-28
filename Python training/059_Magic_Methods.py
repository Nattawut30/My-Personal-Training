# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of Python's built-in operations.
#                 They allow developers, to define or customize the behavior of objects

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    # And this is dunder string. We can return a string representation of the object
    # When we print it directly to the console

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self, other): #other means the other book
        return self.title == other.title and self.author == other.author
        # Disregard how many book pages in there, just the same title or same author

    def __lt__(self, other):
        return self.num_pages < other.num_pages #Return a boolean value

    def __gt__(self, other): #Let's try greater this time
        return self.num_pages > other.num_pages

    def __add__(self, other): #Total page combined
        return f"{self.num_pages + other.num_pages} pages"

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title # find title
        elif key == "author":
            return self.author # find author
        elif key == "num_pages":
            return self.num_pages  # find number of pages
        else:
            return f"key '{key}' was not found" # Can't find any

book1 = Book("The Hobbit", "J.R.R Tolkien", 310)
book2 = Book("Harry Potter and the The Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrope", "C.S. Lewis", 172)
book4 = Book("The Hobbit", "J.R.R Tolkien", 444)

print(book2) #__str__
print(book1 == book4) #__eq__
print(book1 < book3) #__lt__
print(book2 > book3) #__gt__
print(book1 + book3) #__add__
print("Lion" in book3) #__contains__
print("Rowling" in book3) #__contains__
print(book2['title']) #__getitem__
print(book3['author']) #__getitem__
print(book1['num_pages']) #__getitem__
print(book1['audio']) #__getitem__