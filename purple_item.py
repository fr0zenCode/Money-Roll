from item import Item


class PurpleItem(Item):

    def __init__(self):
        super().__init__()
        self.items = [45, 50, 55, 65, 75, 85, 95, 100]
        