class Book:
    def __init__(self, name, author, book_id):
        self.name = name
        self.author = author
        self.id = book_id
        self.next = None

class Student:
    def __init__(self, name, email, book, author, book_id):
        self.name = name
        self.email = email
        self.book = book
        self.author = author
        self.id = book_id
        self.next = None

class Library:
    def __init__(self):
        self.start_lib = None
        self.start_student = None

    def initialize_lib(self):
        books = [
            ("The Kite Runner", "Khaled Hosseini", 101),
            ("To Kill A Mockingbird", "Harper Lee", 102),
            ("The Alchemist", "Paulo Coelho", 103),
            ("Pride And Prejudice", "Jane Austen", 104),
            ("A Tale Of Two Cities", "Charles Dickens", 105)
        ]
        for name, author, book_id in books:
            self.add_book(name, author, book_id)

    def add_book(self, name, author, book_id):
        new_book = Book(name, author, book_id)
        if self.start_lib is None:
            self.start_lib = new_book
        else:
            ptr = self.start_lib
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = new_book

    def delete_book(self, book_id):
        ptr = self.start_lib
        if ptr is None:
            return

        if ptr.id == book_id:
            self.start_lib = ptr.next
            return

        prev_ptr = None
        while ptr is not None and ptr.id != book_id:
            prev_ptr = ptr
            ptr = ptr.next

        if ptr is not None:
            prev_ptr.next = ptr.next

    def issue_book(self):
        if self.start_lib is None:
            print("No books left in the library to issue!")
            return

        ptr = self.start_lib
        i = 1
        print("Books Available:")
        while ptr is not None:
            print(f"Book {i}:")
            print(f"  Title: {ptr.name}")
            print(f"  Author: {ptr.author}")
            print(f"  ID: {ptr.id}")
            print("  ------------------")
            ptr = ptr.next
            i += 1

        book_id = int(input("Enter the Book ID: "))
        ptr = self.start_lib
        while ptr is not None and ptr.id != book_id:
            ptr = ptr.next

        if ptr is None:
            print("Invalid Book ID!")
            return

        student_name = input("Enter your Name: ")
        student_email = input("Enter your Email: ")
        new_student = Student(student_name, student_email, ptr.name, ptr.author, ptr.id)

        if self.start_student is None:
            self.start_student = new_student
        else:
            ptr2 = self.start_student
            while ptr2.next is not None:
                ptr2 = ptr2.next
            ptr2.next = new_student

        self.delete_book(book_id)
        print(f"Book ID {book_id} issued successfully!")

    def return_book(self):
        if self.start_student is None:
            print("No books to return!")
            return

        book_id = int(input("Enter the Book ID: "))
        ptr = self.start_student
        prev_ptr = None

        while ptr is not None and ptr.id != book_id:
            prev_ptr = ptr
            ptr = ptr.next

        if ptr is None:
            print("Invalid Book ID!")
            return

        if prev_ptr is None:
            self.start_student = ptr.next
        else:
            prev_ptr.next = ptr.next

        self.add_book(ptr.book, ptr.author, ptr.id)
        print(f"Book ID {book_id} returned successfully!")

    def display_students(self):
        ptr = self.start_student
        while ptr is not None:
            print(f"Student Name: {ptr.name}")
            print(f"Email: {ptr.email}")
            print(f"Book Issued: {ptr.book}")
            print(f"Book ID: {ptr.id}")
            print("  ------------------")
            ptr = ptr.next

def main():
    library = Library()
    library.initialize_lib()

    while True:
        print("Main Menu:")
        print("1. Issue Book")
        print("2. Return Book")
        print("3. Display Student Details")
        print("4. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            library.issue_book()
        elif choice == 2:
            library.return_book()
        elif choice == 3:
            library.display_students()
        elif choice == 4:
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
