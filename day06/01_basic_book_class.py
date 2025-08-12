class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        print(f"'{self.title}' by {self.author}, {self.pages} pages.")

book1 = Book("Python Basics", "Rupesh", 250)
book1.display_info()
