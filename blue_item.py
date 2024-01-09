from random import choice
from item import Item


class BlueItem(Item):

    def __init__(self):
        super().__init__()
        self.items = [1, 5, 10, 15]


if __name__ == '__main__':
    blue_item = BlueItem()
    print(blue_item.get())
