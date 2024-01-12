from threading import Thread, enumerate
from time import sleep
from random import choice
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror
from game import Game


class MainWindow(Tk):

    def __init__(self, player):
        super().__init__()

        self.title("MoneyRoll")
        self.geometry("600x400")

        self.images_for_roll = []


        self.default_image = StringVar()
        self.default_image.set("../img/blue_item_5_rub.png")
        self.current_win = 0
        self.current_win_var = StringVar()
        self.current_win_var.set("")

        self.player = player
        self.play_btn = None
        self.canvas = None
        self.img = None
        self.this_game = Game(self.player)

        self.users_curr_balance = StringVar()
        self.users_curr_balance.set(f"Баланс: {self.player.get_balance()} рублей")

        # player's info section
        player_info_frame = Frame(self, borderwidth=1, relief=SOLID)
        player_info_frame.pack(anchor=NW)
        balance_lbl = ttk.Label(player_info_frame, textvariable=self.users_curr_balance)
        balance_lbl.pack(pady=(20, 10), padx=20)
        increase_balance_btn = Button(player_info_frame, text="Пополнить")
        increase_balance_btn.pack(pady=(0, 20))

        # pictures
        self.canvas = Canvas(self, width=300, height=300)
        self.canvas.pack()
        self.img = PhotoImage(file=self.default_image.get())
        self.canvas.create_image(20, 20, anchor=NW, image=self.img)

        # win text
        current_win_lbl = ttk.Label(self, textvariable=self.current_win_var)
        current_win_lbl.pack()

        # main button
        self.play_btn = Button(self, text="Испытать удачу", command=self.play_btn_action)
        self.play_btn.pack()

    def play_btn_action(self):
        if self.player.get_balance() - 50 < 0:
            showerror(title="Вы дебил", message="Вы лудоман и вы слили весь баланс. "
                                                "Чтобы играть дальше, сделайте пополнение!")
            return
        self.play_btn.configure(state=DISABLED)
        prize = self.this_game.get_prize()
        self.current_win = prize[0]
        self.users_curr_balance.set(f"Баланс: {self.player.get_balance()} рублей")
        self.images_for_roll = self._create_list_of_pictures()
        self.images_for_roll.append(prize[1])
        self._change_pictures()
        self.current_win = prize[0]
        print(self.player.first_name)
        print(self.player.get_balance())

    def _change_pictures(self):
        thread = Thread(target=self.change_mechanic, daemon=True)
        thread.start()

    def change_mechanic(self):

        image_files = self.images_for_roll

        for image in image_files:
            self.img = PhotoImage(file=f"../{image}.png")
            self.canvas.create_image(20, 20, anchor=NW, image=self.img)
            sleep(0.1)

        self.play_btn.configure(state=NORMAL)
        self.current_win_var.set(f"Вы выиграли {self.current_win} рублей!")
        self.player.increase_balance(self.current_win)
        self.users_curr_balance.set(f"Баланс: {self.player.get_balance()} рублей")

    @staticmethod
    def print_active_threads():
        active_threads = enumerate()
        for thread in active_threads:
            print(thread.name)

    @staticmethod
    def _create_list_of_pictures(count=9):
        all_pictures = ["img/blue_item_1_rub", "img/blue_item_5_rub", "img/blue_item_10_rub", "img/blue_item_15_rub",
                        "img/dark_purple_item_20_rub", "img/dark_purple_item_25_rub", "img/dark_purple_item_30_rub",
                        "img/dark_purple_item_35_rub", "img/dark_purple_item_40_rub", "img/purple_item_45_rub",
                        "img/purple_item_50_rub", "img/purple_item_55_rub", "img/purple_item_65_rub",
                        "img/purple_item_75_rub", "img/purple_item_85_rub", "img/purple_item_95_rub",
                        "img/purple_item_100_rub", "img/red_item_150_rub", "img/red_item_200_rub",
                        "img/red_item_250_rub", "img/red_item_300_rub", "img/red_item_350_rub", "img/red_item_400_rub",
                        "img/red_item_450_rub", "img/red_item_500_rub", "img/golden_item_1000_rub"]
        result_list = [choice(all_pictures) for i in range(9)]
        return result_list


def main():
    main_window = MainWindow()
    main_window.mainloop()


if __name__ == '__main__':
    main()

