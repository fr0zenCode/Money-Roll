from uuid import UUID
from random import choice


class User:

    def __init__(self, login, user_id, first_name, last_name, email, password, balance, chance_for_big_win):

        self.auth = False

        self.login = login
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.user_email = email

        self.__password = password
        self._balance = balance

        self._chance_for_big_win = chance_for_big_win

    def __str__(self):
        return f'{self.first_name} {self.last_name}, id: {self.user_id}'

    def get_password(self):
        return self.__password




    def log_in(self):

        text = "Введите BACK для выхода \nВведите РЕГИСТРАЦИЯ, чтобы перейти на окно регистрации \n\nВаш ответ: "
        information = ""

        login = input(f"Введите логин: \n\n{text}")
        if login != 'BACK':
            self.login = login
        else:
            return

        with open('../bd.txt') as file:
            for string in file:
                index = string.find(':')
                if login == string[:index]:
                    information = string.split(':')

                if information:

                    while not self.auth:

                        password = input(f"Введите пароль: \n\n{text}")
                        if password != 'BACK':
                            self.__password = password
                        else:
                            return

                        if information[4] == password:
                            self.auth = True
                            self.login = login
                            self.first_name = information[2]
                            self.last_name = information[3]
                            self.__password = password
                            self.__balance = information[4]
                            self.__chance_for_big_win = information[5]
                            print(f"Здравствуйте, {self.first_name}! Вы успешно авторизованы в системе!")
                            return
                        else:
                            print("Неверный пароль, попробуйте снова!")
                            continue
                else:
                    print("Логин не найден")
                    return

    def sign_in(self):

        text = "Введите BACK для выхода"
        pass


def main():

    player = User()

    player.log_in()

    # text = "1. Авторизоваться \n2. Зарегистрироваться \n\nВаш ответ: "
    #
    # while not player.auth:
    #
    #     users_answer = input(text)
    #
    #     if users_answer == "1":
    #         player.log_in()
    #     if users_answer == "2":
    #         player.sign_in()
    #
    #
    #
    #
    # first_names = ['Иван', 'Илья', 'Емиль', 'Чингизхан', 'Вячеслав']
    # last_names = ['Жигун', 'Иванов', 'Багиров', 'Чурка', 'Разуваев']
    # user_id = UUID('{12345678-1234-5678-1234-567812345678}')
    # password = 'Password123'
    # balance = 0
    # chance_for_big_win = 0
    # user = User(choice(first_names), choice(last_names), password, balance, chance_for_big_win, user_id)
    # print(user)


if __name__ == '__main__':
    main()
