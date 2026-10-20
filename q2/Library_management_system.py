#FORMATIVE ASSESSMENT NO. 1

# Define the Publication class
class Publication:
    def __init__(self, title, author,): # Initialize title and author of Publication
        self.__title = title
        self.__author = author

    def get_title(self): # Get title of Publication
        return self.__title

    def get_author(self): # Get author of Publication
        return self.__author
    
    def set_title(self, title): # Set title of Publication
        self.__title = title

    def set_author(self, author): # Set author of Publication
        self.__author = author

    def display_info(self): # Display information of Publication
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")
        
# Define the Book class that inherits from Publication
class Book(Publication):
    def __init__(self, title, author, number_of_pages): # Initialize title, author, and number of pages of Book
        super().__init__(title, author)
        self.__number_of_pages = number_of_pages

    def get_number_of_pages(self): # Get number of pages of Book
        return self.__number_of_pages

    def set_number_of_pages(self, number_of_pages):  # Set number of pages of Book
        if number_of_pages < 0:
            print("Number of pages must be positive.")
        return 
        self.__number_of_pages = number_of_pages
        
    def display_info(self): # Display information of Book
        super().display_info()
        print(f"Number of pages: {self.__number_of_pages}")

#Define the Magazine class that inherits from Publication
class Magazine(Publication):
    def __init__(self, title, author, issue_number): # Initialize title, author, and issue number of Magazine
        super().__init__(title, author)
        self.__issue_number = issue_number

    def get_issue_number(self): # Get issue number of Magazine
        return self.__issue_number

    def set_issue_number(self, issue_number): # Set issue number of Magazine
        self.__issue_number = issue_number
    
    def display_info(self): #Display the information of Magazine
        super().display_info()
        print(f"Issue Number: {self.__issue_number}")

# Create Object 1
publication1 = Publication("The Great Gatsby", "F. Scott Fitzgerald")
book1 = Book("To Kill a Mockingbird", "Harper Lee", 281)
magazine1 = Magazine("National Geographic", "Various Authors", 202)

#Printing the information of the objects in Object 1

print("Publication Information:")
publication1.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310)
book1.display_info()

print("\nMagazine Information:")
magazine1.display_info()

print()

# Create Object 2
publication2 = Publication("1984", "George Orwell")
book2 = Book("Pride and Prejudice", "Jane Austen", 432)
magazine2 = Magazine("Time", "Various Authors", 101)

#Printing the information of the objects in Object 1

print("Object 2 Information:")

print("Publication Information:")
publication2.display_info()

print("\nBook Information:")
book2.set_number_of_pages(432)
book2.display_info()

print("\nMagazine Information:")
magazine2.display_info()
