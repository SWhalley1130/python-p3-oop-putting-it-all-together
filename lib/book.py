#!/usr/bin/env python3

class Book:
    def __init__(self, title="And Then There Were None", page_count=0):
        self.title=title
        self.page_count=page_count

    def get_page_count(self):
        return self._page_count
    
    def set_page_count(self, num):
        if type(num) is int:
            self._page_count=num
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")


    page_count=property(get_page_count, set_page_count)
