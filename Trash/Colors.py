#-------- KLEUREN AANZETTEN --------#

#with open(CONFIG_PATH, "r") as f:
#    config = json.load(f)
#    if config["color"] == 1:
#        print("\033[92m")  # Groen
#    elif config["color"] == 2:
#        print("\033[94m")  # Blue
#    elif config["color"] == 3:
#        print("\033[95m")  # Roze
#    else:
#        print("\033[0m")

#-------- KLEUREN KOPEN --------#


#elif keuze == "4":
#while True:
#    with open(CONFIG_PATH, "r") as f:
#        config = json.load(f)
#        if config["color"] == 1:
#            print("\033[92m")  # Groen
#        elif config["color"] == 2:
#            print("\033[94m")  # Blue
#        elif config["color"] == 3:
#            print("\033[95m")  # Roze
#        else:
#            print("\033[0m")
#    print("\nKies een kleur:")
#    print("1. $100.000:    Groen")
#    print("2. $1.000.000:  Blauw")
#    print("3. $10.000.000: Roze")
#    print("4. Terug")
#    kleurkeuze = input("Keuze: ")
#    if kleurkeuze == "1":
#        if player["geld"] > 100000:
#            config["color"] = 1
#            player["geld"] -= 100000
#            with open(CONFIG_PATH, "w") as f:
#                json.dump(config, f)
#            with open(PLAYER_PATH, "w") as f:
#                json.dump(player, f)
#            print("Kleur aangepast!")
#        else:
#            print("Niet genoeg geld!")
#    elif kleurkeuze == "2":
#        if player["geld"] > 1000000:
#            config["color"] = 2
#            player["geld"] -= 1000000
#            with open(CONFIG_PATH, "w") as f:
#                json.dump(config, f)
#            with open(PLAYER_PATH, "w") as f:
#                json.dump(player, f)
#            print("Kleur aangepast!")
#        else:
#            print("Niet genoeg geld!")
#    elif kleurkeuze == "3":
#        if player["geld"] > 10000000:
#            config["color"] = 3
#            player["geld"] -= 10000000
#            with open(CONFIG_PATH, "w") as f:
#                json.dump(config, f)
#            with open(PLAYER_PATH, "w") as f:
#                json.dump(player, f)
#            print("Kleur aangepast!")
#        else:
#            print("Niet genoeg geld!")
#   elif kleurkeuze == "4":
#        break