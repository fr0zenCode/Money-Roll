from tkinter import *
from tkinter import ttk

import authorization_page


class RegistrationPage(Tk):

    def __init__(self):
        super().__init__()

        self.title("Регистрация")
        self.geometry("600x400")

        back_btn = Button(
            text="Назад",
            command=self.back_btn_action
        )
        back_btn.pack()

    def back_btn_action(self):
        self.destroy()
        authorization_page_var = authorization_page.AuthorizationPage()
        authorization_page_var.mainloop()
