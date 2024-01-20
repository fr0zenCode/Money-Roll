import tkinter as tk
import customtkinter as ctk
from tkinter.messagebox import showerror

import psycopg2

import connection
from settings import (user as db_user, password as db_password, database as db_name, background_color,
                      buttons_background_color, buttons_hover_background_color, areas_background)

import authorization.authorization_page as authorization_page
import main_window_package.main_window as main_window
import user_package.user as user


class RegistrationPage(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.connection = connection.Connection()
        self.player = None

        # window settings
        self.title("Регистрация")
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.minsize(int(self.screen_width / 1.7), int(self.screen_height / 1.7))

        self.configure(fg_color=background_color)

        # validate methods
        self.email_entry_validate_method = (self.register(self.validate_email_entry), "%P")
        self.login_entry_validate_method = (self.register(self.validate_login_entry), "%P")

        # variables
        self.login_error_text_message = tk.StringVar(value="")
        self.email_error_text_message = tk.StringVar(value="")
        self.confirm_password_error_text_message = tk.StringVar(value="")
        self.registration_error_text = tk.StringVar(value="")

        # main frame
        ###############################################################################################################
        content_frame = ctk.CTkFrame(self, fg_color=background_color)
        content_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.8, relheight=0.8)
        ###############################################################################################################

        back_btn = ctk.CTkButton(
            content_frame,
            text="Назад",
            command=self.back_btn_action,
            fg_color=buttons_background_color,
            hover_color=buttons_hover_background_color,
            border_width=1,
            border_color="grey"
        )
        back_btn.place(relx=0, rely=0, anchor="nw", relwidth=0.06, relheight=0.05)

        # user's data frame
        ###############################################################################################################
        users_data_frame = ctk.CTkFrame(content_frame, fg_color=background_color)
        users_data_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.8, relheight=0.8)

        # login
        login_name_lbl = ctk.CTkLabel(users_data_frame, text="Придумайте Логин")
        login_name_lbl.place(relx=0.5, rely=0, anchor="n", relwidth=0.8, relheight=0.03)

        self.login_ent = ctk.CTkEntry(
            users_data_frame,
            justify="center",
            validate="key",
            validatecommand=self.login_entry_validate_method,
            fg_color=areas_background
        )
        self.login_ent.place(relx=0.5, rely=0.03, anchor="n", relwidth=0.5, relheight=0.04)

        login_error_text_lbl = ctk.CTkLabel(
            users_data_frame,
            textvariable=self.login_error_text_message,
            text_color="red"
        )
        login_error_text_lbl.place(relx=0.5, rely=0.07, anchor="n", relwidth=0.8, relheight=0.03)

        # first name
        first_name_name_lbl = ctk.CTkLabel(users_data_frame, text="Ваше имя")
        first_name_name_lbl.place(relx=0.5, rely=0.10, anchor="n", relwidth=0.8, relheight=0.03)

        self.first_name_ent = ctk.CTkEntry(users_data_frame, justify="center", fg_color=areas_background)
        self.first_name_ent.place(relx=0.5, rely=0.13, anchor="n", relwidth=0.5, relheight=0.04)

        # last name
        last_name_name_lbl = ctk.CTkLabel(users_data_frame, text="Ваша фамилия")
        last_name_name_lbl.place(relx=0.5, rely=0.2, anchor="n", relwidth=0.8, relheight=0.03)

        self.last_name_ent = ctk.CTkEntry(users_data_frame, justify="center", fg_color=areas_background)
        self.last_name_ent.place(relx=0.5, rely=0.23, anchor="n", relwidth=0.5, relheight=0.04)

        # email
        user_email_name_lbl = ctk.CTkLabel(users_data_frame, text="Ваш адрес электронной почты")
        user_email_name_lbl.place(relx=0.5, rely=0.3, anchor="n", relwidth=0.8, relheight=0.03)

        self.email_ent = ctk.CTkEntry(
            users_data_frame,
            justify="center",
            validate="key",
            validatecommand=self.email_entry_validate_method,
            fg_color=areas_background
        )
        self.email_ent.place(relx=0.5, rely=0.33, anchor="n", relwidth=0.5, relheight=0.04)

        email_error_text_lbl = ctk.CTkLabel(
            users_data_frame,
            textvariable=self.email_error_text_message,
            text_color="red"
        )
        email_error_text_lbl.place(relx=0.5, rely=0.37, anchor="n", relwidth=0.8, relheight=0.03)

        # password
        user_password_name_lbl = ctk.CTkLabel(users_data_frame, text="Придумайте пароль")
        user_password_name_lbl.place(relx=0.5, rely=0.4, anchor="n", relwidth=0.8, relheight=0.03)

        self.password_ent = ctk.CTkEntry(users_data_frame, justify="center", fg_color=areas_background)
        self.password_ent.place(relx=0.5, rely=0.43, anchor="n", relwidth=0.5, relheight=0.04)

        # confirm password
        user_confirm_password_name_lbl = ctk.CTkLabel(users_data_frame, text="Повторите пароль")
        user_confirm_password_name_lbl.place(relx=0.5, rely=0.5, anchor="n", relwidth=0.8, relheight=0.03)

        self.confirm_password_ent = ctk.CTkEntry(users_data_frame, justify="center", fg_color=areas_background)
        self.confirm_password_ent.place(relx=0.5, rely=0.53, anchor="n", relwidth=0.5, relheight=0.04)

        confirm_password_error_text_lbl = ctk.CTkLabel(
            users_data_frame,
            textvariable=self.confirm_password_error_text_message,
            text_color="red"
        )
        confirm_password_error_text_lbl.place(relx=0.5, rely=0.57, anchor="n", relwidth=0.8, relheight=0.03)
        ###############################################################################################################

        # button frame
        ###############################################################################################################
        button_frame = ctk.CTkFrame(users_data_frame, fg_color=background_color)
        button_frame.place(relx=0, rely=1, anchor="sw", relwidth=1, relheight=0.4)

        registration_error_lbl = ctk.CTkLabel(button_frame, textvariable=self.registration_error_text, text_color="red")
        registration_error_lbl.place(relx=0.5, rely=0.35, anchor="s", relwidth=0.8, relheight=0.1)

        self.registration_btn = ctk.CTkButton(
            button_frame,
            text="Зарегистрироваться",
            command=self.registration_btn_action,
            fg_color=buttons_background_color,
            hover_color=buttons_hover_background_color,
            border_width=2,
            border_color="white"
        )
        self.registration_btn.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.2, relheight=0.3)
        ###############################################################################################################

    def back_btn_action(self):
        self.destroy()
        authorization_page_var = authorization_page.AuthorizationPage()
        authorization_page_var.mainloop()

    def registration_btn_action(self):

        if not self.check_all_entries():
            return

        if not self.check_password():
            return

        if self.registrate_new_user():
            player = self.player
            self.destroy()
            main_window_page = main_window.MainWindow(player)
            main_window_page.mainloop()

    def registrate_new_user(self):

        # user_package data
        login = self.login_ent.get()
        first_name = self.first_name_ent.get()
        last_name = self.last_name_ent.get()
        email = self.email_ent.get()
        password = self.password_ent.get()
        balance = 0

        if self.connection is None:
            self.start_connection_to_db()

        try:

            self.connection.get_cursor().execute(
                f"""INSERT INTO "authorization-data" (login, first_name, last_name, email, password, balance) 
                VALUES ('{login}', '{first_name}', '{last_name}', '{email}', '{password}', '{balance}')"""
            )
            self.connection.get_cursor().execute(
                f"""SELECT * FROM "authorization-data"
                WHERE 
                login='{login}' AND email='{email}' AND password='{password}'""")

            fetchone_object = self.connection.get_cursor().fetchone()

            self.player = user.User(
                fetchone_object[0],
                fetchone_object[1],
                fetchone_object[2],
                fetchone_object[3],
                fetchone_object[4],
                fetchone_object[5],
                fetchone_object[6],
                0
            )
            self.connection.get_connection().commit()
            return True

        except psycopg2.OperationalError:
            showerror("Ошибка регистрации!", "Произошла ошибка во время записи данных в базу данных. "
                                             "Повторите попытку!")
            self.connection.get_connection().close()
            return False

    def check_password(self):
        if self.password_ent.get() != self.confirm_password_ent.get():
            self.confirm_password_error_text_message.set("Пароли не совпадают!")
            return False
        return True

    def check_all_entries(self):
        self.registration_error_text.set("")

        if not (self.login_ent.get()
                and self.first_name_ent.get()
                and self.last_name_ent.get()
                and self.email_ent.get()
                and self.password_ent.get()
                and self.confirm_password_ent.get()):
            self.registration_error_text.set("Не все поля заполнены!")
            return False
        return True

    def validate_email_entry(self, email):
        if self.connection is None:
            self.start_connection_to_db()
        if self.find_data_in_db(email, email_type=True):
            self.email_error_text_message.set("Email уже занят!")
            self.registration_btn.configure(state="disabled")
            return True
        self.email_error_text_message.set("")
        self.registration_btn.configure(state="normal")
        return True

    def validate_login_entry(self, login):
        if " " in login:
            self.login_error_text_message.set("Запрещенный символ!")
            return False
        if self.connection is None:
            self.start_connection_to_db()
        if self.find_data_in_db(login, login_type=True):
            self.login_error_text_message.set("Логин уже занят!")
            self.registration_btn.configure(state="disabled")
            return True
        self.login_error_text_message.set("")
        self.registration_btn.configure(state="normal")
        return True

    def find_data_in_db(self, data, email_type=False, login_type=False):
        parameter_in_db = None
        if email_type:
            parameter_in_db = "email"
        elif login_type:
            parameter_in_db = "login"

        self.connection.get_cursor().execute(
            f'''
            SELECT *
            FROM "authorization-data"
            WHERE
            {parameter_in_db}='{data}';
            '''
        )
        fetchall_object = self.connection.get_cursor().fetchall()
        if fetchall_object:
            if parameter_in_db == "email":
                return True
            else:
                return True

        return False

    def start_connection_to_db(self):
        self.connection = connection.Connection()
        self.connection.make_connection(user=db_user, password=db_password, database=db_name)


def main():
    registration_page = RegistrationPage()
    registration_page.mainloop()


if __name__ == "__main__":
    main()
