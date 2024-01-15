from tkinter import *
from tkinter import ttk
import tkinter.font as TkFont
import re
from user_package.user import User

from authorization.functions import get_percentage_of_screen_size_from_full_hd_size
import main


class TopUpTheBalancePage(Tk):

    def __init__(self, player: User):
        super().__init__()

        self.user = player

        # window settings
        self.state("zoomed")
        self.background_color = "#EDE9E6"

        self.configure(background=self.background_color)

        # screen sizes
        self.percentage_width_from_full_hd = get_percentage_of_screen_size_from_full_hd_size(self)[0] / 100
        self.percentage_height_from_full_hd = get_percentage_of_screen_size_from_full_hd_size(self)[1] / 100

        self.minsize(int(400 * self.percentage_width_from_full_hd), int(500 * self.percentage_height_from_full_hd))

        # fonts
        self.font_for_entries = TkFont.Font(
            family="Arial",
            size=int(11 * (self.percentage_width_from_full_hd + self.percentage_height_from_full_hd) / 2)
        )

        self.font_for_email_entry = TkFont.Font(
            family="Arial",
            size=int(9 * (self.percentage_width_from_full_hd + self.percentage_height_from_full_hd) / 2)
        )

        # main frame
        ###############################################################################################################
        content_frame = Frame(
            background=self.background_color,
            width=int(400 * self.percentage_width_from_full_hd),
            height=int(500 * self.percentage_height_from_full_hd)
        )
        content_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        back_btn = Button(
            content_frame,
            text="Назад",
            cursor="hand2",
            justify=CENTER,
            relief=FLAT,
            font=self.font_for_email_entry,
            background="#B12650",
            foreground="#FFFFFF",
            width=int(5 * self.percentage_width_from_full_hd),
            height=int(1 * self.percentage_height_from_full_hd),
            command=self.back_btn_action
        )
        back_btn.place(relx=0, rely=0, anchor=NW)
        ###############################################################################################################

        # card main frame
        ###############################################################################################################
        self.card_background_color = "#6A6A6A"
        self.card_entries_background = "#CACACA"

        card_frame = Frame(
            content_frame,
            background=self.card_background_color,
            width=int((200 * 1.5857725083364208966283808818081) * self.percentage_width_from_full_hd),
            height=int(200 * self.percentage_height_from_full_hd)
        )
        card_frame.place(relx=0.5, rely=0.5, anchor=S)
        ###############################################################################################################

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

        self.card_number_ent = ttk.Entry(
            card_number_frame,
            width=int(20 * self.percentage_width_from_full_hd),
            font=self.font_for_entries,
            background=self.card_entries_background,
            foreground=self.card_background_color,
            validate="key",
            validatecommand=self.card_number_validater,
            justify=CENTER
        )
        self.card_number_ent.place(relx=0.5, rely=0.6, anchor=CENTER)
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
        ###############################################################################################################
        email_for_recipe_frame = Frame(
            content_frame,
            background=self.background_color,
            width=int((200 * 1.5857725083364208966283808818081) * self.percentage_width_from_full_hd),
            height=int(40 * self.percentage_height_from_full_hd)
        )
        email_for_recipe_frame.place(relx=0.5, rely=0.56, anchor=CENTER)

        email_for_recipe_lbl = ttk.Label(
            email_for_recipe_frame,
            text="Email для чека",
            font=self.font_for_email_entry,
            background=self.background_color
        )
        email_for_recipe_lbl.place(relx=0.5, rely=0.30, anchor=CENTER)

        self.email_for_recipe_ent = ttk.Entry(
            email_for_recipe_frame,
            width=(int(25 * self.percentage_width_from_full_hd)),
            font=self.font_for_email_entry,
            justify=CENTER
        )
        self.email_for_recipe_ent.place(relx=0.5, rely=0.8, anchor=CENTER)
        ###############################################################################################################

        # sum for make a payment
        ###############################################################################################################
        sum_frame = Frame(
            content_frame,
            background=self.background_color,
            width=int((120 * 1.5857725083364208966283808818081) * self.percentage_width_from_full_hd),
            height=int(60 * self.percentage_height_from_full_hd),
            borderwidth=1,
            relief=SOLID
        )
        sum_frame.place(relx=0.5, rely=0.72, anchor=CENTER)

        sum_lbl = ttk.Label(
            sum_frame,
            text="Сумма пополнения",
            font=self.font_for_entries,
            background=self.background_color
        )
        sum_lbl.place(relx=0.5, rely=0.25, anchor=CENTER)

        self.sum_validate = (self.register(self.validate_sum), "%P")

        self.sum_ent = ttk.Entry(
            sum_frame,
            font=self.font_for_entries,
            justify=CENTER,
            validate="key",
            validatecommand=self.sum_validate
        )
        self.sum_ent.place(relx=0.5, rely=0.75, anchor=CENTER)
        ###############################################################################################################

        # submit button frame
        ###############################################################################################################
        submit_button_frame = Frame(
            content_frame,
            background=self.background_color,
            width=int((120 * 1.5857725083364208966283808818081) * self.percentage_width_from_full_hd),
            height=int(60 * self.percentage_height_from_full_hd)
        )
        submit_button_frame.place(relx=0.5, rely=0.9, anchor=CENTER)

        submit_btn = Button(
            submit_button_frame,
            text="Оплатить",
            cursor="hand2",
            justify=CENTER,
            relief=FLAT,
            font=self.font_for_entries,
            background="#94C1C0",
            width=int(10 * self.percentage_width_from_full_hd),
            height=int(2 * self.percentage_height_from_full_hd),
            command=self.submit_btn_action
        )
        submit_btn.place(relx=0.5, rely=0.5, anchor=CENTER)
        ###############################################################################################################

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

    @staticmethod
    def validate_sum(input_sum):
        if len(input_sum) == 0:
            return True
        if " " in input_sum or len(input_sum) > 4:
            return False
        try:
            int(input_sum)
            return True
        except ValueError:
            return False

    def back_btn_action(self):
        player = self.user
        self.destroy()
        main_window = main.MainWindow(player)
        main_window.mainloop()

    def submit_btn_action(self):
        card_number = self.card_number_ent.get()
        card_date = self.card_date_ent.get()
        card_cvv = self.card_cvv_ent.get()
        email_for_recipe = self.email_for_recipe_ent.get()
        sum_for_increase = int(self.sum_ent.get())

        client = self.user

        if len(card_number) == 16 and len(card_date) == 5 and len(card_cvv) == 3 and email_for_recipe and int(
                sum_for_increase) > 0:
            client.increase_balance(sum_for_increase)
            self.destroy()
            main_window = main.MainWindow(client)
            main_window.mainloop()
        else:
            print("Проверьте данные")


def main_this_window():
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
    main_this_window()
