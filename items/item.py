from random import choice
from abc import ABC


class Item(ABC):

    def __init__(self):
        self.picture = None
        self.items: list = []

    def get(self):
        item = choice(self.items)
        return item
