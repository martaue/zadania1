class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library\n  City: {self.city}\n  Street: {self.street}\n  Zip Code: {self.zip_code}\n  Open Hours: {self.open_hours}\n  Phone: {self.phone}"


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Employee\n  Name: {self.first_name} {self.last_name}\n  Hire Date: {self.hire_date}\n  Birth Date: {self.birth_date}\n  Address: {self.city}, {self.street}, {self.zip_code}\n  Phone: {self.phone}"


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book\n  Author: {self.author_name} {self.author_surname}\n  Publication Date: {self.publication_date}\n  Number of Pages: {self.number_of_pages}\n  Library: {self.library}"


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student\n  Name: {self.name}\n  Marks: {self.marks}"


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = '\n  '.join(str(book) for book in self.books)
        return f"Order\n  Employee: {self.employee}\n  Student: {self.student}\n  Order Date: {self.order_date}\n  Books:\n  {books_str}"


library1 = Library("Katowice", "Bankowa", "24-456", "8-16", "658940438")
library2 = Library("Wrocław", "Studencka", "43-598", "9-17", "973649872")

employee1 = Employee("Katarzyna", "Nowak", "2023-10-31", "1980-03-25", "Katowice", "Bankowa", "24-456", "658940438")
employee2 = Employee("Sławomir", "Kowalski", "2023-11-02", "1970-12-09", "Krakow", "Polna", "43-576", "348264743")
employee3 = Employee("Anna", "Sakowska", "2022-03-03", "2000-03-03", "Warszawa", "Kolejowa", "34-348", "342324869")

student1 = Student("Kasia", [6, 4, 2])
student2 = Student("Basia", [5, 3, 4])
student3 = Student("Paweł", [3, 2, 4])

book1 = Book(library1, "1998", "Karol", "Nowakowski", 353)
book2 = Book(library2, "2013", "Olga", "Tokarczuk", 450)
book3 = Book(library1, "2014", "Juliusz", "Słowacki", 555)
book4 = Book(library2, "1999", "Elżbieta", "Kowalska", 350)
book5 = Book(library1, "2003", "Henryk", "Sinekiewicz", 250)

order1 = Order(employee1, student1, [book1, book2], "2023-11-05")
order2 = Order(employee2, student2, [book3, book4, book5], "2023-11-09")


print(order1)
print("\n")
print(order2)