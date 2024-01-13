from tkinter import *
from tkinter import ttk
import tkinter.font as tk_font
from PIL import Image, ImageTk


from user.user import User
import registration_page

from connection import Connection
from settings import database, user, password
from main import MainWindow


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
        self.percentage_width_from_full_hd = self._get_percentage_of_screen_size_from_full_hd_size()[0] / 100
        self.percentage_height_from_full_hd = self._get_percentage_of_screen_size_from_full_hd_size()[1] / 100

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

        font_for_btn = None

        entry_style = ttk.Style()
        entry_style.configure(
            "TEntry",
            foreground="#3A3737",
        )

        # dynamic variables
        self.submit_error_text = StringVar()
        self.connection = None
        self.player = None

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
            pady=(20 * self.percentage_height_from_full_hd, 20 * self.percentage_width_from_full_hd),
            padx=20 * self.percentage_width_from_full_hd
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
        email_ent = ttk.Entry(
            users_data_frame,
            width=int(50 * self.percentage_width_from_full_hd),
            font=font_for_entries,
            justify=CENTER,
            background=self.background_color
        )
        email_ent.pack(padx=20 * self.percentage_width_from_full_hd)

        password_name_lbl = ttk.Label(
            users_data_frame,
            text="Введите пароль:",
            font=font_for_lbl,
            background=self.background_color
        )
        password_name_lbl.pack(
            pady=(10 * self.percentage_height_from_full_hd, 5 * self.percentage_height_from_full_hd)
        )
        password_ent = ttk.Entry(
            users_data_frame,
            show="•",
            width=int(50 * self.percentage_width_from_full_hd),
            font=font_for_entries,
            justify=CENTER,
            background=self.background_color
        )
        password_ent.pack(pady=(0, 20 * self.percentage_height_from_full_hd))

        submit_btn = Button(
            content_frame,
            text="Войти",
            width=20,
            height=2,
            bd=1,
            relief=RIDGE,
            command=lambda: self.find_user_in_db(email_ent.get(), password_ent.get())
        )
        submit_btn.pack(pady=(30 * self.percentage_height_from_full_hd, 0))

        registration_btn = Button(
            content_frame,
            text="Зарегистрироваться",
            width=20,
            height=2,
            bd=1,
            relief=RIDGE,
            font=font_for_lbl,
            command=lambda: self.switch_to_registration_page()
        )
        registration_btn.pack(
            pady=(20 * self.percentage_height_from_full_hd, 30 * self.percentage_height_from_full_hd)
        )

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

    def _get_percentage_of_screen_size_from_full_hd_size(self):

        normal_screen_width = 1920
        normal_screen_height = 1080

        device_screen_width = self.winfo_screenwidth()
        device_screen_height = self.winfo_screenheight()

        percentage_width = (device_screen_width / normal_screen_width) * 100
        percentage_height = (device_screen_height / normal_screen_height) * 100

        return percentage_width, percentage_height


if __name__ == "__main__":
    authorization_page = AuthorizationPage()
    authorization_page.mainloop()
