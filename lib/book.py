#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count=0):
        self.title = title # creating an attribute called title and assigning it the value of the title parameter
        self.page_count = page_count # creating an attribute called page_count and assigning it the value of the page_count parameter

    pass

    def __str__(self):
        return self.title # returns the value of the title attribute

    def get_page_count(self): # self is a reference to the instance of the class

        return self._page_count # self.page_count is an attribute of the Book class
    
    def set_page_count(self, page_count): # creating a getter method for the page_count attribute


        if isinstance(page_count, int): # isinstance is a built-in function that returns True if the object is an instance of the class

            self._page_count = page_count # in this case, it checks if page_count is an integer. if it is, it assigns the value of page_count to the attribute _page_count

        else:
            print("page_count must be an integer") 
            self._page_count = None # if it is not, it prints an error message and assigns None to the attribute _page_count.
            
        
    page_count = property(get_page_count, set_page_count) # property is a built-in function that returns a property attribute


    def turn_page(self):
        print("Flipping the page...wow, you read fast!") # prints a string


# Path: lib/book.py
    

    