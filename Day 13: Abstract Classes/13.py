#Write MyBook class
class MyBook(Book) :
    def __init__(self,title,auther,price):
        self.price=price
    def display(self) :
        print("Title: {}".format(title))
        print("Author: {}".format(author))
        print("Price: {}".format(price))
