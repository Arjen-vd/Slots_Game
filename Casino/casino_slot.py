from Scripts.config_path import CONFIG_PATH, PLAYER_PATH
import random
import json

def slots():
    # Config en speler laden
    with open(CONFIG_PATH, "r") as r:
        config = json.load(r)
    with open(PLAYER_PATH, "r") as f:
        player = json.load(f)

    print("\nWelkom bij Fruit Blitz Royale")
    print("Elke jackpot wordt vermenigvuldigd met uw inzet!")
    print(f"Uw huidige saldo is: ${round(player['geld'],2)}")
    try:
        keuze = float(input(f"Wat is je inzet? (1$ - ${config["max_bet"]}) "))
    except ValueError:
        print("Ongeldige invoer!")
        return slots()

    if keuze > player["geld"]:
        print("Niet genoeg geld!")
        return slots()
    elif keuze > float(config["max_bet"]) or keuze < 1:
        print("Ongeldige invoer!")
        return slots()

    config["bet"] = keuze
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f)

    multi = float(config["multi"])

    print("=============")
    print("=   BLITZ   =")
    print("=============")
    print(f"000 = {2 * keuze * multi}")
    print(f"*** = {10 * keuze * multi}")
    print(f"$$$ = {50 * keuze * multi}")
    print(f"777 = {1000 * keuze * multi}")
    print("=============")


    while True:
        spin = input("\nDruk 1 om te spinnen of 99 om te stoppen: ")

        if spin == "99":
            print("Je hebt het spel verlaten.")
            break
        elif spin != "1":
            print("Ongeldige keuze, probeer opnieuw.\n")
            return slots()

        sloticons = ["0", "*", "$", "7"]
        weights = [
            config["kans_0"],
            config["kans_*"],
            config["kans_$"],
            config["kans_7"]
        ]

        random1 = random.choices(sloticons, weights, k=1)[0]
        random2 = random.choices(sloticons, weights, k=1)[0]
        random3 = random.choices(sloticons, weights, k=1)[0]

        if random1 == "0" and random2 == "0" and random3 == "0":
            winst = 2 * keuze * float(config["multi"])
        elif random1 == "*" and random2 == "*" and random3 == "*":
            winst = 10 * keuze * float(config["multi"])
        elif random1 == "$" and random2 == "$" and random3 == "$":
            winst = 50 * keuze * float(config["multi"])
        elif random1 == "7" and random2 == "7" and random3 == "7":
            winst = 1000 * keuze * float(config["multi"])
        else:
            winst = 0

        player["geld"] = player["geld"] - keuze + winst
        if player["geld"] <= 0:
            player["geld"] = 0
            with open(PLAYER_PATH, "w") as f:
                json.dump(player, f)
            print("Je hebt geen geld meer over!")
            return

        with open(PLAYER_PATH, "w") as f:
            json.dump(player, f)

        print("=============")
        print("=   BLITZ   =")
        print("=============")
        print(f"=   {random1} {random2} {random3}   =")
        print("=============")
        print(f"Je inzet is: {keuze}")
        print(f"WINST: ${round(winst,2)}")
        print(f"Je hebt nog ${round(player['geld'], 2)} over")
