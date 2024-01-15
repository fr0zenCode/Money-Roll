from tkinter import *
from tkinter import ttk
import tkinter.font as TkFont
import re
from user import User

from authorization.functions import get_percentage_of_screen_size_from_full_hd_size


class TopUpTheBalancePage(Tk):

    def __init__(self, player: User):
        super().__init__()

        self.user = player

        # window settings
        self.state("zoomed")

        # screen sizes
        self.percentage_width_from_full_hd = get_percentage_of_screen_size_from_full_hd_size(self)[0] / 100
        self.percentage_height_from_full_hd = get_percentage_of_screen_size_from_full_hd_size(self)[1] / 100

        self.minsize(int(400 * self.percentage_width_from_full_hd), int(500 * self.percentage_height_from_full_hd))

        # fonts
        self.font_for_entries = TkFont.Font(
            family="Arial",
            size=int(11 * (self.percentage_width_from_full_hd + self.percentage_height_from_full_hd) / 2)
        )

        # main frame
        content_frame = Frame(
            background="red",
            width=int(400 * self.percentage_width_from_full_hd),
            height=int(500 * self.percentage_height_from_full_hd)
        )
        content_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # card main frame
        self.card_background_color = "#6A6A6A"
        self.card_entries_background = "#CACACA"

        card_frame = Frame(
            content_frame,
            background=self.card_background_color,
            width=int((200 * 1.5857725083364208966283808818081) * self.percentage_width_from_full_hd),
            height=int(200 * self.percentage_height_from_full_hd)
        )
        card_frame.place(relx=0.5, rely=0.5, anchor=S)

        # card number frame
        ###############################################################################################################
        card_number_frame = Frame(
            card_frame,
            background=self.card_background_color,
            width=int((180 * 1.5857725083364208966283808818081) * self.percentage_width_from_full_hd),
            height=int(80 * self.percentage_height_from_full_hd)
        )
        card_number_frame.place(relx=0.5, rely=0.3, anchor=CENTER)

        self.card_number_validater = (self.register(self.validate_card_number_logic), "%P")

        card_number_lbl = ttk.Label(
            card_number_frame,
            text="Номер банковской карты",
            background=self.card_background_color,
            font=self.font_for_entries,
            foreground=self.card_entries_background
        )
        card_number_lbl.place(relx=0.5, rely=0.25, anchor=CENTER)

        card_number_ent = ttk.Entry(
            card_number_frame,
            width=int(20 * self.percentage_width_from_full_hd),
            font=self.font_for_entries,
            background=self.card_entries_background,
            foreground=self.card_background_color,
            validate="key",
            validatecommand=self.card_number_validater,
            justify=CENTER
        )
        card_number_ent.place(relx=0.5, rely=0.6, anchor=CENTER)
        ###############################################################################################################

        # card date frame
        ###############################################################################################################
        card_date_frame = Frame(
            card_frame,
            background=self.card_background_color,
            width=int((80 * 1.5857725083364208966283808818081) * self.percentage_width_from_full_hd),
            height=int(40 * self.percentage_height_from_full_hd)
        )
        card_date_frame.place(relx=0.3, rely=0.8, anchor=CENTER)

        self.card_date_validater = (self.register(self.card_date_validater_logic), "%P", "%d")

        card_date_lbl = ttk.Label(
            card_date_frame,
            text="ММ/ГГ:",
            background=self.card_background_color,
            font=self.font_for_entries,
            foreground=self.card_entries_background
        )
        card_date_lbl.place(relx=0.3, rely=0.5, anchor=CENTER)

        self.card_date_ent = ttk.Entry(
            card_date_frame,
            width=int(4 * self.percentage_width_from_full_hd),
            font=self.font_for_entries,
            background=self.card_entries_background,
            foreground=self.card_background_color,
            validate="key",
            validatecommand=self.card_date_validater,
            justify=CENTER
        )
        self.card_date_ent.place(relx=0.7, rely=0.5, anchor=CENTER)
        ###############################################################################################################

        # card CVV frame
        ###############################################################################################################
        card_cvv_frame = Frame(
            card_frame,
            background=self.card_background_color,
            width=int((60 * 1.5857725083364208966283808818081) * self.percentage_width_from_full_hd),
            height=int(40 * self.percentage_height_from_full_hd)
        )
        card_cvv_frame.place(relx=0.7, rely=0.8, anchor=CENTER)

        self.card_cvv_validater = (self.register(self.cvv_validater_logic), "%P")

        card_cvv_lbl = ttk.Label(
            card_cvv_frame,
            text="CVV:",
            background=self.card_background_color,
            font=self.font_for_entries,
            foreground=self.card_entries_background
        )
        card_cvv_lbl.place(relx=0.3, rely=0.5, anchor=CENTER)

        self.card_cvv_ent = ttk.Entry(
            card_cvv_frame,
            width=int(3 * self.percentage_width_from_full_hd),
            font=self.font_for_entries,
            background=self.card_entries_background,
            foreground=self.card_background_color,
            validate="key",
            validatecommand=self.card_cvv_validater,
            justify=CENTER
        )
        self.card_cvv_ent.place(relx=0.7, rely=0.5, anchor=CENTER)
        ###############################################################################################################

        # email for recipe frame
        email_for_recipe_frame = Frame(
            content_frame,
            background="yellow",
            width=int((200 * 1.5857725083364208966283808818081) * self.percentage_width_from_full_hd),
            height=int(40 * self.percentage_height_from_full_hd)
        )
        email_for_recipe_frame.place(relx=0.5, rely=0.6, anchor=CENTER)

        email_for_recipe_lbl = ttk.Label(email_for_recipe_frame, text="Email для чека", font=self.font_for_entries)
        email_for_recipe_lbl.place(relx=0.5, rely=0.25, anchor=CENTER)

        email_for_recipe_ent = ttk.Entry(
            email_for_recipe_frame,
            width=(int(25 * self.percentage_width_from_full_hd)),
            font=self.font_for_entries
        )
        email_for_recipe_ent.place(relx=0.5, rely=0.75, anchor=CENTER)

        # submit button frame
        submit_button_frame = Frame(
            content_frame,
            background="blue",
            width=int((120 * 1.5857725083364208966283808818081) * self.percentage_width_from_full_hd),
            height=int(60 * self.percentage_height_from_full_hd)
        )
        submit_button_frame.place(relx=0.5, rely=0.8, anchor=CENTER)

        submit_btn = Button(submit_button_frame, text="Оплатить")
        submit_btn.place(relx=0.5, rely=0.5, anchor=CENTER)

    # TODO: вариант, когда выделены несколько символов и вводится буквенный символ, выделеленные удаляются
    @staticmethod
    def cvv_validater_logic(cvv):
        if len(cvv) > 3:
            return False
        try:
            int(cvv)
            return True
        except ValueError:
            if len(cvv) == 0:
                return True
            return False

    # TODO: оптимизировать условия
    def card_date_validater_logic(self, card_date, action_type):

        if action_type == "0":
            if len(card_date) >= 3:
                if "/" not in card_date:
                    return False
                else:
                    if card_date[2] != "/":
                        return False

        if " " in card_date:
            return False
        if 6 > len(card_date) >= 4:
            try:
                int(card_date[3::])
                return True
            except ValueError:
                return False

        if len(card_date) > 5:
            return False
        if len(card_date) >= 2 and action_type != "0":
            if len(card_date) > 2:
                if card_date[2] == "/":
                    return True
                else:
                    if card_date == " ":
                        return False
                    try:
                        int(card_date)
                    except ValueError:
                        return False
                    self.card_date_ent.delete(0, 10)
                    self.card_date_ent.insert(0, f"{card_date[:2]}/{card_date[2:]}")
                    return False
            try:
                int(card_date)
                self.card_date_ent.delete(0, 5)
                self.card_date_ent.insert(0, f"{card_date}/")
            except ValueError:
                return False
        try:
            int(card_date[:2])
            return True
        except ValueError:
            if len(card_date) == 0:
                return True
            return False

    # TODO: test
    @staticmethod
    def validate_card_number_logic(card_number):
        if len(card_number) > 16:
            return False
        try:
            int(card_number)
            return True
        except ValueError:
            if len(card_number) == 0:
                return True
            return False


def main():
    test_player = User(
        "TestPlayer",
        "7",
        "Ivan",
        "Ivanov",
        "IvanIvanov@mail.ru",
        "123",
        0,
        0
    )
    tup_up_the_balance_page = TopUpTheBalancePage(test_player)
    tup_up_the_balance_page.mainloop()


if __name__ == "__main__":
    main()
