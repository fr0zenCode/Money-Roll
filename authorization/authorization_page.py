from datetime import datetime

from PIL import Image, ImageTk

import tkinter as tk
import _tkinter
import customtkinter as ctk

import connection
from settings import (user as db_user, password as db_password, database as db_name, background_color,
                      areas_background, buttons_background_color, buttons_hover_background_color)

import authorization.registration_page as registration_page
import user_package.user as user
import main_window_package.main_window as main_window


class AuthorizationPage(ctk.CTk):

    def __init__(self):
        super().__init__()

        # window's properties
        self.title("Авторизация")
        self.configure(fg_color=background_color)

        # variables
        self.small_logo: tk.StringVar = tk.StringVar(value="img/log_in_logo.png")

        self.screen_width: int = self.winfo_screenwidth()
        self.screen_height: int = self.winfo_screenheight()
        self.minsize(int(self.screen_width // 1.7), int(self.screen_height // 1.7))

        self.font_for_h2: tuple = ("default", 0)
        self.font_for_ent_and_lbl: tuple = ("default", 0)
        self._create_fonts()

        # dynamic variables
        self.connection: connection.Connection() = connection.Connection()
        self.player: user.User = user.User(
            "default",
            0,
            "default",
            "default",
            "default",
            "default",
            0
        )

        main_frame = ctk.CTkFrame(self, fg_color=background_color)
        main_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.8, relheight=0.8)

        # users data frame
        ###############################################################################################################
        upper_frame = ctk.CTkFrame(main_frame, fg_color=background_color)
        upper_frame.place(relx=0, rely=0, anchor="nw", relwidth=1, relheight=0.5)

        page_name = ctk.CTkLabel(upper_frame, text="Авторизация пользователя", font=self.font_for_h2)
        page_name.place(relx=0.5, rely=0, anchor="n", relwidth=0.9, relheight=0.1)

        # small logo
        ###############################################################################################################
        self.canvas = tk.Canvas(
            master=upper_frame,
            bd=0,
            highlightthickness=0,
            relief="ridge",
            background=background_color
        )
        self.canvas.place(relx=0.5, rely=0.2, anchor="n", relwidth=0.06, relheight=0.2)
        self.canvas.bind("<Configure>", self._stretch_small_logo)

        try:
            self.image_original = Image.open(self.small_logo.get())
        except _tkinter.TclError:
            self.image_original = Image.open(f"../{self.small_logo.get()}")
        except FileNotFoundError:
            self.image_original = Image.open(f"../{self.small_logo.get()}")

        self.resized_image = self.image_original.resize((self.winfo_width(), self.winfo_height()))
        self.resized_tk = ImageTk.PhotoImage(self.resized_image)

        self.canvas.create_image(0, 0, anchor="nw", image=self.resized_tk)
        ###############################################################################################################

        self.entries_validate_method = (self.register(self._validate_entries), "%P", "%d")

        self._create_label(upper_frame, "Введите email:", 0.5)
        self.email_ent = self._create_entry(upper_frame, 0.56)

        self._create_label(upper_frame, "Введите пароль:", 0.7)
        self.password_ent = self._create_entry(upper_frame, 0.76, is_password=True)
        ###############################################################################################################

        down_frame = ctk.CTkFrame(main_frame, fg_color=background_color)
        down_frame.place(relx=0, rely=0.5, anchor="nw", relwidth=1, relheight=0.5)

        # error message
        ###############################################################################################################
        self.error_message_var = tk.StringVar(value="")

        error_message_lbl = ctk.CTkLabel(
            down_frame,
            textvariable=self.error_message_var,
            text_color="#E32261",
            font=self.font_for_ent_and_lbl
        )
        error_message_lbl.place(relx=0.5, rely=0, anchor="n", relwidth=0.8, relheight=0.1)
        ###############################################################################################################

        self.submit_btn = ctk.CTkButton(
            down_frame,
            text="Войти",
            command=lambda: self.find_user_in_db(self.email_ent.get(), self.password_ent.get()),
            state="disabled",
            fg_color=buttons_background_color,
            hover_color=buttons_hover_background_color,
            border_color="white",
            border_width=2,
            font=self.font_for_ent_and_lbl
        )
        self.submit_btn.place(relx=0.5, rely=0.2, anchor="n", relwidth=0.14, relheight=0.14)

        registration_btn = ctk.CTkButton(
            down_frame,
            text="Зарегистрироваться",
            command=lambda: self.switch_to_registration_page(),
            fg_color="#3C5171",
            hover_color="#BD6C8C",
            border_color="grey",
            border_width=2,
            font=self.font_for_ent_and_lbl
        )
        registration_btn.place(relx=0.5, rely=0.4, anchor="n", relwidth=0.14, relheight=0.14)

    def find_user_in_db(self, user_email: str, user_password: str) -> bool:
        """
        RUS:
        Функция устанавливает соединение с базой данных и выполняет запрос с данными, предоставленными пользователем.
        Если строка в БД найдена, то вызывается функция "_authorise_user()", которая выполняет авторизацию пользователя
        в системе. В случае неудачи задается текст ошибки для переменной, отображаемой в интерфейсе через виджет Label.

        ENG:
        The function establishes a connection with the database and executes a query with data provided by the user.
        If the string is found in the database, the function "_authorise_user()" is called, which authorises the user
        in the system.
        In case of failure, and error message is set for the variable displayed in the interface by label-widget.

        :param user_email: string, user's email
        :param user_password: string, user's, password
        :return: bool, True if everything is ok; False if an error
        """
        if not self.connection.get_connection():
            self.connection.make_connection(user=db_user, password=db_password, database=db_name)

        self.connection.get_cursor().execute(
            f"""
            SELECT *
            FROM 
                "authorization-data"
            WHERE
                email='{user_email}' AND password='{user_password}'
            """
        )

        fetchone_object = self.connection.get_cursor().fetchone()
        if fetchone_object:
            users_data = fetchone_object
            self._authorise_user(
                users_data[0],
                users_data[1],
                users_data[2],
                users_data[3],
                users_data[4],
                users_data[5],
                users_data[6]
            )
            authorization_time = datetime.now()
            print(f"Пользователь {self.player.login} авторизован! \n"
                  f"Дата и время авторизации: {authorization_time} \n\n"
                  f"Идентификатор в системе: {self.player.user_id} \n"
                  f"Логин: {self.player.login} \n"
                  f"Имя: {self.player.first_name} \n"
                  f"Фамилия: {self.player.last_name} \n"
                  f"Баланс: {self.player.get_balance()} рублей \n")
        else:
            self.error_message_var.set("Неверные данные для входа!")
            return False

        return True

    def switch_to_registration_page(self) -> None:
        """
        RUS:
        Функция осуществляет переход на страницу регистрации. Она уничтожает объект класса "AuthorizationPage", создает
        объект класса "RegistrationPage" и запускает его методом "mainloop()".

        ENG:
        The function switches to the registration page. It destroys object of the "AuthorizationPage" class, creates
        an object of the "RegistrationPage" class, and starts it with the "mainloop()" method.

        :return: None
        """
        self.destroy()
        registration_page_var = registration_page.RegistrationPage()
        registration_page_var.mainloop()

    def _authorise_user(
            self,
            user_id: int,
            login: str,
            first_name: str,
            last_name: str,
            email: str,
            user_password: str,
            balance: int = 0
    ) -> None:
        """
        RUS:
        Функция принимает параметры для формирования объекта класса "User" из модуля "user" и формирует его.
        Если все поля заполнены, то после формирования объекта окно авторизации закрывается, и открывается главное
        окно (объект класса "MainWindow" из модуля "main_window"), в которое передается авторизованный пользователь.
        В противном случае выводит текст об ошибке.

        ENG:
        The function takes parameters to form an object of  the "User" class from the "user" module and forms it.
        If all fields are filled, after forming the object, the authorization window is closed, and the main window
        (an object of the "MainWindow" class from the "main_window" module) is opened, which takes authorise user.
        If Error, an error message is displayed.

        :param user_id: integer, primary key, user's id
        :param login: string, user's login
        :param first_name: string, user's first name
        :param last_name: string, user's last name
        :param email: string, user's email
        :param user_password: string, user's password
        :param balance: integer, user's balance
        :return: None
        """

        if user_id and login and first_name and last_name and email and user_password and balance:

            self.player = user.User(login, user_id, first_name, last_name, email, user_password, balance)
            self.destroy()

            main_window_var = main_window.MainWindow(self.player)
            main_window_var.mainloop()

        else:

            error_text: str = (
                f"""ERROR! 
                \nPackage: authorizations 
                \nModule: authorization_page.py 
                \nError: can't form object User: not all parameters have been given."""
            )
            print(error_text)

    def _stretch_small_logo(self, event: tk.Event) -> None:
        """
        RUS:
        Функция вызывается при изменении размера виджета "Canvas", в котором находится маленькое лого авторизации.
        При изменении размера виджета, функция вычисляет с помощью методов "tkinter'а" новые размеры и измененяет
        размер исходной картинки.
        Затем функция заменяет картинку в виджете.

        ENG:
        The function is called when the "Canvas" widget containing the small authorization logo changes size.
        When the widget size changes, the function calculates the new size using "tkinter's" methods and resizes
        picture.
        Then the function replaces the image in the "Canvas".

        :param event: tkinter.Event
        :return: None
        """
        width: int = event.width
        height: int = event.height

        self.resized_image = self.image_original.resize((width, height))
        self.resized_tk = ImageTk.PhotoImage(self.resized_image)
        self.canvas.create_image(0, 0, image=self.resized_tk, anchor="nw")

    def _validate_entries(self, text: str, action_type: str) -> bool:
        """
        RUS:
        Осуществляет валидацию вводимых данных в полях "Адрес электронной почты" и "Пароль".
        Если в фукнцию поступает строка длиной более 1 символа, то проверяются на заполенность оба поля:
        "Адрес электронной почты" и "Пароль", т.к. при введении первого символа, в момент валидации, при применении к
        виджету "Entry" метода "get()", возвращается пустая строка.
        Если поступает на вход строка длиной 1 символ, то проверяется заполненность хотя бы одного виджета "Entry",
        т.к. текущий будет незаполнен, поскольку идет только процесс валидации.
        В случае, если одна из проверок пройдена, открывается возможность нажатия на кнопку "Войти", в противном случае
        для кнопки "Войти" устанавливается состояние DISABLED.
        Если тип действия не вставка символа и строка не пустая, то валидация пропускается.

        ENG:
        The function validates the incoming data from entries "Email" and "Password".
        If the function receives a string with length of more than one symbol, it inspects both entries because if
        there is only one symbol in the entry during validation, using the "get()" method on this entry return an empty
        string.
        If the function receives a string which a length of one symbol, it inspects whether only one of the two entries
        if filled because the one under validation will be empty.
        If any of the tests are successful, the submit button will be able to clic; otherwise it will be disabled.
        If the action type is not inputting a symbol and the string is not empty, validation will be skipped.

        :param text: string, text for validation.
        :return: bool, True if test is success and False if tests fails.
        """
        self.error_message_var.set("")

        if " " in text:
            return False

        if action_type != "1" and text:
            return True

        if len(text) > 1:
            if self.email_ent.get() and self.password_ent.get():
                self.submit_btn.configure(state="normal")
        elif len(text) == 1:
            if (len(text) > 0 and self.email_ent.get()) or (len(text) > 0 and self.password_ent.get()):
                self.submit_btn.configure(state="normal")
        else:
            self.submit_btn.configure(state="disabled")
        return True

    def _create_entry(self, master: ctk.CTkFrame, rely: float | int, is_password: bool = False) -> ctk.CTkEntry:
        """
        RUS:
        Функция создает и возвращает виджет Entry.

        ENG:
        Function creates and returns the Entry-widget.

        :param master: ctk.CTkFrame, parents frame
        :param rely: float | integer - relative vertical position
        :return: ctk.CTkEntry - Entry widget
        """
        entry: ctk.CTkEntry = ctk.CTkEntry(
            master,
            justify="center",
            validate="key",
            validatecommand=self.entries_validate_method,
            fg_color=areas_background,
            border_color="white",
            font=self.font_for_ent_and_lbl
        )
        entry.place(relx=0.5, rely=rely, anchor="n", relwidth=0.5, relheight=0.1)

        if is_password:
            entry.configure(show="•")

        return entry

    def _create_label(self, master: ctk.CTkFrame, text: str, rely: float | int) -> ctk.CTkLabel:
        """
        RUS:
        Функция создает и возвращает виджет Label.

        ENG:
        Function creates and returns Label widget.

        :param master: ctk.CTkFrame, parents frame
        :param text: string, text in label
        :param rely: float | integer - relative vertical position
        :return: ctk.CTkLabel, label widget
        """
        label: ctk.CTkLabel = ctk.CTkLabel(master, text=text, font=self.font_for_ent_and_lbl)
        label.place(relx=0.5, rely=rely, anchor="n", relwidth=0.9, relheight=0.05)

        return label

    def _create_fonts(self) -> None:
        """
        RUS:
        Функция, в зависимости от размера экрана, передает в динамические переменные шрифтов наименование и размер
        подходящего шрифта.

        ENG:
        Function looks at the screen sizes and makes fonts. It sets dynamic variables.

        :return: None
        """
        if self.screen_width >= 800 and self.screen_height >= 600:
            self.font_for_h2 = ("Arial", 8)
            self.font_for_ent_and_lbl = ("Arial", 4)
        if self.screen_width >= 1024 and self.screen_height >= 768:
            self.font_for_h2 = ("Arial", 12)
            self.font_for_ent_and_lbl = ("Arial", 6)
        if self.screen_width >= 1176 and self.screen_height >= 664:
            self.font_for_h2 = ("Arial", 12.5)
            self.font_for_ent_and_lbl = ("Arial", 6.5)
        if self.screen_width >= 1280 and self.screen_height >= 720:
            self.font_for_h2 = ("Arial", 13.4)
            self.font_for_ent_and_lbl = ("Arial", 7.4)
        if self.screen_width >= 1600 and self.screen_height >= 900:
            self.font_for_h2 = ("Arial", 15.4)
            self.font_for_ent_and_lbl = ("Arial", 9.4)
        if self.screen_width >= 1920 and self.screen_height >= 1080:
            self.font_for_h2 = ("Arial", 20)
            self.font_for_ent_and_lbl = ("Arial", 11)
        if self.screen_width >= 2560 and self.screen_height >= 1440:
            self.font_for_h2 = ("Arial", 25)
            self.font_for_ent_and_lbl = ("Arial", 15)
        if self.screen_width >= 3840 and self.screen_height >= 2160:
            self.font_for_h2 = ("Arial", 35)
            self.font_for_ent_and_lbl = ("Arial", 20)


if __name__ == "__main__":
    authorization_page = AuthorizationPage()
    authorization_page.mainloop()
