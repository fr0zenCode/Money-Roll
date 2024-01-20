from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk

import connection
from settings import (background_color, buttons_background_color, buttons_hover_background_color, areas_background,
                      user as db_user, password as db_password, database as db_name)

import user_package.user as user
import main_window_package.main_window as main_window


class AccountPageMainFrame(ctk.CTkFrame):

    def __init__(self, master, player: user.User):
        super().__init__(master)

        self.player = player
        self.connection = connection.Connection()

        self.image_original = Image.open("../img/avatars/default_avatar_image.jpg")
        self.resized_tk = None

        # main frame
        ###############################################################################################################
        content_frame = ctk.CTkFrame(master, fg_color=background_color)
        content_frame.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=1, relheight=1)
        ###############################################################################################################

        upper_frame = ctk.CTkFrame(content_frame, fg_color=background_color)
        upper_frame.place(relx=0, rely=0.05, relwidth=1, relheight=0.8)

        avatar_frame = ctk.CTkFrame(upper_frame, fg_color=background_color)
        avatar_frame.place(relx=0.05, rely=0, relwidth=0.27, relheight=1)

        photo_frame = ctk.CTkFrame(avatar_frame, fg_color=background_color)
        photo_frame.place(relwidth=1, relheight=0.75)

        self.canvas = Canvas(photo_frame, background="white", bd=0, highlightthickness=0, relief=RIDGE)
        self.canvas.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.99, relheight=0.99)
        self.canvas.bind("<Configure>", self.stretch_image)

        # combobox
        self.items_for_combobox = ("<Выберите аватар>", "Озорник", "Лудоман", "Плохой парень", "MoneyRoll")
        self.combobox_variable, self.combobox_for_avatars = self.create_combobox(avatar_frame, self.items_for_combobox)

        # user's data
        users_data_frame = ctk.CTkFrame(upper_frame, fg_color=background_color)
        users_data_frame.place(relx=0.33, rely=0, relwidth=0.67, relheight=1, anchor=NW)

        self.first_name_variable = StringVar(value=self.player.first_name)
        self.last_name_variable = StringVar(value=self.player.last_name)
        self.current_password_variable = StringVar(value="")
        self.new_password_variable = StringVar(value="")
        self.confirm_new_password_variable = StringVar(value="")

        self.first_name_frame, self.first_name_ent = self.create_entry(users_data_frame, "Имя:", background_color)
        self.first_name_frame.place(relx=0.5, rely=0, anchor="n", relwidth=1, relheight=0.1)
        self.first_name_ent.configure(textvariable=self.first_name_variable)

        self.last_name_frame, self.last_name_ent = self.create_entry(users_data_frame, "Фамилия:", background_color)
        self.last_name_frame.place(relx=0.5, rely=0.2, anchor="n", relwidth=1, relheight=0.1)
        self.last_name_ent.configure(textvariable=self.last_name_variable)

        self.current_password_frame, self.current_password_ent = self.create_entry(users_data_frame, "Пароль:",
                                                                                   background_color)
        self.current_password_frame.place(relx=0.5, rely=0.4, anchor="n", relwidth=1, relheight=0.1)
        self.current_password_ent.configure(textvariable=self.current_password_variable)

        self.new_password_frame, self.new_password_ent = self.create_entry(users_data_frame, "Новый пароль:",
                                                                           background_color)
        self.new_password_frame.place(relx=0.5, rely=0.6, anchor="n", relwidth=1, relheight=0.1)
        self.new_password_ent.configure(textvariable=self.new_password_variable)

        self.confirm_new_password_frame, self.confirm_new_password_ent = self.create_entry(users_data_frame,
                                                                                           "Подтверждение пароля:",
                                                                                           background_color)
        self.confirm_new_password_frame.place(relx=0.5, rely=0.8, anchor="n", relwidth=1, relheight=0.1)
        self.confirm_new_password_ent.configure(textvariable=self.confirm_new_password_variable)

        # buttons
        self.cancel_btn, self.submit_btn = self.create_ok_and_cancel_buttons(content_frame)

    def stretch_image(self, event):

        width = event.width
        height = event.height

        resized_image = self.image_original.resize((width, height))
        self.resized_tk = ImageTk.PhotoImage(resized_image)

        self.canvas.create_image(0, 0, image=self.resized_tk, anchor=NW)

    def create_ok_and_cancel_buttons(self, parent_frame):

        bottom_frame = ctk.CTkFrame(parent_frame, fg_color=background_color)
        bottom_frame.place(relx=0, rely=0.85, anchor=NW, relwidth=1, relheight=0.15)

        buttons_frame = ctk.CTkFrame(bottom_frame, fg_color=background_color)
        buttons_frame.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.3, relheight=0.5)

        cancel_btn = ctk.CTkButton(
            buttons_frame,
            text="Отмена",
            corner_radius=10,
            fg_color=buttons_background_color,
            hover_color=buttons_hover_background_color,
            border_width=2,
            border_color="red",
            command=self.cancel_btn_action
        )

        submit_btn = ctk.CTkButton(
            buttons_frame,
            text="Принять",
            corner_radius=10,
            fg_color=buttons_background_color,
            hover_color=buttons_hover_background_color,
            border_width=2,
            border_color="green",
            command=self.submit_btn_action
        )

        cancel_btn.place(relx=0, rely=0.5, anchor=W, relwidth=0.45, relheight=1)
        submit_btn.place(relx=1, rely=0.5, anchor=E, relwidth=0.45, relheight=1)

        return cancel_btn, submit_btn

    def cancel_btn_action(self):
        player = self.player
        self.master.destroy()
        main_window_page = main_window.MainWindow(player)
        main_window_page.mainloop()

    def submit_btn_action(self):

        if self.current_password_ent.get() != self.player.get_password():
            print("Неверный пароль!")
            return False

        if self.new_password_ent.get() != self.confirm_new_password_ent.get():
            print("Пароли не совпадают!")
            return False

        if self.first_name_ent.get() != self.player.first_name or self.last_name_ent.get() != self.player.last_name:
            if self.connection.get_connection() is None:
                self.connection.make_connection(user=db_user, password=db_password, database=db_name)
                self.connection.get_cursor().execute(f"""
                UPDATE "authorization-data" 
                SET 
                    first_name = '{self.first_name_ent.get()}', last_name = '{self.last_name_ent.get()}'
                WHERE
                    login = '{self.player.login}' 
                    AND password = '{self.player.get_password()}' 
                    AND email = '{self.player.user_email}';
                """)

        if self.new_password_ent.get() == self.confirm_new_password_ent.get() != self.current_password_ent.get() != "":
            if self.connection.get_connection() is None:
                self.connection.make_connection(user=db_user, password=db_password, database=db_name)
                self.connection.get_cursor().execute(f"""
                UPDATE "authorization-data"
                SET
                    password = '{self.new_password_ent.get()}'
                WHERE
                    login = '{self.player.login}'
                    AND password = '{self.player.get_password()}'
                    AND email = '{self.player.user_email}';
                """)
        self.connection.get_connection().commit()
        self.connection.get_connection().close()

    def create_combobox(self, parent, items: list | tuple):

        photo_selector_frame = ctk.CTkFrame(parent, fg_color=background_color)
        photo_selector_frame.place(relx=0, rely=1, relwidth=1, relheight=0.25, anchor=SW)

        combobox_variable = StringVar()
        combobox_variable.set(items[0])

        photo_selector_combobox = ctk.CTkComboBox(
            photo_selector_frame,
            variable=combobox_variable,
            values=items,
            justify="center",
            command=self.combobox_action
        )

        photo_selector_combobox.place(relx=0.5, rely=0.15, anchor=CENTER, relwidth=0.5, relheight=0.15)

        return combobox_variable, photo_selector_combobox

    def combobox_action(self, value):

        image = ""

        if value == "<Выберите аватар>":
            pass
        if value == "Лудоман":
            image = "../img/avatars/ludoman.png"
        if value == "Озорник":
            image = "../img/avatars/funny_man.png"
        if value == "Плохой парень":
            image = "../img/avatars/bad_boy.png"
        if value == "MoneyRoll":
            image = "../img/avatars/default_avatar_image.jpg"

        self.image_original = Image.open(image)
        resized_image = self.image_original.resize((self.canvas.winfo_width(), self.canvas.winfo_height()))

        self.resized_tk = ImageTk.PhotoImage(resized_image)
        self.canvas.create_image(0, 0, image=self.resized_tk, anchor=NW)

    @staticmethod
    def create_entry(parent_frame, text, bg_color):
        frame = ctk.CTkFrame(parent_frame, fg_color=background_color)
        frame_lbl = ctk.CTkLabel(frame, text=text, bg_color=bg_color)
        frame_ent = ctk.CTkEntry(frame, bg_color=bg_color, justify=CENTER)
        frame_lbl.place(relx=0.1, rely=0.5, anchor=W, relwidth=0.5, relheight=0.5)
        frame_ent.place(relx=0.6, rely=0.5, anchor=W, relwidth=0.3, relheight=0.5)
        return frame, frame_ent
