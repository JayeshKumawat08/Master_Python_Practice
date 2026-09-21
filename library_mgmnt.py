class Library:

    def __init__(self,book_list):
        self.__available_books =book_list

    def display_books(self):
        print("Currently Available Books\n")
        if self.__available_books:
            for book in self.__available_books:
                print(book)
        else:
            print("No books currently available")

    def borrow_book(self,book_name):
        if book_name in self.__available_books:
            self.__available_books.remove(book_name)
            print(f"Book borrowed {book_name}")
        else:
            print(f"{book_name} is already borrowed or not in the library")

    def return_book(self,book_name):
        self.__available_books.append(book_name)
        print(f"Thank you for returning {book_name} to the libbrary")

def run_library_system():

    initial_inventory = ["Python Crash Course", "Clean Code", "Data Structures", "Mastering AI"]
    my_library = Library(initial_inventory)

    while True:
        print("1.Display Books available")
        print("2.Borrow a Book")
        print("3.Return a Book")
        print("4.Exit")

        choice =  input("Enter your choice: ").strip()

        if choice == '1':
            my_library.display_books()

        elif choice == '2':
            book_title =  input("Enter the Book name to Issue: ").strip()
            my_library.borrow_book(book_title)

        elif choice == '3':
            book_title = input("Enter the name of the book to Return: ").strip()
            my_library.return_book(book_title)

        elif choice == '4':
            print("Exiting the Library System.")
            break

        else:
            print("Invalid Choice Selected.")

if __name__ == "__main__":
    run_library_system()
