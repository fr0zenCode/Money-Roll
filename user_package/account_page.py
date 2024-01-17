from tkinter import *
import customtkinter as ctk


import authorization.functions as functions
import user_package.user as user
import user_package.account_page_main_frame as account_page_main_frame


class AccountPage(ctk.CTk):

    def __init__(self, player):
        super().__init__()

        self.player = player

        self.title("Аккаунт")
        self.state("zoomed")
        self.minsize(600, 400)

        main_frame = account_page_main_frame.AccountPageMainFrame(self, self.player)
        main_frame.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=1, relheight=1)


def main():
    player = user.User(
        "TestLogin",
        "50",
        "Petya",
        "Petrov",
        "Petrov@gmail.com",
        "123",
        1000,
        0
    )
    account_page = AccountPage(player)
    account_page.mainloop()


if __name__ == "__main__":
    main()
