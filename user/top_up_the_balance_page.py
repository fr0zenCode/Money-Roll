from tkinter import *
from tkinter import ttk

from authorization.functions import get_percentage_of_screen_size_from_full_hd_size


class TopUpTheBalancePage(Tk):

    def __init__(self):
        super().__init__()

        # window settings
        self.state("zoomed")

        # screen sizes
        self.percentage_width_from_full_hd = get_percentage_of_screen_size_from_full_hd_size(self)[0] / 100
        self.percentage_height_from_full_hd = get_percentage_of_screen_size_from_full_hd_size(self)[1] / 100

        self.minsize(int(400 * self.percentage_width_from_full_hd), int(500 * self.percentage_height_from_full_hd))

        # main frame
        content_frame = Frame(
            background="red",
            width=int(400 * self.percentage_width_from_full_hd),
            height=int(500 * self.percentage_height_from_full_hd)
        )
        content_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # card main frame
        card_frame = Frame(
            content_frame,
            background="green",
            width=int((200 * 1.5857725083364208966283808818081) * self.percentage_width_from_full_hd),
            height=int(200 * self.percentage_height_from_full_hd)
        )
        card_frame.place(relx=0.5, rely=0.5, anchor=S)

        # card number frame
        card_number_frame = Frame(
            card_frame,
            background="yellow",
            width=int((180 * 1.5857725083364208966283808818081) * self.percentage_width_from_full_hd),
            height=int(80 * self.percentage_height_from_full_hd)
        )
        card_number_frame.place(relx=0.5, rely=0.3, anchor=CENTER)

        card_number_lbl = ttk.Label(card_number_frame, text="Номер банковской карты")
        card_number_lbl.place(relx=0.5, rely=0.25, anchor=CENTER)

        card_number_ent = ttk.Entry(card_number_frame, width=int(30 * self.percentage_width_from_full_hd))
        card_number_ent.place(relx=0.5, rely=0.6, anchor=CENTER)

        # card date frame
        card_date_frame = Frame(
            card_frame,
            background="blue",
            width=int((80 * 1.5857725083364208966283808818081) * self.percentage_width_from_full_hd),
            height=int(40 * self.percentage_height_from_full_hd)
        )
        card_date_frame.place(relx=0.3, rely=0.8, anchor=CENTER)

        card_date_lbl = ttk.Label(card_date_frame, text="ММ/ГГ:")
        card_date_lbl.place(relx=0.3, rely=0.5, anchor=CENTER)

        card_date_ent = ttk.Entry(card_date_frame, width=int(7 * self.percentage_width_from_full_hd))
        card_date_ent.place(relx=0.7, rely=0.5, anchor=CENTER)

        # card CVV frame
        card_cvv_frame = Frame(
            card_frame,
            background="blue",
            width=int((60 * 1.5857725083364208966283808818081) * self.percentage_width_from_full_hd),
            height=int(40 * self.percentage_height_from_full_hd)
        )
        card_cvv_frame.place(relx=0.7, rely=0.8, anchor=CENTER)

        card_cvv_lbl = ttk.Label(card_cvv_frame, text="CVV:")
        card_cvv_lbl.place(relx=0.3, rely=0.5, anchor=CENTER)

        card_cvv_ent = ttk.Entry(card_cvv_frame, width=int(5 * self.percentage_width_from_full_hd))
        card_cvv_ent.place(relx=0.7, rely=0.5, anchor=CENTER)

        # email for recipe frame
        email_for_recipe_frame = Frame(
            content_frame,
            background="yellow",
            width=int((200 * 1.5857725083364208966283808818081) * self.percentage_width_from_full_hd),
            height=int(40 * self.percentage_height_from_full_hd)
        )
        email_for_recipe_frame.place(relx=0.5, rely=0.6, anchor=CENTER)

        email_for_recipe_lbl = ttk.Label(email_for_recipe_frame, text="Адрес электронной почты для выставления чека")
        email_for_recipe_lbl.place(relx=0.5, rely=0.25, anchor=CENTER)

        # submit button frame
        submit_button_frame = Frame(
            content_frame,
            background="blue",
            width=int((120 * 1.5857725083364208966283808818081) * self.percentage_width_from_full_hd),
            height=int(60 * self.percentage_height_from_full_hd)
        )
        submit_button_frame.place(relx=0.5, rely=0.8, anchor=CENTER)


def main():
    tup_up_the_balance_page = TopUpTheBalancePage()
    tup_up_the_balance_page.mainloop()


if __name__ == "__main__":
    main()
