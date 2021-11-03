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
topkost = 0
sprinkle = 0
sauze = 0
toptotal = 0
totalkost = 0


#2
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


#3
def topping():
    global topkost
    print("wilt u er nog een topping bij?")
    top = input("A.Slagroom, B.Sprinkles, C.Caramel saus D. geen topping : ").lower()
    if top == "a":
        topkost += 0.50
        print("+ slagroom")
    elif top == "b":
        topkost += 0.30 * aantalbol
        print("+ sprinkles")
    elif top == "c":
        if deel == "bakje":
            print("+ caramel saus")
            topkost += 0.90
        elif deel == "hoorntje":
            print("+ caramel saus")
            topkost += 0.60
    elif top == "d":
        print()
    else:
        print(weetniet)
    bestellen()



#4
def bestellen():
    global bakjetotal ,bakjeaantal ,hoornaantal ,hoorntotal, bollen, toptotal, totalkost
    bestellen = input("Hier is uw "+ deel+ " " + smaak +" met " + str(aantalbol)+ " bolletje(s). Wilt u nog meer bestellen? (Y/N)").lower()
    if bestellen == "y":
        bakjetotal += bakgeld
        hoorntotal += hoorngeld
        bollen += aantalbol
        toptotal += topkost
        begin()
    elif bestellen == "n":
        bakjetotal += bakgeld
        hoorntotal += hoorngeld
        bollen += aantalbol
        toptotal += topkost
        totalkost += toptotal
        totalkost += bakjetotal
        totalkost += hoorntotal        
        print('---------["Papi Gelato]---------')
        hoorntotal= "{:.2f}".format(round(float(hoorngeld)*1 , 2))
        bakjetotal= "{:.2f}".format(round(float(bakgeld)*1 , 2))
        toptotal = "{:.2f}".format(round(float(topkost)*1 , 2))

        print("toppings  1 x",toptotal,"= ",toptotal)
        print("bakje     ", bakjeaantal," x 0,75 = ", float(bakjetotal))
        print("hoorntje  ", hoornaantal," x 1,25 = ",float(hoorntotal))

        total = "{:.2f}".format(round(float(bollen)*1.1 , 2))
        print("bolletjes", bollen ,"x 1.10 =", total)
        totalkost += bollen * 1.10
        totalkost = "{:.2f}".format(round(float(totalkost)*1 , 2))  

        print("--------------------------------")
        print("total               =",float(totalkost))
        print("Bedankt en tot ziens.")
        print("--------------------------------")
        sys.exit()
    else:
        print(weetniet)
        ijssalon+0

#1
print("Welkom bij Papi Gelato. ")
def begin():

    global hoornaantal, hoorngeld, bakgeld ,bak, bakjeaantal , bakje, deel, aantalbol
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
                    topping()
                elif hoorntje == "b":
                    deel = "bakje"
                    bakgeld += 0.75
                    bakjeaantal += 1
                    smaken()
                    topping()
                else:
                    print(weetniet)

        elif aantalbol >=4 and aantalbol <=8:
            deel = "bakje"
            bakgeld += 0.75
            bakjeaantal += 1
            smaken()
            topping()
        else:
            print(weetniet)

begin()
