from auth import login, logout, register
from utils import Response, BadRequest
from session import Session
from dto import UserRegisterDTO


def main():
    while True:
        print("1. Ro'yxatdan o'tish (Sign up)")
        print("2. Kirish (Log in)")
        print("3. Chiqish (Log out)")
        print("4. Chiqish (exit)")

        choice = input("Tanlovni kiriting (1/2/3/4/exit): ")

        if choice == '1':
            username = input("Username: ")
            password = input("Password: ")
            user_dto = UserRegisterDTO(username, password)
            response = register(user_dto.username, user_dto.password)
            print(response.message)

        elif choice == '2':
            username = input("Username: ")
            password = input("Password: ")
            response = login(username, password)
            print(response.message)

        elif choice == '3':
            response = logout()
            print(response.message)

        elif choice == '4' or choice.lower() == 'exit':
            print("Tizimdan chiqilyapti...")
            break

        else:
            print("Noto'g'ri tanlov!")


if __name__ == "__main__":
    main()