import Slotmachine
import Shop
import json

def main_menu():

    while True:
        with open("config.json", "r") as f:
            data = json.load(f)
            if data["color"] == 1:
                print("\033[92m")  # Groen
            elif data["color"] == 2:
                print("\033[94m")  # Blue
            elif data["color"] == 3:
                print("\033[95m")  # Roze
            else:
                print("\033[0m")
        print("\nWelkom in het Casino!")
        print(f"Uw huidige saldo is: ${round(data["geld"],2)}")
        print("Waar wilt u naar toe? (1-3)")
        print("1. Fruitmachine")
        print("2. Shop")
        print("3. Reset")
        print("4. Uitgang")
        keuze = input("Keuze: ")
        if keuze == "1":
            Slotmachine.slots()
        elif keuze == "2":
            Shop.main()
        elif keuze == "3":
            with open("config.json", "w") as f:
                data["geld"] = 100
                data["multi"] = 1.0
                data["multi_cost"] = 50
                data["max_bet"] = 10
                data["max_bet_cost"] = 1000
                data["color"] = 0
                json.dump(data, f)
                print("\nJe game is gereset!")
        elif keuze == "4":
            break
        else:
            print("\nOnjuiste invoer!\n")

main_menu()