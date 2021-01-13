# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# HarryLibrary = Library(listofbooks, library_name)


# dictionary (books-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input

class Library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lendict = {}

    def displaybook(self):
        print(f"We have following books in {self.name} library")
        for book in self.booklist:
            print(book)

    def lendbook(self, user, book):
        if book not in self.lendict.keys():
            self.lendict.update({book: user})
            print("database has been updated.You can take the book now")
        else:
            print(f"the book is being used by {self.lendict[book]} ")

    def addbook(self,book):
        self.booklist.add(book)
        print("Book has been sucessfully added to the list ")



    def returnbook(self, book):
        self.lendict.pop(book)


if __name__ == '__main__':
    naman = Library({"Hunger Games", "Fifety shades", "Harry Potter",
                     "REV.2020", "Pennywise"}, "Euphoria")

    while (True):
        print(f"Welcome to {naman.name} Library. Enter the choice to continue: ")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a book")
        print("4. Return a Book \n")
        user_choice = int(input())

        if user_choice == 1:
            naman.displaybook()
        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend: ")
            user = input("Enter the name of the user:")
            naman.lendbook(user, book)
        elif user_choice == 3:
            book = input("Enter the name of the book you want to add: ")
            naman.addbook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return: ")
            naman.returnbook(book)
        else:
            print("Enter a valid option")

        print("Enter q to quit and c to continue:- ")
        user_choice2 = input()
        if user_choice2 == "q":
            exit()
        elif user_choice2 == "c":
            continue
