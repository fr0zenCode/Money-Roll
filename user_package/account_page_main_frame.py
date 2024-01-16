from tkinter import *
from tkinter import ttk
import tkinter.font as TkFont
from PIL import Image, ImageTk
import user_package.user as user

class AccountPageMainFrame(Frame):

    def __init__(self, player: user.User):
        super().__init__()

        self.player = player

        self.main_font = self.create_font_for_lbl(12)

        self.image_original = Image.open("../img/avatars/default_avatar_image.jpg")
        image_tk = ImageTk.PhotoImage(self.image_original)

        self.resized_tk = None

        # main frame
        ###############################################################################################################
        content_frame = Frame(
            background="green",
            # width=int(800 * self.percentage_width_from_full_hd),
            # height=int(500 * self.percentage_height_from_full_hd)
        )
        content_frame.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=1, relheight=1)
        content_frame.pack_propagate(False)

        ###############################################################################################################

        ###############################################################################################################
        ###############################################################################################################

        upper_frame = Frame(content_frame, background="yellow")
        upper_frame.place(relx=0, rely=0, relwidth=1, relheight=0.85)

        avatar_frame = Frame(upper_frame, background="red")
        avatar_frame.place(relx=0, rely=0, relwidth=0.33, relheight=1)

        photo_frame = Frame(avatar_frame, background="blue")
        photo_frame.place(relwidth=1, relheight=0.75)

        self.canvas = Canvas(photo_frame, background="white", bd=0, highlightthickness=0, relief=RIDGE)
        self.canvas.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.99, relheight=0.99)

        self.canvas.bind("<Configure>", self.stretch_image)

        photo_selector_frame = Frame(avatar_frame, background="pink")
        photo_selector_frame.place(relx=0, rely=1, relwidth=1, relheight=0.25, anchor=SW)

        photo_variants = ("<Выберите аватар>", "Лудоман", "Озорник", "Плохой парень")
        combobox_variable = StringVar()
        combobox_variable.set(photo_variants[0])

        photo_selector_combobox = ttk.Combobox(
            photo_selector_frame,
            textvariable=combobox_variable,
            font=self.main_font
        )
        photo_selector_combobox["values"] = photo_variants
        photo_selector_combobox.pack(
            pady=(20, 60))

        # user's data
        users_data_frame = Frame(upper_frame, background="green")
        users_data_frame.place(relx=0.33, rely=0, relwidth=0.67, relheight=1, anchor=NW)

        self.first_name_variable = StringVar(value=self.player.first_name)
        self.last_name_variable = StringVar(value=self.player.last_name)
        self.current_password_variable = StringVar(value="")
        self.new_password_variable = StringVar(value="")
        self.confirm_new_password_variable = StringVar(value="")

        self.first_name_ent = self.create_entry(users_data_frame, "Имя:", "grey").configure(textvariable=self.first_name_variable)
        self.last_name_ent = self.create_entry(users_data_frame, "Фамилия:", "grey").configure(textvariable=self.last_name_variable)
        self.current_password_ent = self.create_entry(users_data_frame, "Старый пароль:", "grey").configure(textvariable=self.current_password_variable)
        self.new_password_ent = self.create_entry(users_data_frame, "Новый пароль:", "grey").configure(textvariable=self.new_password_variable)
        self.confirm_new_password_ent = self.create_entry(users_data_frame, "Подтверждение пароля:",
                                                          "grey").configure(textvariable=self.confirm_new_password_variable)

        # bottom
        ###############################################################################################################
        bottom_frame = Frame(content_frame, background="blue")
        bottom_frame.place(relx=0, rely=0.85, anchor=NW, relwidth=1, relheight=0.15)

        buttons_frame = Frame(bottom_frame, background="red")
        buttons_frame.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.3, relheight=0.5)

        cancel_btn = Button(buttons_frame, text="Отмена")
        submit_btn = Button(buttons_frame, text="Принять")
        cancel_btn.place(relx=0, rely=0.5, anchor=W, relwidth=0.45, relheight=1)
        submit_btn.place(relx=1, rely=0.5, anchor=E, relwidth=0.45, relheight=1)
        ###############################################################################################################

        self.mainloop()

    def stretch_image(self, event):

        width = event.width
        height = event.height

        resized_image = self.image_original.resize((width, height))
        self.resized_tk = ImageTk.PhotoImage(resized_image)

        self.canvas.create_image(0, 0, image=self.resized_tk, anchor=NW)

    @staticmethod
    def create_font_for_lbl(font_size):
        font = TkFont.Font(family="Arial", size=int(font_size))
        return font

    def create_entry(self, parent_frame, text, bg_color):
        frame = Frame(parent_frame, background=bg_color)
        frame.pack(expand=True, fill=BOTH)
        frame_lbl = ttk.Label(frame, text=text, font=self.main_font, background=bg_color)
        frame_ent = ttk.Entry(frame, font=self.main_font, background=bg_color, justify=CENTER)
        frame_lbl.place(relx=0.1, rely=0.5, anchor=W, relwidth=0.5, relheight=0.3)
        frame_ent.place(relx=0.6, rely=0.5, anchor=W, relwidth=0.3, relheight=0.3)
        return frame_ent
