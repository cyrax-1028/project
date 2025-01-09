from auth import login, logout, register
from utils import Response, BadRequest
from session import Session
from dto import UserRegisterDTO
from db import add_food, get_foods, update_food, delete_food


def main():
    session = Session()
    while True:
        print("\n1. Ro'yxatdan o'tish (Sign up)")
        print("2. Kirish (Log in)")
        print("3. Chiqish (Log out)")
        print("4. Yangi taom qo'shish")
        print("5. Taomlarni ko‘rish")
        print("6. Taomni yangilash")
        print("7. Taomni o‘chirish")
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
            name = input("Taom nomi: ")
            recipe = input("Taom retsepti: ")
            user_id = session.session.id
            response = add_food(name, recipe, user_id)
            print(response.message)

        elif choice == '5':
            if not session.check_session():
                print("Avval tizimga kiring!")
                continue
            user_id = session.session.id
            response = get_foods(user_id)
            print(response.message)

        elif choice == '6':
            if not session.check_session():
                print("Avval tizimga kiring!")
                continue
            food_id = int(input("Yangilamoqchi bo'lgan taom ID’sini kiriting: "))
            name = input("Yangi nom (bo‘sh qoldirishingiz mumkin): ")
            recipe = input("Yangi retsept (bo‘sh qoldirishingiz mumkin): ")
            response = update_food(food_id, name, recipe)
            print(response.message)

        elif choice == '7':
            if not session.check_session():
                print("Avval tizimga kiring!")
                continue
            food_id = int(input("O'chirmoqchi bo'lgan taom ID’sini kiriting: "))
            response = delete_food(food_id)
            print(response.message)

        elif choice == '8' or choice.lower() == 'exit':
            print("Tizimdan chiqilyapti...")
            break

        else:
            print("Noto'g'ri tanlov!")


if __name__ == "__main__":
    main()