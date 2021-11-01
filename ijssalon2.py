import os
import sys
ijssalon = 1
weetniet ="Sorry, ik snap het niet..."
bollen =0
bak = 1
bakje = 0
hoorntjes = 0
bakjeaantal = 0
hoornaantal = 0

#1
def smaken():
    global smaak
    for x in range(bol, 0 , -1):
        smaak = str(input("Welke smaak wilt u voor bolletje "+ str(x) +" A) Aardbei, C) Chocolade, M) Munt of V) Vanille?")).lower()
        if smaak == "a":
            smaak= "Aarbei"
        elif smaak == "c":
            smaak= "Chocolade"
        elif smaak == "m":
            smaak= "Munt"
        elif smaak == "v":
            smaak= "Vanille"
        else:
            print(weetniet)



#2
def bestellen():
    global bestel
    bestellen = input("Hier is uw "+ deel+ " " + smaak +" met " + str(bol)+ " bolletje(s). Wilt u nog meer bestellen? (Y/N)").lower()
    if bestellen == "y":
        return ijssalon
    elif bestellen == "n":
        print('---------["Papi Gelato]---------')
        print(" ")
        print(" ")
        print("bakje     ", bakjeaantal," x 0,75 = ", float(bakje))
        print("hoorntje  ", hoornaantal," x 1,25 = ",float(hoorntjes))
        total = "{:.2f}".format(round(float(bollen)*1.1 , 2))
        print("bolletjes", bol ,"x 1.10 =", total)
        print("Bedankt en tot ziens.")
        print()
        sys.exit() 
    else:
        print(weetniet)
        ijssalon+0

#3
print("Welkom bij Papi Gelato. ")
while ijssalon == 1:
    bol = int(input("Hoeveel bolletjes ijs wilt u? : "))
    while bol >8:
        print("Sorry, zulke grote bakken hebben we niet")
        bol = int(input("Hoeveel bolletjes ijs wilt u? : "))
    if bol >=1 and bol <=3:
        bollen += bol
        while bak == 1:
            hoorntje = str(input("Wilt u deze " + str(bol) + " bolletje(s) in A) een hoorntje of B) een bakje? : ")).lower()
            if hoorntje == "a":
                deel = "hoorntje"
                hoorntjes += 1.25
                hoornaantal += 1
                smaken()
                bestellen()
            elif hoorntje == "b":
                deel = "bakje"
                bakje += 0.75
                bakjeaantal += 1
                smaken()
                bestellen()
            else:
                print(weetniet)
    elif bol >=4 and bol <=8:
        deel = "bakje"
        bakje += 0.75
        bollen += bol
        bakjeaantal += 1
        smaken()
        bestellen()
    else:
        print(weetniet)