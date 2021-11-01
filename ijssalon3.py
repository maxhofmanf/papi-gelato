import os
import sys
ijssalon = 1
weetniet ="Sorry, ik snap het niet..."
bak = 0
bakgeld = 0
hoorngeld = 0
bakjeaantal = 0
hoornaantal = 0
bakje = 0
hoorntotal= 0 
bakjetotal = 0
aantalbol = 0
bollen = 0

#1
def smaken():
    global smaak
    for x in range(aantalbol, 0 , -1):
        smaak = str(input("Welke smaak wilt u voor bolletje "+ str(x) +" A) Aardbei, C) Chocolade, M) Munt of V) Vanille?  ")).lower()
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
    global bakjetotal ,bakjeaantal ,hoornaantal ,hoorntotal, bollen
    bestellen = input("Hier is uw "+ deel+ " " + smaak +" met " + str(aantalbol)+ " bolletje(s). Wilt u nog meer bestellen? (Y/N)").lower()
    if bestellen == "y":
        bakjetotal += bakgeld
        hoorntotal += hoorngeld
        bollen += aantalbol
        begin()
    elif bestellen == "n":
        bakjetotal += bakgeld
        hoorntotal += hoorngeld
        bollen += aantalbol
        print('---------["Papi Gelato]---------')
        hoorntotal= "{:.2f}".format(round(float(hoorngeld)*1 , 2))
        bakjetotal= "{:.2f}".format(round(float(bakgeld)*1 , 2))
        print("bakje     ", bakjeaantal," x 0,75 = ", float(bakjetotal))
        print("hoorntje  ", hoornaantal," x 1,25 = ",float(hoorntotal))
        total = "{:.2f}".format(round(float(bollen)*1.1 , 2))
        print("bolletjes", bollen ,"x 1.10 =", total)
        print("Bedankt en tot ziens.")
        print("--------------------------------")

    else:
        print(weetniet)
        ijssalon+0

#3
print("Welkom bij Papi Gelato. ")
def begin():

    global hoornaantal, hoorngeld, bakgeld ,bak, bakjeaantal,bollen , bakje, deel, aantalbol
    while ijssalon == 1:
        aantalbol = int(input("Hoeveel bolletjes ijs wilt u? : "))
        if aantalbol >8:
            print("Sorry, zulke grote bakken hebben we niet")
        elif aantalbol >=1 and aantalbol <=3:
                hoorntje = str(input("Wilt u deze " + str(aantalbol) + " bolletje(s) in A) een hoorntje of B) een bakje? : ")).lower()
                if hoorntje == "a":
                    deel = "hoorntje"
                    hoorngeld += 1.25
                    hoornaantal += 1
                    smaken()
                    bestellen()
                elif hoorntje == "b":
                    deel = "bakje"
                    bakgeld += 0.75
                    bakjeaantal += 1
                    smaken()
                    bestellen()
                else:
                    print(weetniet)

        elif aantalbol >=4 and aantalbol <=8:
            deel = "bakje"
            bakgeld += 0.75
            bakjeaantal += 1
            smaken()
            bestellen()
        else:
            print(weetniet)

begin()
