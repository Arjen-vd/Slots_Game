import Slotmachine
import json

def main_menu():
    while True:
        with open("config.json", "r") as f:
            data = json.load(f)
        print("Welkom in het Casino!")
        print(f"Uw huidige saldo is: ${data["geld"]}")
        print("Waar wilt u naar toe? (1-2)")
        print("1. Fruitmachine ")
        print("2. Uitgang")
        keuze = input("Keuze: ")
        if keuze == "1":
            Slotmachine.slots()
        elif keuze == "2":
            break
        else:
            print("\nOnjuiste invoer!\n")

main_menu()