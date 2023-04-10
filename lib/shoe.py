#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand): # the __init__ method is called when an instance of the class is created and it initializes the attributes of the class with the values passed in as parameters when the instance is created \
        self.brand = brand


    def get_size(self): # creating a getter method for the size attribute
        return self._size # self.size is an attribute of the Shoe class
    
    def set_size(self, size):
        if isinstance(size, int): # isinstance is a built-in function that returns True if the object is an instance of the class for example, isinstance(1, int) returns True because 1 is an integer and isinstance("1", int) returns False because "1" is not an integer
            self._size = size
        else:
            print("size must be an integer") # if the size parameter is not an integer, it prints an error message and assigns None to the attribute _size 
            self._size = None # self._size is an attribute of the Shoe class and it is private because it starts with an underscore and it is not meant to be accessed outside of the class definition 

    def cobble(self): # creating a method called cobble that prints a string and assigns the value "New" to the condition attribute of the instance of the class that called the method and returns None
        print("Your shoe is as good as new!") # prints a string 
        self.condition = "New" # self.condition is an attribute of the Shoe class and it is public because it does not start with an underscore and it is meant to be accessed outside of the class definition

    size = property(get_size, set_size) # property is a built-in function that returns a property attribute and it takes two parameters, the first is the getter method and the second is the setter method and it assigns the property attribute to the size attribute of the Shoe class and it is public because it does not start with an underscore and it is meant to be accessed outside of the class definition 
