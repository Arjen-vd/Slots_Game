from Scripts.config_path import CONFIG_PATH, PLAYER_PATH
import json
import time

def main():
    while True:
        with open(CONFIG_PATH, "r") as f:
            config = json.load(f)
        with open(PLAYER_PATH, "r") as f:
            player = json.load(f)
        print("Welkom in de shop!")
        print(f"Uw huidige saldo is: ${round(player["geld"],2)}")
        print("Wat wilt u kopen? (1-4)")
        print(f"1. ${round(config["multi_cost"],2)}: Multiplier * 1.1")
        print(f"2. ${round(config["max_bet_cost"],2)}: Max bet * 1.5")
        print("3. Stats")
        print("4. Terug")
        keuze = input("Keuze: ")

        # Multiplier kopen
        if keuze == "1":
            if player["geld"] > config["multi_cost"]:
                player["geld"] -= config["multi_cost"]
                config["multi_cost"] *= 2.5
                config["multi"] *= 1.1

                with open(CONFIG_PATH, "w") as f:
                    json.dump(config, f)

                with open(PLAYER_PATH, "w") as f:
                    json.dump(player, f)
            else:
                print("Niet genoeg geld!")

        #Max bet kopen
        elif keuze == "2":
            if player["geld"] > config["max_bet_cost"]:
                player["geld"] -= config["max_bet_cost"]
                config["max_bet_cost"] *= 2.5
                config["max_bet"] *= 1.5

                with open(CONFIG_PATH, "w") as f:
                    json.dump(config, f)

                with open(PLAYER_PATH, "w") as f:
                    json.dump(player, f)

        #Stats bekijken
        elif keuze == "3":
            print("----======================----")
            print(f"Je huidige multiplier is {round(config["multi"],2)}")
            print(f"Je huidige max bet is {config["max_bet"]}")
            print("----======================----\n")

        #Terug
        elif keuze == "4":
            return()
        else:
            print("----======================----")
            print("Onjuiste invoer!")
            print("----======================----\n")