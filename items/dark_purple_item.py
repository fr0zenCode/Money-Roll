from items.item import Item


class DarkPurpleItem(Item):

    def __init__(self):
        super().__init__()
        self.items = [20, 25, 30, 35, 40]
        self.items_and_pictures = {
            20: "img/dark_purple_item_20_rub",
            25: "img/dark_purple_item_25_rub",
            30: "img/dark_purple_item_30_rub",
            35: "img/dark_purple_item_35_rub",
            40: "img/dark_purple_item_40_rub"
        }
