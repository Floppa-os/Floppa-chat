from client.client import MessengerClient

def main():
    client = MessengerClient()
    print("Добро пожаловать в Floppa chat!")

    while True:
        print("\n1. Регистрация\n2. Вход\n3. Отправить сообщение\n4. Посмотреть сообщения\n5. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            username = input("Имя пользователя: ")
            password = input("Пароль: ")
            if client.register(username, password):
                print("Регистрация успешна!")
            else:
                print("Пользователь уже существует.")

        elif choice == '2':
            username = input("Имя пользователя: ")
            password = input("Пароль: ")
            if client.login(username, password):
                print("Вход выполнен!")
            else:
                print("Неверный логин или пароль.")

        elif choice == '3':
            if not client.username:
                print("Сначала войдите в аккаунт.")
                continue
            recipient = input("Кому: ")
            text = input("Сообщение: ")
            if client.send_message(recipient, text):
                print("Сообщение отправлено!")
            else:
                print("Ошибка отправки.")

        elif choice == '4':
            if not client.username:
                print("Сначала войдите в аккаунт.")
                continue
            msgs = client.get_messages()
            if msgs:
                for sender, text in msgs:
                    print(f"{sender}: {text}")
            else:
                print("Нет сообщений.")

        elif choice == '5':
            print("Прощайте!")
            break

        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()
