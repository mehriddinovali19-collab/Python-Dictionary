def phonebook_menu(phonebook: dict[str, str]) -> None:
    print("1. Telefon raqamini qo'shish")
    print("2. Telefon raqamini o'chirish")
    print("3. Telefon raqamini ko'rsatish")
    print("4. Chiqish")
    
    choice = input("Tanlovni kiriting: ")

    if choice == "1":
        add_contact(phonebook)
    elif choice == "2":
        remove_contact(phonebook)
    elif choice == "3":
        show_contact(phonebook)
    elif choice == "4":
        print("Dasturdan chiqish...")
    else:
        print("Noto'g'ri tanlov, qayta urinib ko'ring.")

        
        
    
def add_contact(phonebook: dict[str, str]) -> None:
    name = input("Kontakt nomni kiriting: ")
    number = input("Telefon raqamini kiriting: ")
    phonebook[name] = number 
    print(f"{name} kontakt qo'shildi.")

def remove_contact(phonebook: dict[str, str]) -> None:
    name = input("O'chiriladigan kontakt nomini kiriting: ")
    if name in phonebook:
        del phonebook[name]
        print(f"{name} kontakt o'chirildi.")
    else:
        print(f"{name} kontakt topilmadi.")


def show_contact(phonebook: dict[str, str ]) -> None:
    name = input("Ko'rsatiladigan kontakt nomini kiriting: ")
    if name in phonebook:
        print(f"{name}: {phonebook[name]}")
    else:
        print(f"{name} kontakt topilmadi.")

def left_menu() -> None:
    phonebook = {}
    

def main() -> None:
  left_menu()
phonebook = {}
while True:
        phonebook_menu(phonebook)
        if input("Davom etish uchun Enter tugmasini bosing, chiqish uchun 'q' ni kiriting: ") == 'q':
            break

main()