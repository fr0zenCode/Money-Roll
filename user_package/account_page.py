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
        self.font_for_lbl = self.create_font_for_lbl(
            10 * (self.percentage_width_from_full_hd + self.percentage_height_from_full_hd) / 2)
        self.font_for_ent = self.font_for_lbl
        self.font_for_combobox = self.font_for_lbl



        # main frame
        ###############################################################################################################
        content_frame = Frame(
            background="green",
            width=int(600 * self.percentage_width_from_full_hd),
            height=int(400 * self.percentage_height_from_full_hd)
        )
        content_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        content_frame.pack_propagate(False)
        ###############################################################################################################

        ###############################################################################################################
        ###############################################################################################################

        upper_frame = Frame(content_frame, background="yellow")
        upper_frame.pack(expand=True, fill=BOTH)





        avatar_frame = Frame(upper_frame, background="red", width=int(250 * self.percentage_width_from_full_hd))
        avatar_frame.pack(side=LEFT, fill=BOTH)
        avatar_frame.pack_propagate(False)




        photo_frame = Frame(avatar_frame, background="blue")
        photo_frame.pack(expand=True, fill=BOTH)
        photo_frame.pack_propagate(False)
        photo_lbl = ttk.Label(photo_frame, text="Photo")
        photo_lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

        photo_selector_frame = Frame(avatar_frame, background="pink")
        photo_selector_frame.pack(fill=BOTH)

        photo_variants = ("<Выберите аватар>", "Лудоман", "Озорник", "Плохой парень")
        combobox_variable = StringVar()
        combobox_variable.set(photo_variants[0])

        photo_selector_combobox = ttk.Combobox(
            photo_selector_frame,
            textvariable=combobox_variable,
            font=self.font_for_combobox
        )
        photo_selector_combobox["values"] = photo_variants
        photo_selector_combobox.pack(pady=(20 * self.percentage_width_from_full_hd, 60 * self.percentage_height_from_full_hd))





        # user's data
        users_data_frame = Frame(upper_frame, background="green")
        users_data_frame.pack(side=LEFT, expand=True, fill=BOTH)
        users_data_frame.pack_propagate(False)

        self.first_name_ent = self.create_entry(users_data_frame, "Имя:", "grey")
        self.last_name_end = self.create_entry(users_data_frame, "Фамилия:", "grey")
        self.current_password_ent = self.create_entry(users_data_frame, "Старый пароль:", "grey")
        self.new_password_end = self.create_entry(users_data_frame, "Новый пароль:", "grey")
        self.confirm_new_password_ent = self.create_entry(users_data_frame, "Подтверждение пароля:",
                                                          "grey")

        # bottom
        ###############################################################################################################
        bottom_frame = Frame(content_frame, background="blue")
        bottom_frame.pack(fill=X)

        buttons_frame = Frame(bottom_frame, background="red")
        buttons_frame.pack(pady=10 * self.percentage_height_from_full_hd)

        cancel_btn = Button(buttons_frame, text="Отмена")
        submit_btn = Button(buttons_frame, text="Принять")
        cancel_btn.pack(side=LEFT, pady=10 * self.percentage_height_from_full_hd)
        submit_btn.pack(side=LEFT, padx=(30 * self.percentage_width_from_full_hd, 0))

        ###############################################################################################################

        ###############################################################################################################
        ###############################################################################################################

        #     # player's photo frame
        #     ###############################################################################################################
        #     photo_frame = Frame(
        #         content_frame,
        #         background="blue",
        #         width=int(130 * self.percentage_width_from_full_hd),
        #         height=int(160 * self.percentage_height_from_full_hd)
        #     )
        #     photo_frame.place(relx=0.04, rely=0.05, anchor=NW)
        #
        #     # string var for photo selector
        #     self.photo_variant_string = StringVar()
        #     self.photo_variant_string.set("../img/log_in_logo.png")
        #
        #     self.img = Image.open(self.photo_variant_string.get())
        #     self.resized_image = self.img.resize((
        #         int(110 * self.percentage_width_from_full_hd),
        #         int(150 * self.percentage_height_from_full_hd))
        #     )
        #     self.new_image = ImageTk.PhotoImage(self.resized_image)
        #
        #     self.label_avatar = ttk.Label(photo_frame, image=self.new_image)
        #     self.label_avatar.place(relx=0.5, rely=0.5, anchor=CENTER)
        #     ###############################################################################################################
        #
        #     # photo selector frame
        #     ###############################################################################################################
        #     photo_selector_frame = Frame(
        #         content_frame,
        #         background="yellow",
        #         width=int(120 * self.percentage_width_from_full_hd),
        #         height=int(50 * self.percentage_height_from_full_hd)
        #     )
        #     photo_selector_frame.place(relx=0.19, rely=0.7, anchor=CENTER)
        #
        #     self.photo_variants = ("<Выберите аватар>", "Лудоман", "Озорник", "Плохой парень")
        #     self.combobox_variable = StringVar()
        #     self.combobox_variable.set(self.photo_variants[0])
        #     self.photo_selector_combobox = ttk.Combobox(photo_selector_frame, textvariable=self.combobox_variable)
        #     self.photo_selector_combobox["values"] = self.photo_variants
        #     self.photo_selector_combobox.place(relx=0.5, rely=0.1, anchor=CENTER)
        #
        #     self.photo_selector_combobox.bind(
        #         "<<ComboboxSelected>>",
        #         lambda event: self.photo_selector_action(self.combobox_variable.get())
        #     )
        #     ###############################################################################################################
        #
        #

    @staticmethod
    def create_font_for_lbl(font_size):
        font = TkFont.Font(family="Arial", size=int(font_size))
        return font

    def create_entry(self, parent_frame, text, bg_color):
        frame = Frame(parent_frame, background=bg_color)
        frame.pack(expand=True, fill=BOTH)
        frame_lbl = ttk.Label(frame, text=text, font=self.font_for_lbl, background=bg_color)
        frame_ent = ttk.Entry(frame, font=self.font_for_ent, background=bg_color)
        frame_lbl.pack(side=LEFT, padx=(10 * self.percentage_width_from_full_hd, 0))
        frame_ent.pack(side=RIGHT, padx=(0, 10 * self.percentage_width_from_full_hd))
        return frame_ent


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
