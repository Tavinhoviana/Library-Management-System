class User:
    _id_counter = 1

    def __init__(self, name):
        self.name = name
        self.user_id = User._id_counter
        User._id_counter += 1
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed the book '{book.title}'.")
        else:
            print(f"The book '{book.title}' is not available at the moment.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned the book '{book.title}'.")
            return True
        print(f"{self.name} does not have the book '{book.title}' to return.")
        return False

    def __str__(self):
        return f"{self.name} (ID: {self.user_id})"


class Book:
    def __init__(self, title):
        self.title = title
        self.available = True

    def borrow(self):
        self.available = False

    def return_book(self):
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} ({status})"


class Library:
    def __init__(self):
        self.users = []

    def register_user(self, user):
        self.users.append(user)
        print(f"User {user.name} registered with ID {user.user_id}.")

    def search_book(self, title):
        for user in self.users:
            for book in user.borrowed_books:
                if title.lower() in book.title.lower():
                    return book
        return None

    def list_books(self):
        print("\n📚 Books borrowed by users:")
        for user in self.users:
            for book in user.borrowed_books:
                print(f"- {book.title} (Borrowed by {user.name})")
        print()


def main():
    library = Library()
    user = []
    book = []

    while True:
        print("\n--- Library Menu ---")
        print("1. Register new user")
        print("2. View registered users")
        print("3. Borrow book")
        print("4. List books borrowed by users")
        print("5. Return book")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("User name: ")
            user = User(name)
            library.register_user(user)

        elif choice == "2":
            print("\n👥 Registered users:")
            if not library.users:
                print("No users registered yet.")
            else:
                for user in library.users:
                    print(f"- {user}")

        elif choice == "3":
            name = input("User name: ")
            user = next((u for u in library.users if u.name == name), None)
            if user:
                title = input("Title of the book to borrow: ")
                book = Book(title)
                user.borrow_book(book)
            else:
                print("User not found.")

        elif choice == "4":
            library.list_books()

        elif choice == "5":
            name = input("User name: ")
            user = next((u for u in library.users if u.name == name), None)
            if user:
                title = input("Title of the book to return: ")
                book = next((b for b in user.borrowed_books if b.title == title), None)
                if book:
                    user.return_book(book)
                else:
                    print("This user does not have that book.")
            else:
                print("User not found.")

        elif choice == "6":
            print("Exiting the system...")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
