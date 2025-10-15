import json

def main():
    while True:
        with open("config.json", "r") as f:
            data = json.load(f)
        print("\nWelkom in de shop!")
        print(f"Uw huidige saldo is: ${data["geld"]}")
        print("Wat wilt u kopen? (1-3)")
        print(f"1. ${data["multi_cost"]}: Multiplier + 0.1")
        print("2. Stats")
        print("3. Terug")
        keuze = input("Keuze: ")
        if keuze == "1":
            if data["geld"] > data["multi_cost"]:
                with open("config.json", "w") as f:
                    data["geld"] -= data["multi_cost"]
                    data["multi_cost"] *= 2
                    data["multi"] += 0.1
                    json.dump(data, f)
            else:
                print("Niet genoeg geld!")
        elif keuze == "2":
            print(f"Je huidige multiplier is {round(data["multi"],2)}")
        elif keuze == "3":
            return()
        else:
            print("\nOnjuiste invoer!\n")