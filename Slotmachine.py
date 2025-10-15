import random
import json



def slots():
    with open("config.json", "r") as f:
        data = json.load(f)
    print("\nWelkom bij Fruit Blitz Royale")
    print("Elke jackpot wordt vermenigvuldigd met uw inzet!")
    print(f"Uw huidige saldo is: {round(data["geld"],2)}")
    print("==============")
    print("=  Inzet $1  =")
    print("==============")
    print("=  000 = 5   =")
    print("=  *** = 10  =")
    print("=  $$$ = 15  =")
    print("==============")
    while True:
        try:
            keuze = float(input(f"Wat is je inzet? (1$-${data["max_bet"]}) (99 om te stoppen) "))
            if keuze == 99:
                break
            elif keuze > data["geld"]:
                print("Niet genoeg geld!")
            elif keuze > float(data["max_bet"]):
                print("Ongeldige invoer!")
            elif keuze < 1:
                print("Ongeldige invoer!")
            else:
                sloticons = ["0", "$", "*"]
                random1 = random.choice(sloticons)
                random2 = random.choice(sloticons)
                random3 = random.choice(sloticons)
                if random1 == "0" and random2 == "0" and random3 == "0":
                    winst = 5 * keuze * float(data["multi"])
                elif random1 == "*" and random2 == "*" and random3 == "*":
                    winst = 10 * keuze * float(data["multi"])
                elif random1 == "$" and random2 == "$" and random3 == "$":
                    winst = 15 * keuze * float(data["multi"])
                else:
                    winst = 0
                data["geld"] = data["geld"] - keuze + winst
                with open("config.json", "w") as f:
                    json.dump(data, f)

                if data["geld"] <= 0:
                    data["geld"] = 0
                    with open("config.json", "w") as f:
                        json.dump(data, f)
                    return()
                else:
                    print("=============")
                    print("=           =")
                    print(f"=   {str(random1)} {str(random2)} {str(random3)}   =")
                    print("=           =")
                    print("=============")
                    print(f"WINST: ${round(winst,2)}")
                    print(f"Je hebt nog ${round(data["geld"], 2)} over")
        except ValueError:
            print("Ongeldige invoer")

