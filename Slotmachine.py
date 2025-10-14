import random



def slots(geld):
    print("\nWelkom bij Fruit Blitz Royale")
    print("Elke jackpot wordt vermenigvuldigd met uw inzet!")
    print("==============")
    print("=  Inzet $1  =")
    print("==============")
    print("=  000 = 2   =")
    print("=  *** = 3  =")
    print("=  $$$ = 5  =")
    print("==============")
    while True:
        try:
            keuze = float(input("Wat is je inzet? (1$-10$) "))
            if keuze > geld:
                print("Niet genoeg geld!")
            elif keuze > 10:
                print("Ongeldige invoer!")
            elif keuze < 1:
                print("Ongeldige invoer!")
            else:
                sloticons = ["0", "$", "*"]
                random1 = random.choice(sloticons)
                random2 = random.choice(sloticons)
                random3 = random.choice(sloticons)
                if random1 == "0" and random2 == "0" and random3 == "0":
                    winst = 2 * keuze
                elif random1 == "*" and random2 == "*" and random3 == "*":
                    winst = 3 * keuze
                elif random1 == "$" and random2 == "$" and random3 == "$":
                    winst = 5 * keuze
                else:
                    winst = 0
                geld = geld - keuze + winst
                if geld <= 0:
                    break
                else:
                    print("=============")
                    print("=           =")
                    print(f"=   {str(random1)} {str(random2)} {str(random3)}   =")
                    print("=           =")
                    print("=============")
                    print(f"WINST: ${winst}")
                    print(f"Je hebt nog {round(geld, 2)} euro over")
        except ValueError:
            print("Ongeldige invoer")

