from random import choice
from abc import ABC


class Item(ABC):

    def __init__(self):
        self.items = []
        self.items_and_pictures: dict = {}

    def get(self):
        item = choice(self.items)
        return item, self.items_and_pictures[item]
