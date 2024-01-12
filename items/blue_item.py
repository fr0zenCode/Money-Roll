from items.item import Item


class BlueItem(Item):

    def __init__(self):
        super().__init__()
        self.items = [1, 5, 10, 15]
        self.items_and_pictures = {
            1: "img/blue_item_1_rub",
            5: "img/blue_item_5_rub",
            10: "img/blue_item_10_rub",
            15: "img/blue_item_15_rub"
        }


if __name__ == '__main__':
    blue_item = BlueItem()
    print(blue_item.get())
