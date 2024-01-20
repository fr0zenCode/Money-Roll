from tkinter import *
import customtkinter as ctk

import connection
from settings import (background_color, buttons_background_color, buttons_hover_background_color, areas_background,
                      user as db_user, password as db_password, database as db_name)

import user_package.user as user
import main_window_package.main_window as main_window


class TopUpTheBalancePage(ctk.CTk):

    def __init__(self, player: user.User):
        super().__init__()

        self.player = player

        # window settings
        self.state("zoomed")

        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        self.minsize(int(self.screen_width / 1.7), int(self.screen_height / 1.7))

        self.configure(fg_color=background_color)

        self.content_frame = ctk.CTkFrame(self, fg_color=background_color)
        self.content_frame.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=1, relheight=1)

        self.connection = connection.Connection()

        # back button
        self.back_btn = self.create_back_button(self.content_frame)

        self.main_font = ("Arial", 12)
        self.font_for_important_objects = ("Arial", 13)

        # card main frame
        ###############################################################################################################
        self.card_background_color = "#5D6086"
        self.card_entries_background = "#344B6A"
        self.card_labels_text_color = "#44D7E2"

        card_frame = ctk.CTkFrame(
            self.content_frame,
            corner_radius=30,
            fg_color=self.card_background_color,
        )
        card_frame.place(relx=0.5, rely=0.1, anchor=N, relwidth=0.3, relheight=0.29)
        ###############################################################################################################

        # card number frame
        ###############################################################################################################
        card_number_frame = ctk.CTkFrame(
            card_frame,
            fg_color=self.card_background_color,
            border_width=2,
            border_color=self.card_entries_background
        )
        card_number_frame.place(relx=0.5, rely=0.3, anchor=CENTER, relwidth=0.8, relheight=0.35)
        self.card_number_validater = (self.register(self.validate_card_number_logic), "%P")

        card_number_lbl = ctk.CTkLabel(
            card_number_frame,
            text="Номер банковской карты",
            text_color=self.card_labels_text_color,
            font=self.main_font
        )
        card_number_lbl.place(relx=0.5, rely=0.1, anchor=N, relwidth=0.9, relheight=0.3)

        self.card_number_ent = ctk.CTkEntry(
            card_number_frame,
            fg_color=self.card_entries_background,
            validate="key",
            validatecommand=self.card_number_validater,
            justify=CENTER,
            font=self.main_font
        )
        self.card_number_ent.place(relx=0.5, rely=0.5, anchor=N, relwidth=0.8, relheight=0.4)
        ###############################################################################################################

        # card date frame
        ###############################################################################################################
        card_date_frame = ctk.CTkFrame(
            card_frame,
            fg_color=self.card_background_color
        )
        card_date_frame.place(relx=0.1, rely=0.8, anchor=W, relwidth=0.4, relheight=0.3)

        self.card_date_validater = (self.register(self.card_date_validater_logic), "%P")

        card_date_mouth_lbl = ctk.CTkLabel(
            card_date_frame,
            text="ММ:"
        )
        card_date_mouth_lbl.place(relx=0.1, rely=0.5, anchor=W, relwidth=0.2, relheight=0.5)
        self.card_date_mouth_ent = ctk.CTkEntry(
            card_date_frame,
            justify="center",
            validate="key",
            validatecommand=self.card_date_validater
        )
        self.card_date_mouth_ent.place(relx=0.3, rely=0.5, anchor=W, relwidth=0.2, relheight=0.5)

        card_date_slash_lbl = ctk.CTkLabel(card_date_frame, text="/")
        card_date_slash_lbl.place(relx=0.5, rely=0.5, anchor=W, relwidth=0.05, relheight=0.5)

        card_date_year_lbl = ctk.CTkLabel(card_date_frame, text="ГГ:")
        card_date_year_lbl.place(relx=0.55, rely=0.5, anchor=W, relwidth=0.2, relheight=0.5)
        self.card_date_year_ent = ctk.CTkEntry(
            card_date_frame,
            justify="center",
            validate="key",
            validatecommand=self.card_date_validater
        )
        self.card_date_year_ent.place(relx=0.75, rely=0.5, anchor="w", relwidth=0.2, relheight=0.5)
        ###############################################################################################################

        # card CVV frame
        ###############################################################################################################
        card_cvv_frame = ctk.CTkFrame(
            card_frame,
            fg_color=self.card_background_color
        )
        card_cvv_frame.place(relx=0.9, rely=0.8, anchor=E, relwidth=0.35, relheight=0.3)

        self.card_cvv_validater = (self.register(self.cvv_validater_logic), "%P")

        card_cvv_lbl = ctk.CTkLabel(
            card_cvv_frame,
            text="CVV:",
            bg_color=self.card_background_color,
            text_color=self.card_labels_text_color,
            font=self.main_font
        )
        card_cvv_lbl.place(relx=0.1, rely=0.5, anchor=W, relwidth=0.4)

        self.card_cvv_ent = ctk.CTkEntry(
            card_cvv_frame,
            fg_color=self.card_entries_background,
            validate="key",
            validatecommand=self.card_cvv_validater,
            justify=CENTER,
            font=self.main_font
        )
        self.card_cvv_ent.place(relx=0.9, rely=0.5, anchor=E, relwidth=0.4)
        ###############################################################################################################

        # email for recipe frame
        ###############################################################################################################
        email_for_recipe_frame = ctk.CTkFrame(
            self.content_frame,
            fg_color=background_color
        )
        email_for_recipe_frame.place(relx=0.5, rely=0.45, anchor=N, relwidth=0.55, relheight=0.07)

        email_for_recipe_lbl = ctk.CTkLabel(
            email_for_recipe_frame,
            text="Email для чека",
            font=self.main_font
        )
        email_for_recipe_lbl.place(relx=0.5, rely=0.25, anchor=CENTER, relwidth=0.8, relheight=0.5)

        self.email_for_recipe_ent = ctk.CTkEntry(
            email_for_recipe_frame,
            justify=CENTER,
            font=self.main_font,
            fg_color=areas_background
        )
        self.email_for_recipe_ent.place(relx=0.5, rely=0.75, anchor=CENTER, relwidth=0.8, relheight=0.5)
        ###############################################################################################################

        # sum for make a payment
        ###############################################################################################################
        sum_frame = ctk.CTkFrame(
            self.content_frame,
            fg_color=background_color
        )
        sum_frame.place(relx=0.5, rely=0.6, anchor=N, relwidth=0.25, relheight=0.1)

        sum_lbl = ctk.CTkLabel(
            sum_frame,
            text="Сумма пополнения",
            font=self.font_for_important_objects
        )
        sum_lbl.place(relx=0.5, rely=0.25, anchor=CENTER, relwidth=0.9, relheight=0.5)

        self.sum_validate = (self.register(self.validate_sum), "%P")

        self.sum_ent = ctk.CTkEntry(
            sum_frame,
            justify=CENTER,
            validate="key",
            validatecommand=self.sum_validate,
            font=self.font_for_important_objects,
            fg_color=areas_background
        )
        self.sum_ent.place(relx=0.5, rely=0.75, anchor=CENTER, relwidth=0.9, relheight=0.5)
        ###############################################################################################################

        # submit button frame
        ###############################################################################################################
        submit_button_frame = ctk.CTkFrame(self.content_frame, fg_color=background_color)
        submit_button_frame.place(relx=0.5, rely=0.8, anchor=CENTER, relwidth=0.25, relheight=0.1)

        submit_btn = ctk.CTkButton(
            submit_button_frame,
            text="Оплатить",
            cursor="hand2",
            border_color="white",
            border_width=2,
            fg_color=buttons_background_color,
            hover_color=buttons_hover_background_color,
            command=self.submit_btn_action
        )
        submit_btn.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.85, relheight=0.7)
        ###############################################################################################################

    def create_back_button(self, master):

        back_btn = ctk.CTkButton(
            master,
            text="Назад",
            cursor="hand2",
            command=self.back_btn_action,
            fg_color=buttons_background_color,
            hover_color=buttons_hover_background_color,
            border_width=1,
            border_color="grey"
        )
        back_btn.place(relx=0.01, rely=0.01, anchor=NW, relwidth=0.07, relheight=0.035)
        return back_btn

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

    @staticmethod
    def card_date_validater_logic(card_date):

        if card_date:

            if len(card_date) > 2:
                return False
            if " " in card_date:
                return False

            try:
                int(card_date)
                return True
            except ValueError:
                return False

        return True

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
        player = self.player
        self.destroy()
        new_window = main_window.MainWindow(player)
        new_window.mainloop()

    def submit_btn_action(self):
        card_number = self.card_number_ent.get()

        card_date_mouth = self.card_date_mouth_ent.get()
        card_date_year = self.card_date_year_ent.get()

        card_cvv = self.card_cvv_ent.get()
        email_for_recipe = self.email_for_recipe_ent.get()
        sum_for_increase = int(self.sum_ent.get())

        client = self.player

        if (len(card_number) == 16 and len(card_date_mouth) == 2 and len(card_date_year) == 2 and len(card_cvv) == 3
                and email_for_recipe and int(sum_for_increase) > 0):
            client.increase_balance(sum_for_increase)

            if self.connection.get_connection() is None:
                self.connection.make_connection(user=db_user, password=db_password, database=db_name)

            self.connection.get_cursor().execute(f"""
            UPDATE "authorization-data" 
            SET balance = '{self.player.get_balance()}' 
            WHERE login = '{self.player.login}' 
            AND password = '{self.player.get_password()}' 
            AND email = '{self.player.user_email}';"""
                                                 )

            self.connection.get_connection().commit()

            self.destroy()
            new_window = main_window.MainWindow(self.player)
            new_window.mainloop()

        else:
            print("Проверьте данные")


def main_this_window():
    test_player = user.User(
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
