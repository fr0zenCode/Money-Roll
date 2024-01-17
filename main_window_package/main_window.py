import _tkinter
from threading import Thread, enumerate
from time import sleep
from random import choice
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror

import main_window_package.game as game
from user_package.user import User

import user_package.account_page as account_page

import user_package.top_up_the_balance_page as tup_up_the_balance_page
import authorization.functions as functions


class MainWindow(Tk):

    def __init__(self, player):
        super().__init__()

        self.title("MoneyRoll")
        self.state("zoomed")

        # screen sizes
        self.percentage_width_from_full_hd = functions.get_percentage_of_screen_size_from_full_hd_size(self)[0] / 100
        self.percentage_height_from_full_hd = functions.get_percentage_of_screen_size_from_full_hd_size(self)[1] / 100

        self.minsize(int(451 * self.percentage_width_from_full_hd), int(451 * self.percentage_height_from_full_hd))

        self.images_for_roll = []

        self.default_image = StringVar()

        self.default_image.set("../img/blue_item_5_rub.png")

        self.current_win = 0
        self.current_win_var = StringVar()
        self.current_win_var.set("")

        # current user_package (player)
        self.player = player

        self.canvas = None
        self.img = None
        self.this_game = game.Game(self.player)

        self.users_curr_balance = StringVar()
        self.users_curr_balance.set(f"Баланс: {self.player.get_balance()} рублей")

        # account section
        ###############################################################################################################
        account_button_frame = Frame(
            self,
            width=int(50 * self.percentage_height_from_full_hd),
            height=int(50 * self.percentage_height_from_full_hd)
        )
        account_button_frame.place(relx=0, rely=0, anchor=NW)

        account_btn = Button(account_button_frame, text="ACC", command=self.account_btn_action)
        account_btn.place(relx=0.5, rely=0.5, anchor=CENTER)
        ###############################################################################################################

        # balance section
        ###############################################################################################################
        player_info_frame = Frame(
            self,
            borderwidth=1,
            relief=SOLID,
            width=int(150 * self.percentage_width_from_full_hd),
            height=int(50 * self.percentage_height_from_full_hd)
        )
        player_info_frame.place(relx=0.03, rely=0, anchor=NW)

        increase_balance_btn = Button(player_info_frame, text="Пополнить", command=self.top_up_the_balance_btn_action)
        increase_balance_btn.place(relx=0.5, rely=0.25, anchor=CENTER)

        balance_lbl_frame = Frame(
            player_info_frame,
            width=int(120 * self.percentage_width_from_full_hd),
            height=int(20 * self.percentage_height_from_full_hd)
        )
        balance_lbl_frame.place(relx=0.5, rely=0.75, anchor=CENTER)

        balance_lbl = ttk.Label(balance_lbl_frame, textvariable=self.users_curr_balance)
        balance_lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

        ###############################################################################################################

        # pictures
        self.canvas = Canvas(self, width=300, height=300)
        self.canvas.pack()
        try:
            self.img = PhotoImage(file=self.default_image.get())
        except _tkinter.TclError:
            self.img = PhotoImage(file="../img/purple_item_45_rub.png")
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

        self.mainloop()

    def _change_pictures(self):
        thread = Thread(target=self.change_mechanic, daemon=True)
        thread.start()


    def change_mechanic(self):

        image_files = self.images_for_roll

        for image in image_files:
            try:
                self.img = PhotoImage(file=f"../{image}.png")
            except _tkinter.TclError:
                self.img = PhotoImage(file=f"{image}.png")
            self.canvas.create_image(20, 20, anchor=NW, image=self.img)
            sleep(0.1)

        self.play_btn.configure(state=NORMAL)
        self.current_win_var.set(f"Вы выиграли {self.current_win} рублей!")
        self.player.increase_balance(self.current_win)
        self.users_curr_balance.set(f"Баланс: {self.player.get_balance()} рублей")

        self.mainloop()

    def account_btn_action(self):
        player = self.player
        self.destroy()
        account_page.AccountPage(player)

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

    def top_up_the_balance_btn_action(self):
        player = self.player
        self.destroy()
        top_up_the_balance_page = tup_up_the_balance_page.TopUpTheBalancePage(player)
        top_up_the_balance_page.mainloop()


def main():
    player = User(
        'Login',
        "user_id",
        "first_name",
        "last_name",
        "email",
        "password",
        1000,
        0
    )
    main_window = MainWindow(player)
    main_window.mainloop()


if __name__ == '__main__':
    main()

