from tkinter import *
import customtkinter as ctk

import tkinter.font as tk_font
from PIL import Image, ImageTk

import user_package.user as user
from main_window_package import main_window


class AccountPageMainFrame(ctk.CTkFrame):

    def __init__(self, master, player: user.User):
        super().__init__(master)

        self.player = player

        self.image_original = Image.open("../img/avatars/default_avatar_image.jpg")
        self.resized_tk = None

        # main frame
        ###############################################################################################################
        content_frame = Frame(background="green")
        content_frame.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=1, relheight=1)
        content_frame.pack_propagate(False)
        ###############################################################################################################

        upper_frame = ctk.CTkFrame(content_frame, bg_color="yellow")
        upper_frame.place(relx=0, rely=0, relwidth=1, relheight=0.85)

        avatar_frame = ctk.CTkFrame(upper_frame, bg_color="red")
        avatar_frame.place(relx=0, rely=0, relwidth=0.33, relheight=1)

        photo_frame = ctk.CTkFrame(avatar_frame, bg_color="blue")
        photo_frame.place(relwidth=1, relheight=0.75)

        self.canvas = Canvas(photo_frame, background="white", bd=0, highlightthickness=0, relief=RIDGE)
        self.canvas.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.99, relheight=0.99)
        self.canvas.bind("<Configure>", self.stretch_image)

        # combobox
        self.items_for_combobox = ("<Выберите аватар>", "Озорник", "Лудоман", "Плохой парень")
        self.combobox_variable, self.combobox_for_avatars = self.create_combobox(avatar_frame, self.items_for_combobox)

        # user's data
        users_data_frame = ctk.CTkFrame(upper_frame, bg_color="green")
        users_data_frame.place(relx=0.33, rely=0, relwidth=0.67, relheight=1, anchor=NW)

        self.first_name_variable = StringVar(value=self.player.first_name)
        self.last_name_variable = StringVar(value=self.player.last_name)
        self.current_password_variable = StringVar(value="")
        self.new_password_variable = StringVar(value="")
        self.confirm_new_password_variable = StringVar(value="")

        self.first_name_ent = (self.create_entry(
            users_data_frame,
            "Имя:",
            "grey").configure(textvariable=self.first_name_variable))
        self.last_name_ent = self.create_entry(
            users_data_frame,
            "Фамилия:",
            "grey").configure(textvariable=self.last_name_variable)
        self.current_password_ent = self.create_entry(
            users_data_frame,
            "Старый пароль:",
            "grey").configure(textvariable=self.current_password_variable)
        self.new_password_ent = self.create_entry(
            users_data_frame,
            "Новый пароль:",
            "grey").configure(textvariable=self.new_password_variable)
        self.confirm_new_password_ent = self.create_entry(
            users_data_frame,
            "Подтверждение пароля:",
            "grey").configure(textvariable=self.confirm_new_password_variable)

        # buttons
        self.cancel_btn, self.submit_btn = self.create_ok_and_cancel_buttons(content_frame)

        self.mainloop()

    def stretch_image(self, event):

        width = event.width
        height = event.height

        resized_image = self.image_original.resize((width, height))
        self.resized_tk = ImageTk.PhotoImage(resized_image)

        self.canvas.create_image(0, 0, image=self.resized_tk, anchor=NW)

    def create_ok_and_cancel_buttons(self, parent_frame):
        bottom_frame = Frame(parent_frame, background="blue")
        bottom_frame.place(relx=0, rely=0.85, anchor=NW, relwidth=1, relheight=0.15)

        buttons_frame = Frame(bottom_frame, background="white")
        buttons_frame.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.3, relheight=0.5)

        cancel_btn = ctk.CTkButton(
            buttons_frame,
            text="Отмена",
            corner_radius=10,
            fg_color="red",
            command=self.cancel_btn_action
        )

        submit_btn = ctk.CTkButton(
            buttons_frame,
            text="Принять",
            corner_radius=10,
            fg_color="green",
            command=self.submit_btn_action
        )

        cancel_btn.place(relx=0, rely=0.5, anchor=W, relwidth=0.45, relheight=1)
        submit_btn.place(relx=1, rely=0.5, anchor=E, relwidth=0.45, relheight=1)

        return cancel_btn, submit_btn

    def cancel_btn_action(self):
        player = self.player
        self.master.destroy()
        main.MainWindow(player)

    def submit_btn_action(self):
        pass

    @staticmethod
    def create_combobox(parent, items: list | tuple):

        photo_selector_frame = ctk.CTkFrame(parent, bg_color="pink")
        photo_selector_frame.place(relx=0, rely=1, relwidth=1, relheight=0.25, anchor=SW)

        combobox_variable = StringVar()
        combobox_variable.set(items[0])

        photo_selector_combobox = ctk.CTkComboBox(
            photo_selector_frame,
            variable=combobox_variable,
            values=items,
            justify=CENTER
        )

        photo_selector_combobox.place(relx=0.5, rely=0.2, anchor=CENTER, relwidth=0.5)

        return combobox_variable, photo_selector_combobox

    @staticmethod
    def create_font_for_lbl(font_size):
        font = tk_font.Font(family="Arial", size=int(font_size))
        return font

    @staticmethod
    def create_entry(parent_frame, text, bg_color):
        frame = Frame(parent_frame, background=bg_color)
        frame.pack(expand=True, fill=BOTH)
        frame_lbl = ctk.CTkLabel(frame, text=text, bg_color=bg_color)
        frame_ent = ctk.CTkEntry(frame, bg_color=bg_color, justify=CENTER)
        frame_lbl.place(relx=0.1, rely=0.5, anchor=W, relwidth=0.5, relheight=0.3)
        frame_ent.place(relx=0.6, rely=0.5, anchor=W, relwidth=0.3, relheight=0.3)
        return frame_ent
