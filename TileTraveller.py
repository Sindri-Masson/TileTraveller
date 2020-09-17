# Forritið byrjar á reitnum (1, 1) þ.e.a.s. x = 1 og y = 1 og if setningar tékka á því hvert spilari getur fært sig
# Ef x == 1 og y == 1 getur spilari farið í þessar áttir. Þegar búið er að tékka hvert hægt er að færa sig 
# Kemur input þar sem  spilari er beðinn um átt sem hann vill færa sig og if setning testar hvort hann hafi slegið
# inn valid átt. Þegar það er búið er spilari færður í þá átt sem hann vildi fara. While setning er sett utanum 
# sem runnar ef reiturinn sem spilari er á er einhver annar en (3, 1) og í endann er print skipun sem prentar 
# "Victory"

x = 1
y = 1

# fall fyrir áttir
def sud_vest(a1):
    a1 -= 1
    return a1

def nord_aust(a2):
    a2 += 1
    return a2

# main program (hreyfing)
while x != 3 or y != 1:
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
    else:
        if att == 'w' or att == 'W':
            x = sud_vest(x)
        elif att == 's' or att == 'S':
            y = sud_vest(y)
        elif att == 'n' or att == 'N':
            y = nord_aust(y)
        elif att == 'e' or att == 'E':
            x = nord_aust(x)
    print(x)
    print(y)
print("Victory!")


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