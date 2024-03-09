#!/usr/bin/env python3
import ipdb


class Book:
    def __init__(self, title="And Then There Were None", page_count=272):
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")


spiritual_world = Book("Spiritual World, By Peter Tan", 100)
print(spiritual_world.title)