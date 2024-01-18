import tkinter as tk
import _tkinter
import customtkinter as ctk

from PIL import Image, ImageTk

import settings
import connection

import registration_page
import user_package.user as user
import main_window_package.main_window as main_window


class AuthorizationPage(tk.Tk):

    def __init__(self):
        super().__init__()

        # colors
        self.background_color = "#EDE9E6"
        self.buttons_color = ""

        # window's properties
        self.title("Авторизация")
        self.state("zoomed")

        self.configure(background=self.background_color)

        # image
        self.small_logo = tk.StringVar(value="img/log_in_logo.png")

        self.minsize(1500, 1000)

        # cursors
        self.cursor_for_btn = "hand2"

        self.entry1_var = tk.StringVar()
        self.entry2_var = tk.StringVar()

        # dynamic variables
        self.submit_error_text = tk.StringVar()
        self.connection = None
        self.player = None

        # validate command
        self.entries_validate_method = (self.register(self.validate_entries), '%P')

        # main frame
        ###############################################################################################################
        content_frame = ctk.CTkFrame(self, fg_color="yellow")
        content_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=0.8, relheight=0.8)
        ###############################################################################################################

        # users data frame
        ###############################################################################################################
        upper_frame = ctk.CTkFrame(content_frame, fg_color="blue")
        upper_frame.place(relx=0, rely=0, anchor="nw", relwidth=1, relheight=0.5)

        page_name = ctk.CTkLabel(upper_frame, text="Авторизация пользователя", font=("Arial", 20))
        page_name.place(relx=0.5, rely=0, anchor="n", relwidth=0.9, relheight=0.1)

        # small logo
        ###############################################################################################################
        self.canvas = tk.Canvas(master=upper_frame, background="red", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(relx=0.5, rely=0.2, anchor="n", relwidth=0.06, relheight=0.2)
        self.canvas.bind("<Configure>", self.stretch_small_logo)

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

        # email entry
        ###############################################################################################################
        email_name_lbl = ctk.CTkLabel(upper_frame, text="Введите email:", font=("Arial", 12), fg_color="pink")
        email_name_lbl.place(relx=0.5, rely=0.5, anchor="n", relwidth=0.9, relheight=0.05)

        self.email_ent = ctk.CTkEntry(
            upper_frame,
            justify="center",
            fg_color="red",
            validate="key",
            validatecommand=self.entries_validate_method
        )

        self.email_ent.place(relx=0.5, rely=0.55, anchor="n", relwidth=0.5, relheight=0.1)
        ###############################################################################################################

        # password entry
        ###############################################################################################################
        password_name_lbl = ctk.CTkLabel(
            upper_frame,
            text="Введите пароль:",
            fg_color="pink"
        )
        password_name_lbl.place(relx=0.5, rely=0.7, anchor="n", relwidth=0.9, relheight=0.05)

        self.password_ent = ctk.CTkEntry(
            upper_frame,
            show="•",
            justify="center",
            fg_color="red",
            validate="key",
            validatecommand=self.entries_validate_method
        )
        self.password_ent.place(relx=0.5, rely=0.75, anchor="n", relwidth=0.5, relheight=0.1)
        ###############################################################################################################

        # down frame
        ###############################################################################################################
        down_frame = ctk.CTkFrame(content_frame, fg_color="black")
        down_frame.place(relx=0, rely=0.5, anchor="nw", relwidth=1, relheight=0.5)
        ###############################################################################################################

        # buttons
        ###############################################################################################################
        self.submit_btn = ctk.CTkButton(
            down_frame,
            text="Войти",
            command=lambda: self.find_user_in_db(self.email_ent.get(), self.password_ent.get()),
            state=tk.DISABLED
        )
        self.submit_btn.place(relx=0.5, rely=0, anchor="n", relwidth=0.14, relheight=0.14)

        submit_error_lbl = ctk.CTkLabel(down_frame, textvariable=self.submit_error_text)
        submit_error_lbl.place(relx=0.5, rely=0.14, anchor="n", relwidth=0.9, relheight=0.05)

        registration_btn = ctk.CTkButton(down_frame,
                                         text="Зарегистрироваться",
                                         command=lambda: self.switch_to_registration_page())
        registration_btn.place(relx=0.5, rely=0.20, anchor="n", relwidth=0.14, relheight=0.14)
        ###############################################################################################################

    def stretch_small_logo(self, event):
        width = event.width
        height = event.height
        self.resized_image = self.image_original.resize((width, height))
        self.resized_tk = ImageTk.PhotoImage(self.resized_image)
        self.canvas.create_image(0, 0, image=self.resized_tk, anchor="nw")

    def validate_entries(self, text):
        if (len(text) > 0 and len(self.email_ent.get()) > 0) or (len(text) > 0 and len(self.password_ent.get()) > 0):
            self.submit_btn.configure(state=tk.NORMAL)
        elif not self.email_ent.get() or not self.password_ent.get() or len(text) == 0:
            self.submit_btn.configure(state=tk.DISABLED)
        else:
            self.submit_btn.configure(state=tk.NORMAL)
        return True

    def start_connection_to_db(self):
        self.connection = connection.Connection()
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
        self.player = user.User(login, user_id, first_name, last_name, email, user_password, balance, chance_for_big_win)
        self.player.auth = True
        self.destroy()
        main_window_var = main_window.MainWindow(self.player)
        main_window_var.mainloop()


if __name__ == "__main__":
    authorization_page = AuthorizationPage()
    authorization_page.mainloop()
