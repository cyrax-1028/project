from auth import login, logout, register
from utils import Response, BadRequest
from session import Session
from dto import UserRegisterDTO
from db import add_todo, get_todos, update_todo, delete_todo


def main():
    session = Session.new()  # Yagona sessiya ob'ekti
    while True:
        print("\n1. Ro'yxatdan o'tish (Sign up)")
        print("2. Kirish (Log in)")
        print("3. Chiqish (Log out)")
        print("4. Yangi todo qo'shish")
        print("5. Todo’larni ko‘rish")
        print("6. Todo’ni yangilash")
        print("7. Todo’ni o‘chirish")
        print("8. Chiqish (exit)")

        choice = input("\nTanlovni kiriting (1-8 yoki exit): ")

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

        elif choice == '4':
            if not session.check_session():
                print("Avval tizimga kiring!")
                continue
            title = input("Todo nomi: ")
            description = input("Todo tavsifi: ")
            todo_type = input("Todo turi (created, in_progress, completed): ")
            user_id = session.session.id
            response = add_todo(title, description, todo_type, user_id)
            print(response.message)

        elif choice == '5':
            if not session.check_session():
                print("Avval tizimga kiring!")
                continue
            user_id = session.session.id
            response = get_todos(user_id)
            print(response.message)

        elif choice == '6':
            if not session.check_session():
                print("Avval tizimga kiring!")
                continue
            todo_id = int(input("Yangilamoqchi bo'lgan todo ID’sini kiriting: "))
            title = input("Yangi nom (bo‘sh qoldirishingiz mumkin): ")
            description = input("Yangi tavsif (bo‘sh qoldirishingiz mumkin): ")
            todo_type = input("Yangi turi (created, in_progress, completed): ")
            response = update_todo(todo_id, title, description, todo_type)
            print(response.message)

        elif choice == '7':
            if not session.check_session():
                print("Avval tizimga kiring!")
                continue
            todo_id = int(input("O'chirmoqchi bo'lgan todo ID’sini kiriting: "))
            response = delete_todo(todo_id)
            print(response.message)

        elif choice == '8' or choice.lower() == 'exit':
            print("Tizimdan chiqilyapti...")
            break

        else:
            print("Noto'g'ri tanlov!")


if __name__ == "__main__":
    main()