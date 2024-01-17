from tkinter import *
import tkinter.font as tk_font

import ttkbootstrap as ttk

from PIL import Image, ImageTk

from user_package.user import User
import registration_page
from functions import get_percentage_of_screen_size_from_full_hd_size

from connection import Connection
from settings import database, user, password
from main_window_package.main_window import MainWindow


class AuthorizationPage(Tk):

    def __init__(self):
        super().__init__()

        # colors
        self.background_color = "#EDE9E6"
        self.buttons_color = ""

        # window's properties
        self.title("Авторизация")
        self.state("zoomed")

        self.configure(background=self.background_color)

        # screen sizes
        self.percentage_width_from_full_hd = get_percentage_of_screen_size_from_full_hd_size(self)[0] / 100
        self.percentage_height_from_full_hd = get_percentage_of_screen_size_from_full_hd_size(self)[1] / 100

        self.minsize(int(451 * self.percentage_width_from_full_hd), int(451 * self.percentage_height_from_full_hd))

        # cursors
        self.cursor_for_btn = "hand2"

        self.entry1_var = StringVar()
        self.entry2_var = StringVar()

        # fonts
        font_for_entries = tk_font.Font(
            family="Arial",
            size=int(10 * ((self.percentage_width_from_full_hd + self.percentage_height_from_full_hd) / 2)),
        )

        font_for_lbl = tk_font.Font(
            family="Arial",
            size=int(11 * ((self.percentage_width_from_full_hd + self.percentage_height_from_full_hd) / 2))
        )

        font_for_h1_lbl = tk_font.Font(
            family="Arial",
            size=int(13 * ((self.percentage_width_from_full_hd + self.percentage_height_from_full_hd) / 2))
        )

        self.font_for_registration_btn = tk_font.Font(
            family="Arial",
            size=int(10 * ((self.percentage_width_from_full_hd + self.percentage_height_from_full_hd) / 2)),
            underline=True
        )

        entry_style = ttk.Style()
        entry_style.configure(
            "TEntry",
            foreground="#3A3737",
        )

        # dynamic variables
        self.submit_error_text = StringVar()
        self.connection = None
        self.player = None

        # validate command
        self.entries_validate_method = (self.register(self.validate_entries), '%P')

        content_frame = Frame(background=self.background_color)
        content_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        users_data_frame = Frame(content_frame, borderwidth=1, relief=SOLID, background=self.background_color)
        users_data_frame.pack(pady=(20 * self.percentage_height_from_full_hd, 0))

        users_data_frame_name = ttk.Label(
            users_data_frame,
            text="Авторизация пользователя",
            font=font_for_h1_lbl,
            background=self.background_color
        )
        users_data_frame_name.pack(
            pady=(int(20 * self.percentage_height_from_full_hd), int(20 * self.percentage_width_from_full_hd)),
            padx=int(20 * self.percentage_width_from_full_hd)
        )

        # small logo
        self.img = Image.open("../img/log_in_logo.png")
        self.resized_image = self.img.resize((
            int(70 * self.percentage_width_from_full_hd),
            int(70 * self.percentage_height_from_full_hd))
        )
        self.new_image = ImageTk.PhotoImage(self.resized_image)
        label = ttk.Label(users_data_frame, image=self.new_image, background=self.background_color)
        label.pack(pady=(0, 20 * self.percentage_height_from_full_hd))

        email_name_lbl = ttk.Label(
            users_data_frame,
            text="Введите email:",
            font=font_for_lbl,
            background=self.background_color
        )
        email_name_lbl.pack(pady=(0, 5 * self.percentage_height_from_full_hd))
        self.email_ent = ttk.Entry(
            users_data_frame,
            width=int(50 * self.percentage_width_from_full_hd),
            font=font_for_entries,
            justify=CENTER,
            background=self.background_color,
            validate="key",
            validatecommand=self.entries_validate_method
        )
        self.email_ent.pack(padx=int(20 * self.percentage_width_from_full_hd))

        password_name_lbl = ttk.Label(
            users_data_frame,
            text="Введите пароль:",
            font=font_for_lbl,
            background=self.background_color
        )
        password_name_lbl.pack(
            pady=(10 * self.percentage_height_from_full_hd, 5 * self.percentage_height_from_full_hd)
        )
        self.password_ent = ttk.Entry(
            users_data_frame,
            show="•",
            width=int(50 * self.percentage_width_from_full_hd),
            font=font_for_entries,
            justify=CENTER,
            background=self.background_color,
            validate="key",
            validatecommand=self.entries_validate_method
        )
        self.password_ent.pack(pady=(0, 20 * self.percentage_height_from_full_hd))

        self.submit_btn = Button(
            content_frame,
            text="Войти",
            width=20,
            height=2,
            bd=0,
            cursor=self.cursor_for_btn,
            relief=RIDGE,
            font=font_for_lbl,
            command=lambda: self.find_user_in_db(self.email_ent.get(), self.password_ent.get()),
            background="#94C1C0",
            state=DISABLED
        )
        self.submit_btn.pack(pady=(30 * self.percentage_height_from_full_hd, 0))

        registration_btn = ttk.Button(content_frame, text="Зарегистрироваться", bootstyle="success-link",
            cursor=self.cursor_for_btn,
            command=lambda: self.switch_to_registration_page(),
        )
        registration_btn.pack(
            pady=(20 * self.percentage_height_from_full_hd, 30 * self.percentage_height_from_full_hd)
        )

        submit_btn_error_text_lbl = ttk.Label(textvariable=self.submit_error_text)
        submit_btn_error_text_lbl.pack()

    def validate_entries(self, text):
        if (len(text) > 0 and len(self.email_ent.get()) > 0) or (len(text) > 0 and len(self.password_ent.get()) > 0):
            self.submit_btn.configure(state=NORMAL)
        elif not self.email_ent.get() or not self.password_ent.get() or len(text) == 0:
            self.submit_btn.configure(state=DISABLED)
        else:
            self.submit_btn.configure(state=NORMAL)
        return True

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
                  f'Ваш баланс: {self.player.get_balance()} рублей \n'
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
