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
        print("Wat wil je doen?")
        print("1. Casino")
        print("2. Stop")
        keuze = input("Keuze: ")
        if keuze == "1":
            Casino.casino_main.main_casino()
        elif keuze == "2":
            break
        else:
            print("Ongeldige invoer!")

if __name__ == "__main__":
    main_stad()