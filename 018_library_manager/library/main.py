from mylibrary.library import Library

if __name__== "__main__":
    lib = Library()
    
    while True:
        print("\n1. Add book")
        print("2. Remove book")
        print("3. Search book")
        print("4. Show all books")
        print("5. Exit")
        
        choice=input("Choice: ")
        
        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            lib.add_book(title, author)
        elif choice == "2":
            title = input("Title: ")
            lib.remove_book(title)
        elif choice == "3":
            title = input("Title: ")
            lib.search_book(title)
        elif choice == "4":
            lib.show_books()
        elif choice =="5":
            break
            
    
    