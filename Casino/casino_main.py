import Casino.casino_slot
import Casino.casino_shop
from Scripts.config_path import CONFIG_PATH, PLAYER_PATH
import json


def main_casino():
    while True:
        with open(PLAYER_PATH, "r") as f:
            player = json.load(f)
        with open(CONFIG_PATH, "r") as f:
            config = json.load(f)
        print("""
 __________________________
|                          |
|          CASINO          |
|__________________________|
| ♥ ♦ ♣   ♠ ♥ ♦ ♣   ♠ ♥♦ |
|    __      __      __    |
|   |  |    |  |    |  |   |
|   |__|    |__|    |__|   |
|    __      __      __    |
|   |  |    |  |    |  |   |
|   |__|    |__|    |__|   |
|__________________________|
|      ____    ____        |
|     |    |  |    |       |
|     |____|  |____|       |
|                          |
|__________________________|
 """)
        print("Welkom in het Casino!")
        print(f"Uw huidige saldo is: ${round(player["geld"],2)}")
        print("Waar wilt u naar toe? (1-3)")
        print("1. Fruitmachine")
        print("2. Shop")
        print("3. Uitgang")
        keuze = input("Keuze: ")
        if keuze == "1":
            Casino.casino_slot.slots()
        elif keuze == "2":
            Casino.casino_shop.main()
        elif keuze == "3":
            break
        else:
            print("\nOnjuiste invoer!\n")

