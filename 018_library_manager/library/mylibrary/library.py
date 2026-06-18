class Library():
    def __init__(self):
        self.books=[]
        
    def add_book(self, title, author): 
        self.books.append({"title": title, "author": author})
        print(f"{title} added!")
        
    def remove_book(self, title):
        for book in self.books:
            if title == book["author"]:
                self.books.remove(book)
                print(f"'{title}' removed!")
                return
        print(f"'{title}' not found.")
    
    def search_book(self, title):
        for book in self.books:
            if title == book["author"]:
                print(f"Found: '{book['title']}' by {book['author']} ")
                return
        print(f"'{title}' not found.")
    
    def show_books(self):
        if not self.books:
            print("No books in library")
            return
        for i,book in enumerate(self.books, 1):
            print(f"{i}. '{book['title']}' by {book['author']}")
           

