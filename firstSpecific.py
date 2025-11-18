firstE = []
firstT = []
firstF = []

def add(set_list, c):
    if c not in set_list:
        set_list.append(c)

def computeF():
    add(firstF, '(')
    add(firstF, 'i')

def computeT():
    computeF()
    for c in firstF:
        add(firstT, c)

def computeE():
    computeT()
    for c in firstT:
        add(firstE, c)

def printSet(name, set_list):
    print(f"FIRST({name}) = {{ ", end="")
    for i, c in enumerate(set_list):
        print(c, end="")
        if i != len(set_list) - 1:
            print(" , ", end="")
    print(" }")

def main():
    computeE()
    printSet("E", firstE)
    printSet("T", firstT)
    printSet("F", firstF)

main()