from tkinter import *
from tkinter import ttk
import tkinter.font as TkFont

from PIL import Image, ImageTk

import authorization.functions as functions
import user_package.user as user


class AccountPage(Tk):

    def __init__(self, player):
        super().__init__()

        self.player = player

        self.title("Аккаунт")
        self.state("zoomed")

        # screen sizes
        self.percentage_width_from_full_hd = functions.get_percentage_of_screen_size_from_full_hd_size(self)[0] / 100
        self.percentage_height_from_full_hd = functions.get_percentage_of_screen_size_from_full_hd_size(self)[1] / 100

        self.minsize(int(451 * self.percentage_width_from_full_hd), int(451 * self.percentage_height_from_full_hd))

        # fonts
        self.font_for_lbl = TkFont.Font(
            family="Arial",
            size=(11 * int((self.percentage_width_from_full_hd + self.percentage_height_from_full_hd) / 2))
        )

        # main frame
        ###############################################################################################################
        content_frame = Frame(
            background="green",
            width=int(400 * self.percentage_width_from_full_hd),
            height=int(300 * self.percentage_height_from_full_hd)
        )
        content_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        ###############################################################################################################

        # player's photo frame
        ###############################################################################################################
        photo_frame = Frame(
            content_frame,
            background="blue",
            width=int(130 * self.percentage_width_from_full_hd),
            height=int(160 * self.percentage_height_from_full_hd)
        )
        photo_frame.place(relx=0.04, rely=0.05, anchor=NW)

        # string var for photo selector
        self.photo_variant_string = StringVar()
        self.photo_variant_string.set("../img/log_in_logo.png")

        self.img = Image.open(self.photo_variant_string.get())
        self.resized_image = self.img.resize((
            int(110 * self.percentage_width_from_full_hd),
            int(150 * self.percentage_height_from_full_hd))
        )
        self.new_image = ImageTk.PhotoImage(self.resized_image)

        self.label_avatar = ttk.Label(photo_frame, image=self.new_image)
        self.label_avatar.place(relx=0.5, rely=0.5, anchor=CENTER)
        ###############################################################################################################

        # photo selector frame
        ###############################################################################################################
        photo_selector_frame = Frame(
            content_frame,
            background="yellow",
            width=int(120 * self.percentage_width_from_full_hd),
            height=int(50 * self.percentage_height_from_full_hd)
        )
        photo_selector_frame.place(relx=0.19, rely=0.7, anchor=CENTER)

        self.photo_variants = ("<Выберите аватар>", "Лудоман", "Озорник", "Плохой парень")
        self.combobox_variable = StringVar()
        self.combobox_variable.set(self.photo_variants[0])
        self.photo_selector_combobox = ttk.Combobox(photo_selector_frame, textvariable=self.combobox_variable)
        self.photo_selector_combobox["values"] = self.photo_variants
        self.photo_selector_combobox.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.photo_selector_combobox.bind(
            "<<ComboboxSelected>>",
            lambda event: self.photo_selector_action(self.combobox_variable.get())
        )
        ###############################################################################################################

        # user info frame
        ###############################################################################################################
        ###############################################################################################################

        user_info_frame = Frame(
            content_frame,
            background="yellow",
            width=int(220 * self.percentage_width_from_full_hd),
            height=int(200 * self.percentage_height_from_full_hd)
        )
        user_info_frame.place(relx=0.675, rely=0.42, anchor=CENTER)
        user_info_frame.pack_propagate(False)

        # first name frame
        ###############################################################################################################
        first_name_frame = Frame(
            user_info_frame,
            width=int(220 * self.percentage_width_from_full_hd),
            height=int(50 * self.percentage_height_from_full_hd),
            background="blue"
        )
        first_name_frame.place(relx=0, rely=0.1, anchor=W)
        first_name_frame.pack_propagate(False)

        self.first_name_variable = StringVar(value=self.player.first_name)

        first_name_lbl = ttk.Label(first_name_frame, text="Имя:", font=self.font_for_lbl)
        first_name_lbl.pack(side=LEFT, padx=(0, 10 * self.percentage_width_from_full_hd))
        first_name_ent = ttk.Entry(first_name_frame, font=self.font_for_lbl, textvariable=self.first_name_variable)
        first_name_ent.pack(side=RIGHT)
        ###############################################################################################################
        last_name_frame = Frame(
            user_info_frame,
            width=int(220 * self.percentage_width_from_full_hd),
            height=int(50 * self.percentage_height_from_full_hd),
            background="purple"
        )
        last_name_frame.place(relx=0, rely=0.36, anchor=W)
        last_name_frame.pack_propagate(False)

        self.last_name_variable = StringVar(value=self.player.last_name)

        first_name_lbl = ttk.Label(last_name_frame, text="Фамилия:", font=self.font_for_lbl)
        first_name_lbl.pack(side=LEFT, padx=(0, 10 * self.percentage_width_from_full_hd))
        first_name_ent = ttk.Entry(last_name_frame, font=self.font_for_lbl, textvariable=self.last_name_variable)
        first_name_ent.pack(side=RIGHT)
        ###############################################################################################################
        current_password_frame = Frame(
            user_info_frame,
            width=int(220 * self.percentage_width_from_full_hd),
            height=int(50 * self.percentage_height_from_full_hd),
            background="purple"
        )
        current_password_frame.place(relx=0, rely=(0.36 + 0.26), anchor=W)
        current_password_frame.pack_propagate(False)

        first_name_lbl = ttk.Label(current_password_frame, text="Старый пароль:", font=self.font_for_lbl)
        first_name_lbl.pack(side=LEFT, padx=(0, 10 * self.percentage_width_from_full_hd))
        first_name_ent = ttk.Entry(current_password_frame, font=self.font_for_lbl)
        first_name_ent.pack(side=RIGHT)
        ###############################################################################################################
        new_password_frame = Frame(
            user_info_frame,
            width=int(220 * self.percentage_width_from_full_hd),
            height=int(50 * self.percentage_height_from_full_hd),
            background="purple"
        )
        new_password_frame.place(relx=0, rely=(0.36 + 0.26 + 0.26), anchor=W)
        new_password_frame.pack_propagate(False)

        first_name_lbl = ttk.Label(new_password_frame, text="Новый пароль:", font=self.font_for_lbl)
        first_name_lbl.pack(side=LEFT, padx=(0, 10 * self.percentage_width_from_full_hd))
        first_name_ent = ttk.Entry(new_password_frame, font=self.font_for_lbl)
        first_name_ent.pack(side=RIGHT)
        ###############################################################################################################
        ###############################################################################################################

        # buttons frame
        ###############################################################################################################
        buttons_frame = Frame(
            content_frame,
            background="white",
            width=int(200 * self.percentage_width_from_full_hd),
            height=int(40 * self.percentage_height_from_full_hd)
        )
        buttons_frame.place(relx=0.5, rely=0.89, anchor=CENTER)
        ###############################################################################################################

    def photo_selector_action(self, photos_name):
        self.photo_variant_string = StringVar()
        if photos_name == "Лудоман":
            self.photo_variant_string.set("../img/avatars/ludoman.png")
        elif photos_name == "Озорник":
            self.photo_variant_string.set("../img/avatars/funny_man.png")
        elif photos_name == "Плохой парень":
            self.photo_variant_string.set("../img/avatars/bad_boy.png")

        self.img = Image.open(self.photo_variant_string.get())
        self.resized_image = self.img.resize((
            int(110 * self.percentage_width_from_full_hd),
            int(150 * self.percentage_height_from_full_hd))
        )
        self.new_image = ImageTk.PhotoImage(self.resized_image)

        self.label_avatar.configure(image=self.new_image)


def main():
    player = user.User(
        "TestLogin",
        "50",
        "Petya",
        "Petrov",
        "Petrov@gmail.com",
        "123",
        1000,
        0
    )
    account_page = AccountPage(player)
    account_page.mainloop()


if __name__ == "__main__":
    main()
