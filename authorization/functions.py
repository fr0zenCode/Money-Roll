def get_percentage_of_screen_size_from_full_hd_size(self):
    normal_screen_width = 1920
    normal_screen_height = 1080

    device_screen_width = self.winfo_screenwidth()
    device_screen_height = self.winfo_screenheight()

    percentage_width = (device_screen_width / normal_screen_width) * 100
    percentage_height = (device_screen_height / normal_screen_height) * 100

    return percentage_width, percentage_height

