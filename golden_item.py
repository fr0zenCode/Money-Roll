from item import Item


class GoldenItem(Item):

    def __init__(self):
        super().__init__()
        self.items = [1000]
