
# print(b[5])

# try:
#     a=10
#     b="bb"
#     c=a+b
    
# except ZeroDivisionError:
#     print("different data types")
# except TypeError:
#     print("different data types")

# except Exception as e:
#     print(e)

# else:
#     print(c)
# finally:
#     print("finished")



# try: 
# 	raise NameError("Hi there") # Raise Error 
# except NameError: 
# 	print ("An exception") 
# 	raise
# -------------------------------------------------------------------------------------
# Create a Book class with attributes like title, author, and price. 
# Add a method called apply_discount() to reduce the price.
# Create a SpecialEditionBook class that inherits from Book and adds an attribute called special_feature (e.g., autographed copy). 
# Override the describe() method in both classes to display different messages.
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def apply_discount(self, discount_percent):
        self.price -= self.price * (discount_percent / 100)

    def describe(self):
        # return f"Book: '{self.title}' by {self.author}, Price: ₹{self.price:.2f}"
        return self.title,self.author,self.price


class SpecialEditionBook(Book):
    def __init__(self, title, author, price, special_feature):
        super().__init__(title, author, price)
        self.special_feature = special_feature

    def describe(self):
        return (f"Special Edition Book: '{self.title}' by {self.author}",f"Price: ₹{self.price:.2f}, Feature: {self.special_feature}")


book1 = Book("Python Basics", "Guido van Rossum", 500)
book1.apply_discount(10)

special_book = SpecialEditionBook("Advanced Python", "Raymond Hettinger", 800, "Autographed Copy")
special_book.apply_discount(20)

print(book1.describe())
print(special_book.describe())



