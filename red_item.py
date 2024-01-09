from item import Item


class RedItem(Item):

    def __init__(self):
        super().__init__()
        self.items = [150, 200, 250, 300, 350, 400, 450, 500]
