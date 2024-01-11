from tkinter import *
from tkinter import ttk

import authorization_page


class RegistrationPage(Tk):

    def __init__(self):
        super().__init__()

        self.title("Регистрация")
        self.geometry("600x400")

        # variables
        self.login_error_text_message = StringVar()

        back_btn = Button(
            text="Назад",
            command=self.back_btn_action
        )
        back_btn.pack()

        users_data_frame = Frame(borderwidth=1, relief=SOLID)
        users_data_frame.pack()

        login_name_lbl = ttk.Label(users_data_frame, text="Придумайте Логин")
        login_name_lbl.pack(pady=(20, 0))
        login_ent = ttk.Entry(users_data_frame)
        login_ent.pack()
        login_ent.configure(width=30)
        login_error_text_lbl = ttk.Label(users_data_frame, textvariable=self.login_error_text_message)
        login_error_text_lbl.pack()

        first_name_name_lbl = ttk.Label(users_data_frame, text="Ваше имя")
        first_name_name_lbl.pack(pady=(10, 0))
        first_name_ent = ttk.Entry(users_data_frame)
        first_name_ent.pack()
        first_name_ent.configure(width=30)

        last_name_name_lbl = ttk.Label(users_data_frame, text="Ваша фамилия")
        last_name_name_lbl.pack(pady=(20, 0))
        last_name_ent = ttk.Entry(users_data_frame)
        last_name_ent.pack()
        last_name_ent.configure(width=30)

        user_email_name_lbl = Label(users_data_frame, text="Ваш адрес электронной почты")
        user_email_name_lbl.pack(pady=(20, 0), padx=40)
        email_ent = ttk.Entry(users_data_frame)
        email_ent.pack()
        email_ent.configure(width=30)

        user_password_name_lbl = ttk.Label(users_data_frame, text="Придумайте пароль")
        user_password_name_lbl.pack(pady=(20, 0))
        password_ent = ttk.Entry(users_data_frame)
        password_ent.pack()
        password_ent.configure(width=30)

        user_confirm_password_name_lbl = ttk.Label(users_data_frame, text="Повторите пароль")
        user_confirm_password_name_lbl.pack(pady=(20, 0))
        confirm_password_ent = ttk.Entry(users_data_frame)
        confirm_password_ent.pack()
        confirm_password_ent.configure(width=30)

        registration_btn = Button(text="Зарегистрироваться")
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


