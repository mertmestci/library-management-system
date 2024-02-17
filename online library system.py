class Library:
    def __init__(self):
        self.file = open('book.txt','a+')
    def __del__(self):
        self.file.close()
    def list_books(self):
        self.file.seek(0)
        book_lines = self.file.read().splitlines()
        if not book_lines:
            print('Error.... list is empty please check!')
        else:
            for book in book_lines:
                book_name,author,release_date,pages = book.split(',')
                print(f"{book_name},{author}")
            print('Books are listed.')
    def add_books(self):
        book_name = input('please enter book name: ')
        author = input('please enter author: ')
        release_date = input('please enter release date: ')
        page = input('please enter page: ')
        book_info = f"Book name: {book_name},Author:{author},Release Date: {release_date},Page: {page}\n"
        self.file.write(book_info)
        print(f"Book {book_name} successfully added.")
    def remove_books(self):
        deleted_book = input('Which book do you want to remove: ')
        self.file.seek(0)
        book_lines = self.file.read().splitlines()
        if not book_lines:
            print('error..There is no book in lib')
        self.file.seek(0)
        self.file.truncate()
        book_removed = False
        for book in book_lines:
            if deleted_book not in book:
                self.file.write(book)
            else:
                book_removed = True
        if book_removed:
            print('selected book deleted successfully')
        else:
            print('the selected book was not found in the library.')


lib = Library()
while True:
    print(f"****Menu****\n1- List Books\n2- Add Book\n3- Remove Book\n4-Quit")
    menu_select = int(input('Please select option: '))
    if menu_select == 1:
        lib.list_books()
    elif menu_select == 2:
        lib.add_books()
    elif menu_select == 3:
        lib.remove_books()
    elif menu_select == 4:
        exit()
    else:
        print('invalid menu option please try again.')




