from time import sleep
from random import choice

import _tkinter
import threading

from PIL import Image, ImageTk

import tkinter as tk
from tkinter.messagebox import showerror
import customtkinter as ctk

import connection
import main_window_package.game as game
import authorization.authorization_page as authorization_page
from user_package.user import User

import user_package.account_page as account_page

import user_package.top_up_the_balance_page as tup_up_the_balance_page

from settings import user as db_user, password as db_password, database as db_name, background_color, areas_background


class MainWindow(ctk.CTk):

    def __init__(self, player):
        super().__init__()

        self.title("MoneyRoll")

        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        self.minsize(int(self.screen_width / 1.7), int(self.screen_height / 1.7))

        self.images_for_roll = []
        self.image = tk.StringVar()
        self.image.set("../img/items/default_item.png")

        self.configure(fg_color=background_color)

        self.buttons_background = "#4A6AE9"
        self.buttons_hover_background = "#C34FF2"
        self.buttons_border_color = "white"

        self.current_win = 0
        self.current_win_var = tk.StringVar()
        self.current_win_var.set("")

        # current user_package (player)
        self.player = player
        self.connection = connection.Connection()
        self.resized_account_small_logo = None

        self.canvas = None
        self.img = None
        self.this_game = game.Game(self.player)

        self.users_curr_balance = tk.StringVar()
        self.users_curr_balance.set(f"Баланс: {self.player.get_balance()} рублей")

        # account section
        ###############################################################################################################
        account_button_frame = ctk.CTkFrame(self, fg_color=background_color)
        account_button_frame.place(relx=0.005, rely=0.005, anchor=tk.NW, relwidth=0.06, relheight=0.1)

        self.account_btn = ctk.CTkButton(
            account_button_frame,
            command=self.account_btn_action,
            text="""Личный
кабинет""",
            fg_color=self.buttons_background,
            hover_color="#662C4C",
            border_width=1,
            border_color="grey"
        )

        self.account_btn.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=0.9, relheight=0.9)
        ###############################################################################################################

        # balance section
        ###############################################################################################################
        player_info_frame = ctk.CTkFrame(
            self,
            border_width=1,
            border_color="white",
            fg_color=background_color
        )
        player_info_frame.place(relx=0.07, rely=0.005, anchor=tk.NW, relwidth=0.1, relheight=0.1)

        increase_balance_btn = ctk.CTkButton(
            player_info_frame,
            text="Пополнить",
            border_width=1,
            border_color="white",
            fg_color=self.buttons_background,
            hover_color=self.buttons_hover_background,
            command=self.top_up_the_balance_btn_action
        )
        increase_balance_btn.place(relx=0.5, rely=0.1, anchor=tk.N, relwidth=0.8, relheight=0.4)

        self.balance_lbl = ctk.CTkLabel(player_info_frame, textvariable=self.users_curr_balance, font=("Arial", 12))
        if self.player.get_balance() >= 50:
            self.balance_lbl.configure(text_color="#51DAE5")
        else:
            self.balance_lbl.configure(text_color="#E71C60")

        self.balance_lbl.place(relx=0.5, rely=0.95, anchor=tk.S, relwidth=0.98, relheight=0.4)
        ###############################################################################################################

        # game frame
        ###############################################################################################################
        game_frame = ctk.CTkFrame(self, fg_color=background_color)
        game_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=0.6, relheight=0.85)

        picture_frame = ctk.CTkFrame(game_frame, fg_color="#483283")
        picture_frame.place(relx=0, rely=0, anchor="nw", relwidth=1, relheight=0.5)

        # pictures
        self.canvas = tk.Canvas(master=picture_frame, bd=0, highlightthickness=2)
        self.canvas.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.6, relheight=0.8)
        self.canvas.bind("<Configure>", self.stretch_image)

        self.resized_tk = None

        try:
            self.image_original = Image.open(self.image.get())
        except _tkinter.TclError:
            self.image_original = Image.open("../img/items/default_item.png")
        self.canvas.create_image(0, 0, anchor="nw", image=self.img)

        ui_frame = ctk.CTkFrame(game_frame, fg_color=background_color)
        ui_frame.place(relx=0, rely=0.5, anchor="nw", relwidth=1, relheight=0.5)

        # win text
        self.current_win_lbl = ctk.CTkLabel(
            ui_frame,
            textvariable=self.current_win_var,
            text_color="white",
            font=("Arial", 25),
            fg_color=areas_background
        )
        self.current_win_lbl.place(relx=0.5, rely=0.1, anchor="n", relwidth=0.5, relheight=0.3)

        # main button
        self.play_btn = ctk.CTkButton(
            ui_frame,
            text="Испытать удачу",
            command=self.play_btn_action,
            font=("Arial", 25),
            fg_color="#4A6AE9",
            border_width=2,
            border_color="white",
            hover_color="#C34FF2"
        )
        self.play_btn.place(relx=0.5, rely=0.5, anchor="n", relwidth=0.5, relheight=0.3)
        ###############################################################################################################

    def stretch_image(self, event):

        width = event.width
        height = event.height

        resized_image = self.image_original.resize((width, height))
        self.resized_tk = ImageTk.PhotoImage(resized_image)

        self.canvas.create_image(0, 0, image=self.resized_tk, anchor="nw")

    def play_btn_action(self):

        if self.connection.get_connection() is None:
            self.connection.make_connection(user=db_user, password=db_password, database=db_name)

        self.current_win_var.set("")
        if self.player.get_balance() - 50 < 0:
            showerror(title="Вы дебил", message="Вы лудоман и вы слили весь баланс. "
                                                "Чтобы играть дальше, сделайте пополнение!")
            return
        self.play_btn.configure(state=tk.DISABLED)
        prize = self.this_game.get_prize()
        self.current_win = prize[0]
        self.users_curr_balance.set(f"Баланс: {self.player.get_balance()} рублей")
        self.images_for_roll = self._create_list_of_pictures()
        self.images_for_roll.append(prize[1])
        self._change_pictures()
        self.current_win = prize[0]
        if self.player.get_balance() >= 50:
            self.balance_lbl.configure(text_color="#51DAE5")
        else:
            self.balance_lbl.configure(text_color="#E71C60")

    def _change_pictures(self):
        thread = threading.Thread(target=self.change_mechanic, daemon=True)
        thread.start()

    def change_mechanic(self):

        images = self.images_for_roll

        image_width = self.canvas.winfo_width()
        image_heigth = self.canvas.winfo_height()

        for image in images:
            try:
                self.image_original = Image.open(f"../{image}.png")
                resized_image = self.image_original.resize((image_width, image_heigth))
                self.resized_tk = ImageTk.PhotoImage(resized_image)
                self.canvas.create_image(0, 0, image=self.resized_tk, anchor="nw")
                sleep(0.16)
                image_width = self.canvas.winfo_width()
                image_heigth = self.canvas.winfo_height()
                print(image_width, image_heigth)
            except _tkinter.TclError:

                self.image_original = Image.open(f"{image}.png")
                resized_image = self.image_original.resize((image_width, image_heigth))
                self.resized_tk = ImageTk.PhotoImage(resized_image)

                self.canvas.create_image(0, 0, image=self.resized_tk, anchor="nw")
                image_width = self.canvas.winfo_width()
                image_heigth = self.canvas.winfo_height()
                print(image_width, image_heigth)
                sleep(0.16)

        self.play_btn.configure(state=tk.NORMAL)

        if self.current_win in (1, 5, 10, 15):
            self.current_win_lbl.configure(text_color="#70CBFF")
        elif self.current_win in (20, 25, 30, 35, 40):
            self.current_win_lbl.configure(text_color="#8B258D")
        elif self.current_win in (45, 50, 55, 65, 75, 85, 95, 100):
            self.current_win_lbl.configure(text_color="#D700B5")
        elif self.current_win in (150, 200, 250, 300, 350, 400, 450, 500):
            self.current_win_lbl.configure(text_color="white")
        elif self.current_win == 1000:
            self.current_win_lbl.configure(text_color="#D0AA45")

        if self.current_win is 1:
            postfix = "рубль!"
        else:
            postfix = "рублей!"

        self.current_win_var.set(f"Вы выиграли {self.current_win} {postfix}")

        self.player.increase_balance(self.current_win)
        self.users_curr_balance.set(f"Баланс: {self.player.get_balance()} рублей")
        if self.player.get_balance() >= 50:
            self.balance_lbl.configure(text_color="#51DAE5")
        else:
            self.balance_lbl.configure(text_color="#E71C60")

        self.connection.get_cursor().execute(f"""
        UPDATE "authorization-data" 
        SET balance = '{self.player.get_balance()}' 
        WHERE login = '{self.player.login}' 
        AND password = '{self.player.get_password()}' 
        AND email = '{self.player.user_email}';""")
        self.connection.get_connection().commit()

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
        all_pictures = ["img/items/blue_item_1_rub", "img/items/blue_item_5_rub", "img/items/blue_item_10_rub",
                        "img/items/blue_item_15_rub", "img/items/dark_purple_item_20_rub",
                        "img/items/dark_purple_item_25_rub", "img/items/dark_purple_item_30_rub",
                        "img/items/dark_purple_item_35_rub", "img/items/dark_purple_item_40_rub",
                        "img/items/purple_item_45_rub", "img/items/purple_item_50_rub", "img/items/purple_item_55_rub",
                        "img/items/purple_item_65_rub", "img/items/purple_item_75_rub", "img/items/purple_item_85_rub",
                        "img/items/purple_item_95_rub", "img/items/purple_item_100_rub", "img/items/red_item_150_rub",
                        "img/items/red_item_200_rub", "img/items/red_item_250_rub", "img/items/red_item_300_rub",
                        "img/items/red_item_350_rub", "img/items/red_item_400_rub", "img/items/red_item_450_rub",
                        "img/items/red_item_500_rub", "img/items/golden_item_1000_rub"]
        result_list = [choice(all_pictures) for i in range(count)]
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
        200,
        0
    )
    main_window = MainWindow(player)
    main_window.mainloop()


if __name__ == '__main__':
    main()
