# Forritið byrjar á reitnum (1, 1) þ.e.a.s. x = 1 og y = 1 og if setningar tékka á því hvert spilari getur fært sig
# Ef x == 1 og y == 1 getur spilari farið í þessar áttir. Þegar búið er að tékka hvert hægt er að færa sig 
# Kemur input þar sem  spilari er beðinn um átt sem hann vill færa sig og if setning testar hvort hann hafi slegið
# inn valid átt. Þegar það er búið er spilari færður í þá átt sem hann vildi fara. While setning er sett utanum 
# sem runnar ef reiturinn sem spilari er á er einhver annar en (3, 1) og í endann er print skipun sem prentar 
# "Victory"

x = 1
y = 1

<<<<<<< HEAD
# föll fyrir áttir, ef það er Suður eða vestur lækkar input gildið um 1
def sud_vest(a1):
    a1 -= 1
    return a1
# ef það er Norður eða austur hækkar input gildið um 1
=======
# fall fyrir áttir
def sud_vest(a1):
    a1 -= 1
    return a1

>>>>>>> 1f52bb5f42673cc5ed8b8582fffdcd327730eb7b
def nord_aust(a2):
    a2 += 1
    return a2

# main program (hreyfing)
<<<<<<< HEAD
while x != 3 or y != 1: # Runnar þangað til komið er á endapunkt (3, 1)
    # If setningar sem segja hvert hægt er að hreyfa sig eftir staðsetningu
=======
while x != 3 or y != 1:
>>>>>>> 1f52bb5f42673cc5ed8b8582fffdcd327730eb7b
    if x == 1 and y == 1:
        print("You can travel: (N)orth.")
    elif x == 1 and y == 2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
    elif x == 1 and y == 3:
        print("You can travel: (E)ast or (S)outh.")
    elif x == 2 and y == 1:
        print("You can travel: (N)orth.")
    elif x == 2 and y == 2:
        print("You can travel: (S)outh or (W)est.")
    elif x == 2 and y == 3:
        print("You can travel: (E)ast or (W)est.")
    elif x == 3 and y == 2:
        print("You can travel: (N)orth or (S)outh.")
    elif x == 3 and y == 3:
        print("You can travel: (S)outh or (W)est.")

<<<<<<< HEAD
    att = input("Direction: ") # input gildið sem notandi velur

    # If setningar sem segja til um hvort notandi hafi slegið inn gilda átt
    # Bættum ekki við villuleit fyrir aðra stafi en 'neswNESW' þar sem þess var ekki krafist í verkefnalýsingu
    if (x == 1 and y == 1) and att in 'eswESW': # Ef þú ert staðsettur á (1, 1) máttu ekki slá inn neinn af eftirfarandi stöfum 'eswESW'
        print("Not a valid direction!")

    elif (x == 1 and y == 2) and att in 'wW':
        print("Not a valid direction!")

    elif (x == 1 and y == 3) and att in 'nwNW':
        print("Not a valid direction!")

    elif (x == 2 and y == 1) and att in 'eswESW':
        print("Not a valid direction!")

    elif (x == 2 and y == 2) and att in 'neNE':
        print("Not a valid direction!")

    elif (x == 2 and y == 3) and att in 'nsNS':
        print("Not a valid direction!")

    elif (x == 3 and y == 2) and att in 'ewEW':
        print("Not a valid direction!")

    elif (x == 3 and y == 3) and att in 'neNE':
        print("Not a valid direction!")

    # Ef áttin er gild er kallað á tilheyrandi fall
=======
    att = input("Direction: ")

    if x == 1 and y == 1:
        if att in 'eswESW':
            print("Not a valid direction!")
    elif x == 1 and y == 2:
        if att in 'nesNES':
            print("Not a valid direction!")
    elif x == 1 and y == 3:
        if att in 'esES':
            print("Not a valid direction!")
    elif x == 2 and y == 1:
        if att in 'eswESW':
            print("Not a valid direction!")
    elif x == 2 and y == 2:
        if att in 'neNE':
            print("Not a valid direction!")
    elif x == 2 and y == 3:
        if att in 'nsNS':
            print("Not a valid direction!")
    elif x == 3 and y == 2:
        if att in 'ewEW':
            print("Not a valid direction!")
    elif x == 3 and y == 3:
        if att in 'neNE':
            print("Not a valid direction!")
>>>>>>> 1f52bb5f42673cc5ed8b8582fffdcd327730eb7b
    else:
        if att == 'w' or att == 'W':
            x = sud_vest(x)
        elif att == 's' or att == 'S':
            y = sud_vest(y)
        elif att == 'n' or att == 'N':
            y = nord_aust(y)
        elif att == 'e' or att == 'E':
            x = nord_aust(x)
<<<<<<< HEAD
# Virkjast einungis ef while lykkjan hættir, þ.e. þegar komið er á reit (3, 1)
print("Victory!")



=======
    print(x)
    print(y)
print("Victory!")


>>>>>>> 1f52bb5f42673cc5ed8b8582fffdcd327730eb7b
# fall fyrir hvaða áttir má fara
# 1,1 'n'
# 1,2 'nes'
# 1,3 'es'
# 2,1 'n'
# 2,2 'ws'
# 2,3 'we'
# 3,1 'victory'
# 3,2 'ns'
# 3,3 'ws'