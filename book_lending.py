import random
from datetime import datetime

# my_list = [12, 45, 5, 7, 88, 101]
# random.choice(my_list)

# print(random.choice(my_list))
# print(random.choice(my_list))

# now = datetime.now()
# print(now)

class Book:

    on_shelf = []
    on_loan = []

    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
    
    def __str__(self):
        return self.title
        
    
    

    def return_to_library(self):
        if self.lent_out():
            Book.on_shelf.append(self)
            Book.on_loan.remove(self)
            return True
        else:
            return False


    def lent_out(self, book):
        for book in self.on_shelf:
            if book.title == self.title:
                return False
            else:
                pass
        return True
        
    def borrow(self):
        if self.lent_out():
            return False

    @classmethod
    def create(cls, title, author, ISBN):
        cls.on_shelf.append(Book(title, author, ISBN))

        
    @classmethod
    def current_due_date(cls):
        now = datetime.now()
        two_weeks = 60 * 60 * 24 * 14 # two weeks expressed in seconds  
        future_timestamp = now.timestamp() + two_weeks
        return datetime.fromtimestamp(future_timestamp)
    @classmethod
    def over_due_books(cls):
        overdue = []
        for book in cls.on_loan:
            if book.due_date < datetime.now():
                overdue.append(book)
        return overdue
    
    @classmethod
    def browse(cls):
        return random.choice(cls.on_shelf)
    
        


book1 = Book.create('a', 'y', '5')

