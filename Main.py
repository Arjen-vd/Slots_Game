import Slotmachine
geld = 100

def main_menu():
    while True:
        print("Welkom in het Casino!")
        print("Waar wilt u naar toe? (1-2)")
        print("1. Fruitmachine ")
        print("2. Uitgang")
        keuze = input("Keuze: ")
        if keuze == "1":
            Slotmachine.slots(geld)
        elif keuze == "2":
            break
        else:
            print("\nOnjuiste invoer!\n")

main_menu()