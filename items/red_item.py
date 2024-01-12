from items.item import Item


class RedItem(Item):

    def __init__(self):
        super().__init__()
        self.items = [150, 200, 250, 300, 350, 400, 450, 500]
        self.items_and_pictures = {
            150: "img/red_item_150_rub",
            200: "img/red_item_200_rub",
            250: "img/red_item_250_rub",
            300: "img/red_item_300_rub",
            350: "img/red_item_350_rub",
            400: "img/red_item_400_rub",
            450: "img/red_item_450_rub",
            500: "img/red_item_500_rub"
        }
