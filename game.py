from random import random

from items.golden_item import GoldenItem
from items.red_item import RedItem
from items.purple_item import PurpleItem
from items.dark_purple_item import DarkPurpleItem
from items.blue_item import BlueItem


class Game:

    def __init__(self, player):
        self.player = player
        self.total = 0
        self.total_win_text = ""
        self.current_win_text = ""

    @staticmethod
    def _make_drop(item_type_object):
        sup_object = item_type_object()
        item_object = sup_object.get()
        return item_object

    def _choose_item(self):

        chance = random() * 100

        if chance <= 0.05:
            return self._make_drop(GoldenItem)
        if 0.05 < chance <= 0.20:
            return self._make_drop(RedItem)
        if 0.20 < chance <= 2:
            return self._make_drop(PurpleItem)
        if 2 < chance <= 10:
            return self._make_drop(DarkPurpleItem)

        return self._make_drop(BlueItem)

    def get_prize(self):

        item = self._choose_item()
        self.player.take_money_for_game()
        self.total += item[0]
        self.current_win_text = f"Поздравляем! Вы выиграли {item} рублей."

        return item


if __name__ == '__main__':
    game = Game("player")
    game.run()
