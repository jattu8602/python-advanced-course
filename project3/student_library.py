class Library:

    def __init__(self, listOfBooks):
        self.books = listOfBooks
    def displayAvilableBooks(self):
        print("books present in this library are: ")
        for book in self.books:
            
            print("\t *" + book)    
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"ypu have been issued {bookName}. pllease keep it safe and return it within 30 days")
            self.books.remove(bookName)
        else:
            print("sorry, this book has already been issued to someone else. please wait untilthe book is returned") 
    def returnBook(self, bookName):
        self.book.append(bookName)    
        print("thanks for returning book! Hope you enjoyed it. Have a great day ahead!")       


class Student:
    def requestBook(self):
        self.book = input("enter the name of the book you want to borrow: ")
        return self.book
    def returnBook(self):
        self.book = input("enter the name of the book you want to return: ")
        return self.book
    

if __name__ == "__main__":
    centraLibrary = Library(["algorithms", "Django", "clrs", "python notes"])
    # centraLibrary.displayAvilableBooks()
    while(True):
        welcomeMsg = '''====welcome to central library====
        please choose an option:
        1. list all the books
        2. request a book
        3. return a book
        4. exit the library
        '''
        print(welcomeMsg)
        a = int(input("enter a choice: "))
        if a == 1:
            centraLibrary.displayAvilableBooks()
        elif a == 2:
            centraLibrary.borrowBook(Student.requestBook())  
        elif a == 3:
            centraLibrary.returnBook(Student.returnBook()) 
        elif a == 4:
               print("thanks for using central library! have a great day ahead")
               exit()
        else:
            print("invalid choice")
        






























































































