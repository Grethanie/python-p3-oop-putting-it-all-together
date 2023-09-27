#!/usr/bin/env python3

class Shoe:
    
    
    def __init__(self, brand, size):
        self.brand, self.size = brand, size
    
    def get_brand(self):
        return self._brand
    
    def get_size(self):
        return self._size
    
    def set_brand(self, brand):
        self._brand = brand
    
    def set_size(self, size):
        if type(size) is not int:
            print("size must be an integer")
            return
        self._size = size
        
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
    
    size = property(get_size, set_size)   
    brand = property(get_brand, set_brand)