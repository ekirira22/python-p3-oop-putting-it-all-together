#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand="Adidas", size=9):
        self.brand = brand
        self.size = size

    condition = "New"
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")

    def cobble(self):
        print("Your shoe is as good as new!")


erics_shoe = Shoe()
print(erics_shoe.size)
