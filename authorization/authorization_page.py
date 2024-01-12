from tkinter import *
from tkinter import ttk

from user.user import User
import registration_page

from connection import Connection
from settings import database, user, password
from main import MainWindow


class AuthorizationPage(Tk):

    def __init__(self):
        super().__init__()

        # window's properties
        self.title("Авторизация")
        self.geometry("600x400")

        # dynamic variables
        self.submit_error_text = StringVar()
        self.connection = None
        self.player = None

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
        password_ent = ttk.Entry(users_data_frame, show="•")
        password_ent.pack(pady=(0, 20))

        submit_btn = Button(
            text="Войти",
            width=20,
            height=2,
            bd=1,
            relief=RIDGE,
            command=lambda: self.find_user_in_db(email_ent.get(), password_ent.get())
        )
        submit_btn.pack(pady=(30, 0))

        registration_btn = Button(
            text="Зарегистрироваться",
            width=20,
            height=2,
            bd=1,
            relief=RIDGE,
            command=lambda: self.switch_to_registration_page()
        )
        registration_btn.pack(pady=(20, 0))

        submit_btn_error_text_lbl = ttk.Label(textvariable=self.submit_error_text)
        submit_btn_error_text_lbl.pack()

    def start_connection_to_db(self):
        self.connection = Connection()
        self.connection.make_connection(user=user, password=password, database=database)

    def find_user_in_db(self, user_email, user_password):

        if not user_email or not user_password:
            print("Некорректные данные для входа!")
            return False

        self.start_connection_to_db()

        self.connection.get_cursor().execute(
            f'''
            SELECT *
            FROM "authorization-data"
            WHERE
            email='{user_email}' AND password='{user_password}'
            '''
        )
        fetchall_object = self.connection.get_cursor().fetchall()
        if len(fetchall_object):
            users_data = fetchall_object[0]
            self.authorise_user(
                users_data[0],
                users_data[1],
                users_data[2],
                users_data[3],
                users_data[4],
                users_data[5],
                users_data[6]
            )
            print(f'Поздравляем! Вы авторизованы! \n'
                  f'Ваш идентификатор в системе: {self.player.user_id} \n'
                  f'Ваш логин: {self.player.login} \n'
                  f'Ваше имя: {self.player.first_name} \n'
                  f'Ваша фамилия: {self.player.last_name} \n'
                  f'Ваш пароль: {self.player.get_password()} \n'
                  f'Ваш баланс: {self.player._balance} рублей \n'
                  f'Ваш шанс на большой выигрыш {self.player._chance_for_big_win}% \n')
        else:
            print(f"Пользователь со следующими данными не найден: \n"
                  f"email: {user_email} \n"
                  f"password: {user_password} \n")
        return True

    def switch_to_registration_page(self):
        self.destroy()
        registration_page_var = registration_page.RegistrationPage()
        registration_page_var.mainloop()

    def authorise_user(
            self,
            user_id,
            login,
            first_name,
            last_name,
            email,
            user_password,
            balance=0,
            chance_for_big_win=0
    ):
        self.player = User(login, user_id, first_name, last_name, email, user_password, balance, chance_for_big_win)
        self.player.auth = True
        self.destroy()
        main_window_var = MainWindow(self.player)
        main_window_var.mainloop()


if __name__ == "__main__":
    authorization_page = AuthorizationPage()
    authorization_page.mainloop()
