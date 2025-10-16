from Scripts.config_path import CONFIG_PATH, PLAYER_PATH
import Casino.casino_main
import json

def main_stad():
    while True:
        with open(PLAYER_PATH, "r") as f:
            player = json.load(f)
        with open(CONFIG_PATH, "r") as f:
            config = json.load(f)
        print(r"""
                                                  ..======.       
                                                  ||::: : |
     .====.,                                 .~.===: : : :|   ..===.
     |.::'||      .=====.,    ..=======.~,   |"|: :|::::::|   ||:::|=====|
  ___| :::|!__.,  |:::::|!_,   |: :: ::|"|l_l|"|:: |:;;:::|___!| ::|: : :|
 |: :|::: |:: |!__|; :: |: |===::: :: :|"||_||"| : |: :: :|: : |:: |:::::|
 |:::| _::|: :|:::|:===:|::|:::|:===F=:|"!/|\!"|::F|:====:|::_:|: :|::__:|
 !_[]![_]_!_[]![]_!_[__]![]![_]![_][I_]!//_:_\\![]I![_][_]!_[_]![]_!_[__]!
 -----------------------------------"---''''```---"-----------------------
 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ |= _ _:_ _ =| _ _ _ _ _ _ _ _ _ _ _ _
                                     |=    :    =|                
_____________________________________L___________J________________________
--------------------------------------------------------------------------
 """)
        print("Welkom in de stad!")
        print(f"Uw huidige saldo is: ${round(player["geld"],2)}")
        print(f"Uw huidige stamina is: ♥{round(player["stamina"],2)}")
        print("Wat wil je doen?")
        print("1. Casino")
        print("2. Debug")
        print("3. Stop")
        keuze = input("Keuze: ")
        if keuze == "1":
            Casino.casino_main.main_casino()
        elif keuze == "2":
            while True:
                print("1. RESET")
                print("2. TERUG")
                kies = input("Keuze: ")
                if kies == "1":
                    # Reset player stats
                    player["geld"] = 1000
                    player["stamina"] = 100

                    # Reset Config
                    config["multi"] = 1.0
                    config["multi_cost"] = 50
                    config["max_bet"] = 10
                    config["max_bet_cost"] = 1000
                    config["color"] = 0
                    config["bet"] = 1
                    config["kans_0"] = 50
                    config["kans_*"] = 25
                    config["kans_$"] = 15
                    config["kans_7"] = 10
                    config["kans_kruis"] = 1
                    with open(CONFIG_PATH, "w") as f:
                        json.dump(config, f)
                    with open(PLAYER_PATH, "w") as f:
                        json.dump(player, f)
                    print("Reset geslaagd!")
                elif kies == "2":
                    break
        elif keuze == "3":
            break
        else:
            print("Ongeldige invoer!")

if __name__ == "__main__":
    main_stad()