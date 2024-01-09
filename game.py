from random import random
from golden_item import GoldenItem
from red_item import RedItem
from purple_item import PurpleItem
from dark_purple import DarkPurpleItem
from blue_item import BlueItem
# from main import current_win_label, total_win_label


class Game:

    def __init__(self):
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

    def run(self):

        item = self._choose_item()
        self.total -= 50
        self.total += item

        bad_result = f'Вы в МИНУСЕ на {self.total * -1} рублей. Позор, лудоман!'
        good_result = f'Вы в ПЛЮСЕ на {self.total} рублей.'
        text = f'Вы выиграли {item} рублей! Поздравляем!\n\n{bad_result if self.total < 0 else good_result}\n\n'


        self.current_win_text = f"Поздравляем! Вы выиграли {item} рублей."





    def start(self):

        count_for_test = 0

        while True:
            bad_result = f'Вы в МИНУСЕ на {self.total * -1} рублей. Позор, лудоман!'
            good_result = f'Вы в ПЛЮСЕ на {self.total} рублей.'
            text = f'{bad_result if self.total < 0 else good_result} \n\n1. Крутить \n2. Закончить игру \n\nВаш ответ: '



            # if count_for_test < 10:
            #     answer = '1'
            #     count_for_test += 1
            # else:
            #     answer = input(text)

            if answer == '2':
                return

            if answer == '1':
                item = self._choose_item()
                self.total -= 50
                self.total += item
                print(f'Вы выиграли {item} рублей')


if __name__ == '__main__':
    game = Game()
    game.start()
