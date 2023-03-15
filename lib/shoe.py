#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand="Adidas", size=0, condition="Used",color="White",material="Leather"):
        self.brand=brand
        self.size=size
        self.condition=condition
        self.color=color
        self.material=material

    def get_size(self):
        return self._size
    
    def set_size(self, num):
        if (type(num)) is int:
            self._size=num
        else:
            print("size must be an integer")

    size=property(get_size, set_size)

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition="New"

