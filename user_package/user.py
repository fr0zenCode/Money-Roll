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
        self.__balance = balance

        self._chance_for_big_win = chance_for_big_win

    def __str__(self):
        return f'{self.first_name} {self.last_name}, id: {self.user_id}'

    def get_password(self):
        return self.__password

    def get_balance(self):
        return self.__balance

    def take_money_for_game(self):
        self.__balance -= 50

    def increase_balance(self, money):
        self.__balance += money

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




if __name__ == '__main__':
    main()
