import datetime

class Book():

    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year



    def book_age(self):
        today = datetime.date.today()
        age = today.year - self.year
        print("The book '{0}' is {1} years old.".format(self.name, age))

    def get_into(self):
        return f'Names book = {self.name}, author = {self.author}, Year of publication = {self.year}.'



b = Book('The Picture of Dorian Gray', 'Oscar Wilde', 1890)

print(b.get_into())
print(b.book_age())