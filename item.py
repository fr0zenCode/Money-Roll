from random import choice
from abc import ABC, abstractmethod


class Item(ABC):

    def __init__(self):
        self.items = []

    def get(self):
        item = choice(self.items)
        return item
