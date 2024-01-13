from tkinter import *
from tkinter import ttk
import tkinter.font as tk_font

import authorization_page
from functions import get_percentage_of_screen_size_from_full_hd_size


class RegistrationPage(Tk):

    def __init__(self):
        super().__init__()

        # window settings
        self.title("Регистрация")
        self.state("zoomed")

        # screen sizes
        self.percentage_width_from_full_hd = get_percentage_of_screen_size_from_full_hd_size(self)[0] / 100
        self.percentage_height_from_full_hd = get_percentage_of_screen_size_from_full_hd_size(self)[1] / 100

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
        content_frame = Frame()
        content_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        back_btn = Button(
            content_frame,
            text="Назад",
            command=self.back_btn_action
        )
        back_btn.pack(anchor=NW, pady=10, padx=(20, 0))

        users_data_frame = Frame(content_frame, borderwidth=1, relief=SOLID)
        users_data_frame.pack()

        login_name_lbl = ttk.Label(users_data_frame, text="Придумайте Логин", font=self.font_for_lbl)
        login_name_lbl.pack(pady=(20, 10))

        login_ent = ttk.Entry(
            users_data_frame,
            width=int(50 * self.percentage_width_from_full_hd),
            justify=CENTER,
            font=self.font_for_entries
        )

        login_ent.pack()
        login_error_text_lbl = ttk.Label(users_data_frame, textvariable=self.login_error_text_message)
        login_error_text_lbl.pack()

        first_name_name_lbl = ttk.Label(users_data_frame, text="Ваше имя", font=self.font_for_lbl)
        first_name_name_lbl.pack(pady=(10, 10))

        first_name_ent = ttk.Entry(
            users_data_frame,
            width=int(50 * self.percentage_width_from_full_hd),
            justify=CENTER,
            font=self.font_for_entries
        )

        first_name_ent.pack()

        last_name_name_lbl = ttk.Label(users_data_frame, text="Ваша фамилия", font=self.font_for_lbl)
        last_name_name_lbl.pack(pady=(20, 10))

        last_name_ent = ttk.Entry(
            users_data_frame,
            width=int(50 * self.percentage_width_from_full_hd),
            justify=CENTER,
            font=self.font_for_entries,
        )

        last_name_ent.pack()

        user_email_name_lbl = Label(users_data_frame, text="Ваш адрес электронной почты", font=self.font_for_lbl)
        user_email_name_lbl.pack(pady=(20, 10), padx=40)

        email_ent = ttk.Entry(
            users_data_frame,
            width=int(50 * self.percentage_width_from_full_hd),
            justify=CENTER,
            font=self.font_for_entries
        )

        email_ent.pack()

        user_password_name_lbl = ttk.Label(users_data_frame, text="Придумайте пароль", font=self.font_for_lbl)
        user_password_name_lbl.pack(pady=(20, 10))

        password_ent = ttk.Entry(
            users_data_frame,
            width=int(50 * self.percentage_width_from_full_hd),
            justify=CENTER,
            font=self.font_for_entries
        )

        password_ent.pack()

        user_confirm_password_name_lbl = ttk.Label(users_data_frame, text="Повторите пароль", font=self.font_for_lbl)
        user_confirm_password_name_lbl.pack(pady=(20, 10))
        confirm_password_ent = ttk.Entry(
            users_data_frame,
            width=int(50 * self.percentage_width_from_full_hd),
            justify=CENTER,
            font=self.font_for_entries
        )
        confirm_password_ent.pack()

        registration_btn = Button(content_frame, text="Зарегистрироваться")
        registration_btn.pack()

    def back_btn_action(self):
        self.destroy()
        authorization_page_var = authorization_page.AuthorizationPage()
        authorization_page_var.mainloop()

    def registration_btn_action(self):
        pass

    def registrate_new_user(self):
        pass


def main():
    registration_page = RegistrationPage()
    registration_page.mainloop()

if __name__ == "__main__":
    main()


