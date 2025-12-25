class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def getinfo(self):
        return f'Название книги:{self.title}, Автор: {self.author}, Год издания: {self.year}'
book1 = Book("Выбранные места", "Файзов Д.М.", "1990")
print(book1.getinfo())