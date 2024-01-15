from tkinter import *
from tkinter import ttk
import authorization.functions as functions
import user_package.user as user


class AccountPage(Tk):

    def __init__(self, player):
        super().__init__()

        self.title("Аккаунт")
        self.state("zoomed")

        # screen sizes
        self.percentage_width_from_full_hd = functions.get_percentage_of_screen_size_from_full_hd_size(self)[0] / 100
        self.percentage_height_from_full_hd = functions.get_percentage_of_screen_size_from_full_hd_size(self)[1] / 100

        self.minsize(int(451 * self.percentage_width_from_full_hd), int(451 * self.percentage_height_from_full_hd))

        # main frame
        ###############################################################################################################
        content_frame = Frame(
            background="green",
            width=int(400 * self.percentage_width_from_full_hd),
            height=int(300 * self.percentage_height_from_full_hd)
        )
        content_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        ###############################################################################################################

        # player's photo frame
        ###############################################################################################################
        photo_frame = Frame(
            content_frame,
            background="blue",
            width=int(120 * self.percentage_width_from_full_hd),
            height=int(160 * self.percentage_height_from_full_hd)
        )
        photo_frame.place(relx=0.04, rely=0.05, anchor=NW)
        ###############################################################################################################

        # photo selector frame
        ###############################################################################################################
        photo_selector_frame = Frame(
            content_frame,
            background="yellow",
            width=int(120 * self.percentage_width_from_full_hd),
            height=int(50 * self.percentage_height_from_full_hd)
        )
        photo_selector_frame.place(relx=0.19, rely=0.7, anchor=CENTER)
        ###############################################################################################################

        # user info frame
        ###############################################################################################################
        user_info_frame = Frame(
            content_frame,
            background="black",
            width=int(200 * self.percentage_width_from_full_hd),
            height=int(200 * self.percentage_height_from_full_hd)
        )
        user_info_frame.place(relx=0.7, rely=0.42, anchor=CENTER)
        ###############################################################################################################

        # buttons frame
        ###############################################################################################################
        buttons_frame = Frame(
            content_frame,
            background="white",
            width=int(200 * self.percentage_width_from_full_hd),
            height=int(40 * self.percentage_height_from_full_hd)
        )
        buttons_frame.place(relx=0.5, rely=0.89, anchor=CENTER)
        ###############################################################################################################
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
