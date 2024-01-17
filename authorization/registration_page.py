from tkinter import *
from tkinter import ttk
import tkinter.font as tk_font

from functions import get_percentage_of_screen_size_from_full_hd_size

from connection import Connection
from settings import database, user, password
import authorization_page


class RegistrationPage(Tk):

    def __init__(self):
        super().__init__()

        # PostreSQL connection
        self.connection = None

        # window settings
        self.title("Регистрация")
        self.state("zoomed")

        # colors
        self.background_color = "#EDE9E6"

        # screen sizes
        self.percentage_width_from_full_hd = get_percentage_of_screen_size_from_full_hd_size(self)[0] / 100
        self.percentage_height_from_full_hd = get_percentage_of_screen_size_from_full_hd_size(self)[1] / 100
        self.minsize(int(500 * self.percentage_width_from_full_hd), int(500 * self.percentage_height_from_full_hd))
        self.configure(background=self.background_color)

        # validate methods
        self.email_entry_validate_method = (self.register(self.validate_email_entry), "%P")
        self.login_entry_validate_method = (self.register(self.validate_login_entry), "%P")

        # fonts
        self.font_for_entries = tk_font.Font(
            family="Arial",
            size=int(10 * ((self.percentage_width_from_full_hd + self.percentage_height_from_full_hd) / 2)),
        )

        self.font_for_lbl = tk_font.Font(
            family="Arial",
            size=int(11 * ((self.percentage_width_from_full_hd + self.percentage_height_from_full_hd) / 2))
        )

        self.font_for_h1_lbl = tk_font.Font(
            family="Arial",
            size=int(13 * ((self.percentage_width_from_full_hd + self.percentage_height_from_full_hd) / 2))
        )

        self.font_for_registration_btn = tk_font.Font(
            family="Arial",
            size=int(10 * ((self.percentage_width_from_full_hd + self.percentage_height_from_full_hd) / 2)),
            underline=True
        )

        # variables
        self.login_error_text_message = StringVar()

        # main frame
        content_frame = Frame(background=self.background_color)
        content_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        back_btn = Button(
            content_frame,
            text="Назад",
            command=self.back_btn_action
        )
        back_btn.pack(anchor=NW, pady=int(10 * self.percentage_height_from_full_hd))

        users_data_frame = Frame(content_frame, borderwidth=1, relief=SOLID, background=self.background_color)
        users_data_frame.pack()

        login_name_lbl = ttk.Label(users_data_frame, text="Придумайте Логин", font=self.font_for_lbl)
        login_name_lbl.pack(pady=(20, 10))

        self.login_ent = ttk.Entry(
            users_data_frame,
            width=int(50 * self.percentage_width_from_full_hd),
            justify=CENTER,
            font=self.font_for_entries,
            validate="all",
            validatecommand=self.login_entry_validate_method
        )

        self.login_ent.pack()
        login_error_text_lbl = ttk.Label(users_data_frame, textvariable=self.login_error_text_message)
        login_error_text_lbl.pack()

        first_name_name_lbl = ttk.Label(users_data_frame, text="Ваше имя", font=self.font_for_lbl)
        first_name_name_lbl.pack(pady=(10, 10))

        self.first_name_ent = ttk.Entry(
            users_data_frame,
            width=int(50 * self.percentage_width_from_full_hd),
            justify=CENTER,
            font=self.font_for_entries
        )

        self.first_name_ent.pack()

        last_name_name_lbl = ttk.Label(users_data_frame, text="Ваша фамилия", font=self.font_for_lbl)
        last_name_name_lbl.pack(pady=(20, 10))

        self.last_name_ent = ttk.Entry(
            users_data_frame,
            width=int(50 * self.percentage_width_from_full_hd),
            justify=CENTER,
            font=self.font_for_entries,
        )

        self.last_name_ent.pack(padx=int(20 * self.percentage_width_from_full_hd))

        user_email_name_lbl = Label(users_data_frame, text="Ваш адрес электронной почты", font=self.font_for_lbl)
        user_email_name_lbl.pack(pady=(20, 10), padx=40)

        self.email_ent = ttk.Entry(
            users_data_frame,
            width=int(50 * self.percentage_width_from_full_hd),
            justify=CENTER,
            font=self.font_for_entries,
            validate="all",
            validatecommand=self.email_entry_validate_method
        )

        self.email_ent.pack()

        user_password_name_lbl = ttk.Label(users_data_frame, text="Придумайте пароль", font=self.font_for_lbl)
        user_password_name_lbl.pack(pady=(20, 10))

        self.password_ent = ttk.Entry(
            users_data_frame,
            width=int(50 * self.percentage_width_from_full_hd),
            justify=CENTER,
            font=self.font_for_entries
        )

        self.password_ent.pack()

        # confirm password
        user_confirm_password_name_lbl = ttk.Label(users_data_frame, text="Повторите пароль", font=self.font_for_lbl)
        user_confirm_password_name_lbl.pack(pady=(20, 10))

        self.confirm_password_ent = ttk.Entry(
            users_data_frame,
            width=int(50 * self.percentage_width_from_full_hd),
            justify=CENTER,
            font=self.font_for_entries
        )
        self.confirm_password_ent.pack(pady=(0, 20 * self.percentage_height_from_full_hd))

        # registration button
        self.registration_btn = Button(content_frame, text="Зарегистрироваться", command=self.registration_btn_action)
        self.registration_btn.pack(
            pady=(20 * self.percentage_height_from_full_hd, 20 * self.percentage_height_from_full_hd)
        )

    def back_btn_action(self):
        self.destroy()
        authorization_page_var = authorization_page.AuthorizationPage()
        authorization_page_var.mainloop()

    def registration_btn_action(self):
        if not self.check_all_entries():
            print("Не все поля заполнены")
            return
        if not self.check_password():
            print("Пароли не совпадают")
            return
        self.registrate_new_user()
        self.destroy()
        authorization_page_to_redirect = authorization_page.AuthorizationPage()
        authorization_page_to_redirect.mainloop()

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

        self.connection.get_cursor().execute(
            f"""INSERT INTO "authorization-data" (login, first_name, last_name, email, password, balance) 
            VALUES ('{login}', '{first_name}', '{last_name}', '{email}', '{password}', '{balance}')"""
        )

        self.connection.get_connection().commit()

    def check_password(self):
        if self.password_ent.get() == self.confirm_password_ent.get():
            return True
        return False

    def check_all_entries(self):
        if (self.login_ent.get()
                and self.first_name_ent
                and self.last_name_ent
                and self.email_ent
                and self.password_ent
                and self.confirm_password_ent):
            return True
        return False

    def validate_email_entry(self, email):
        if self.connection is None:
            self.start_connection_to_db()
        if self.find_data_in_db(email, email_type=True):
            self.registration_btn.configure(state=DISABLED)
            return True
        self.registration_btn.configure(state=NORMAL)
        return True

    def validate_login_entry(self, login):
        if self.connection is None:
            self.start_connection_to_db()
        if self.find_data_in_db(login, login_type=True):
            self.registration_btn.configure(state=DISABLED)
            return True
        self.registration_btn.configure(state=NORMAL)
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
                print("Адресс электронной почты уже занят!")
                return True
            else:
                print("Логин уже занят!")
                return True

        return False

    def start_connection_to_db(self):
        self.connection = Connection()
        self.connection.make_connection(user=user, password=password, database=database)


def main():
    registration_page = RegistrationPage()
    registration_page.mainloop()


if __name__ == "__main__":
    main()
