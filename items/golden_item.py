from items.item import Item


class GoldenItem(Item):

    def __init__(self):
        super().__init__()
        self.items = [1000]
        self.items_and_pictures = {1000: "img/golden_item_1000_rub.png"}
