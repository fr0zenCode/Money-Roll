from tkinter import *
from game import Game


this_game = Game()

app = Tk()
app.title("Лудоман3001")
app.geometry("1000x1000")


def work():

    this_game.run()

    bad_result = f'Вы в МИНУСЕ на {this_game.total * -1} рублей. Позор, лудоман!'
    good_result = f'Вы в ПЛЮСЕ на {this_game.total} рублей.'
    text = f'{bad_result if this_game.total < 0 else good_result}\n\n'

    total_win_label.config(text=text)

    current_win_label.config(text=this_game.current_win_text)


main_button = Button(text="Испытать удачу", font=100, command=work)

main_button.pack(side=BOTTOM, pady=40)

current_win_label = Label(app, text=f"Вы выиграли {0} рублей", font=100)
total_win_label = Label(app, text=f"Вы в плюсе на {0} рублей", font=100)

current_win_label.pack(pady=(500, 0))
total_win_label.pack(pady=(10, 0))


def main():
    app.mainloop()


if __name__ == '__main__':
    main()

