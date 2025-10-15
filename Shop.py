import json
import time

def main():
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
        print("Welkom in de shop!")
        print(f"Uw huidige saldo is: ${round(data["geld"],2)}")
        print("Wat wilt u kopen? (1-3)")
        print(f"1. ${round(data["multi_cost"],2)}: Multiplier * 1.25")
        print(f"2. ${round(data["max_bet_cost"],2)}: Max bet * 2")
        print("3. Win de game: $100.000.000")
        print("4. Kies een andere kleur")
        print("5. Stats")
        print("6. Terug")
        keuze = input("Keuze: ")

        # Multiplier kopen
        if keuze == "1":
            if data["geld"] > data["multi_cost"]:
                with open("config.json", "w") as f:
                    data["geld"] -= data["multi_cost"]
                    data["multi_cost"] *= 1.5
                    data["multi"] *= 1.25
                    json.dump(data, f)
            else:
                print("Niet genoeg geld!")

        #Max bet kopen
        elif keuze == "2":
            if data["geld"] > data["max_bet_cost"]:
                with open("config.json", "w") as f:
                    data["geld"] -= data["max_bet_cost"]
                    data["max_bet_cost"] *= 2.5
                    data["max_bet"] *= 2
                    json.dump(data, f)

        elif keuze == "3":
            if data["geld"] > 100000000:
                for line in range(1000):
                    print("YOU WON")
                    time.sleep(0.1)
                exit()
            else:
                break

        #Kleur veranderen
        elif keuze == "4":
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
                print("\nKies een kleur:")
                print("1. $100.000:    Groen")
                print("2. $1.000.000:  Blauw")
                print("3. $10.000.000: Roze")
                print("4. Terug")
                kleurkeuze = input("Keuze: ")
                if kleurkeuze == "1":
                    if data["geld"] > 100000:
                        with open("config.json", "r") as f:
                            data = json.load(f)
                            data["color"] = 1
                            data["geld"] -= 100000
                        with open("config.json", "w") as f:
                            json.dump(data, f)
                        print("Kleur aangepast!")
                    else:
                        print("Niet genoeg geld!")
                elif kleurkeuze == "2":
                    if data["geld"] > 1000000:
                        with open("config.json", "r") as f:
                            data = json.load(f)
                            data["color"] = 2
                            data["geld"] -= 1000000
                        with open("config.json", "w") as f:
                            json.dump(data, f)
                        print("Kleur aangepast!")
                    else:
                        print("Niet genoeg geld!")
                elif kleurkeuze == "3":
                    if data["geld"] > 10000000:
                        with open("config.json", "r") as f:
                            data = json.load(f)
                            data["color"] = 3
                            data["geld"] -= 10000000
                        with open("config.json", "w") as f:
                            json.dump(data, f)
                        print("Kleur aangepast!")
                    else:
                        print("Niet genoeg geld!")
                elif kleurkeuze == "4":
                    break

        #Stats bekijken
        elif keuze == "5":
            print(f"Je huidige multiplier is {round(data["multi"],2)}")
            print(f"Je huidige max bet is {data["max_bet"]}")

        #Terug
        elif keuze == "6":
            return()
        else:
            print("\nOnjuiste invoer!\n")