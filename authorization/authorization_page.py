from tkinter import *
from tkinter import ttk

from connection import Connection
from settings import database, user, password


class AuthorizationPage(Tk):

    def __init__(self):
        super().__init__()

        self.title("Авторизация")
        self.geometry("600x400")

        self.submit_error_text = StringVar()

        self.connection = None
        self.start_connection_to_db()

        users_data_frame = Frame(borderwidth=1, relief=SOLID)
        users_data_frame.pack(pady=(20, 0))

        users_data_frame_name = ttk.Label(users_data_frame, text="Авторизация пользователя")
        users_data_frame_name.pack(pady=(20, 30), padx=20)

        email_name_lbl = ttk.Label(users_data_frame, text="Введите email:")
        email_name_lbl.pack()
        email_ent = ttk.Entry(users_data_frame)
        email_ent.pack()

        password_name_lbl = ttk.Label(users_data_frame, text="Введите пароль:")
        password_name_lbl.pack(pady=(10, 0))
        password_ent = ttk.Entry(users_data_frame)
        password_ent.pack(pady=(0, 20))

        submit_btn = Button(
            text="Войти",
            width=20,
            height=2,
            bd=1,
            relief=RIDGE
        )
        submit_btn.pack(pady=(30, 0))

        registration_btn = Button(
            text="Зарегистрироваться",
            width=20,
            height=2,
            bd=1,
            relief=RIDGE
        )
        registration_btn.pack(pady=(20, 0))

        submit_btn_error_text_lbl = ttk.Label(textvariable=self.submit_error_text)
        submit_btn_error_text_lbl.pack()

    def start_connection_to_db(self):
        self.connection = Connection()
        self.connection.make_connection(user=user, password=password, database=database)


if __name__ == "__main__":
    authorization_page = AuthorizationPage()
    authorization_page.mainloop()
