import os
import sys
ijssalon = 1
bak = 1
def smaken():
    global smaak
    smaak = str(input("Welke smaak wilt u voor bolletje"+ str(bol) +" A) Aardbei, C) Chocolade, M) Munt of V) Vanille?")).lower()
    if smaak == "a":
        smaak= "Aarbei"
    elif smaak == "c":
        smaak= "Chocolade"
    elif smaak == "m":
        smaak= "Munt"
    elif smaak == "v":
        smaak= "Vanille"
    else:
        print("Sorry, dat snap ik niet...")
def bestellen():
    bestellen = input("Hier is uw "+ deel+ " " + smaak +" met " + str(bol)+ " bolletje(s). Wilt u nog meer bestellen? (Y/N)").lower()
    if bestellen == "y":
        ijssalon+0
    elif bestellen == "n":
        print("Bedankt en tot ziens.")
        sys.exit()
        
    else:
        print("Sorry, dat snap ik niet...")
        ijssalon+0

print("Welkom bij Papi Gelato. ")
while ijssalon == 1:
    bol = int(input("Hoeveel bolletjes ijs wilt u? : "))
    while bol >8:
        print("Sorry, zulke grote bakken hebben we niet")
        bol = int(input("Hoeveel bolletjes ijs wilt u? : "))
    if bol >=1 and bol <=3:
        while bak == 1:
            hoorntje = str(input("Wilt u deze " + str(bol) + " bolletje(s) in A) een hoorntje of B) een bakje? : ")).lower()
            if hoorntje == "a":
                deel = "hoorntje"
                smaken()
                bestellen()
            elif hoorntje == "b":
                deel = "bakje"
                smaken()
                bestellen()
            else:
                print("Sorry, dat snap ik niet")
    elif bol >=4 and bol <=8:
        deel = "bakje"
        smaken()
        bestellen()
    else:
        print("Sorry, ik snap het niet...")