#import datetime

# class Book():
#
#     def __init__(self, name, author, year):
#         self.name = name
#         self.author = author
#         self.year = year
#
#
#
#     def book_age(self):
#         today = datetime.date.today()
#         age = today.year - self.year
#         print("The book '{0}' is {1} years old.".format(self.name, age))
#
#     def get_into(self):
#         return f'Names book = {self.name}, author = {self.author}, Year of publication = {self.year}.'
#
#
#
# b = Book('The Picture of Dorian Gray', 'Oscar Wilde', 1890)
#
# print(b.get_into())
# print(b.book_age())







class Student:
    def __init__(self, name, last_name, age, avg_grade):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.avg_grade = avg_grade

    def get_info(self):
        return f'Name = {self.name}, last_name = {self.last_name}, age = {self.age}, avg_grade = {self.avg_grade}.'

    def scholarship(self):
        if self.avg_grade >= 9:
            return 1500
        elif self.avg_grade >= 8:
            return 1000
        elif self.avg_grade >= 7:
            return 500
        else:
            return 0



s = Student('Daria', 'Tkach', 16, 9)

s.get_info()
print("Студент отримує стипендію в розмірі {0} грн.".format(s.scholarship()))


print(s.get_info())
