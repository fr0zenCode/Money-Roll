from random import random

import items.blue_item as blue_item
import items.dark_purple_item as dark_purple_item
import items.purple_item as purple_item
import items.red_item as red_item
import items.golden_item as golden_item


class Game:

    def __init__(self, player):
        self.player = player

    @staticmethod
    def _make_drop(item_type_object):
        sup_object = item_type_object()
        item_object = sup_object.get()
        return item_object

    def _choose_item(self):

        chance = random() * 100

        if chance <= 0.05:
            return self._make_drop(golden_item.GoldenItem)
        if 0.05 < chance <= 0.20:
            return self._make_drop(red_item.RedItem)
        if 0.20 < chance <= 2:
            return self._make_drop(purple_item.PurpleItem)
        if 2 < chance <= 10:
            return self._make_drop(dark_purple_item.DarkPurpleItem)

        return self._make_drop(blue_item.BlueItem)

    def get_prize(self):
        item = self._choose_item()
        self.player.take_money_for_game()
        return item


if __name__ == '__main__':
    pass
