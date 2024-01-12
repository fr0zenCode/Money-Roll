from items.item import Item


class PurpleItem(Item):

    def __init__(self):
        super().__init__()
        self.items = [45, 50, 55, 65, 75, 85, 95, 100]
        self.items_and_pictures = {
            45: "img/purple_item_45_rub",
            50: "img/purple_item_50_rub",
            55: "img/purple_item_55_rub",
            65: "img/purple_item_65_rub",
            75: "img/purple_item_75_rub",
            85: "img/purple_item_85_rub",
            95: "img/purple_item_95_rub",
            100: "img/purple_item_100_rub"
        }
        