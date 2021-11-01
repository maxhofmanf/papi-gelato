import os
import sys
ijssalon = 1
bak = 1
qtybakje = 0
qtyhoorn = 0
def bestellen():
    bestellen = input("Hier is uw "+ deel +" met " + str(bol)+ " bolletje(s). Wilt u nog meer bestellen? (Y/N)")
    if bestellen == "y":
        ijssalon+0
    elif bestellen == "n":
        print("Bedankt en tot ziens.")
        print(qtybakje)
        
    else:
        print("Sorry, dat snap ik niet...")
        ijssalon+0
print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")
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
                qtyhoorn += 1
                bestellen()
            elif hoorntje == "b":
                deel = "bakje"
                qtybakje += 1 
                bestellen()

            else:
                print("Sorry, dat snap ik niet")
    elif bol >=4 and bol <=8:
        deel = "bakje"
        qtybakje += 1 
        bestellen()
    else:
        print("Sorry, ik snap het niet...")