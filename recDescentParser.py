pos = 0
inpstr = ''

def handleError():
    global pos
    print(f'Parsing failed at position : {pos}' )
    exit(1)

def peek():
    return inpstr[pos]

def match(x:str):

    global pos

    if inpstr[pos] == x:
        print(f'Matched ~> {x} <~ \n')
        pos+=1
    else:
        handleError()

def E():

    print("..Entering E")

    if T():
        if Eprime():
            print('Exiting E ..')
            return True
        
    return False

def Eprime():

    print("..Entering E'")
    
    if peek() == '+':
        match('+')
        if T():
            if Eprime():
                print("Exiting E' ..")
                return True
            else:
                return False
        else:
            return False
    else:
        print("E' -> Epsilon!")
        return True

def T():
    print('..Entering T')

    if F():
        if Tprime():
            print('Exiting T ..')
            return True
    
    return False

def Tprime():

    print("..Entering T'")

    if peek() == '*':
        match('*')
        if F():
            if Tprime():
                print("Exiting T' ..")
                return True
            else:
                return False
        else:
            return False
    else:
        print("T' -> Epsilon!")
        return True
    
def F():
    print('..Entering F')
    if peek() == '(':
        match('(')
        if E():
            if peek() == ')':
                match(')')
                print('Exiting F ..')
                return True
            else:
                handleError()
                return False
            
        else:
            return False
    
    elif peek() == 'i':
        match('i')
        print('F -> i')
        return True
    
    else:
        handleError()
        return False


if __name__ == '__main__':

    inpstr = input('Enter expression : ')+'\n'
    
    if E() and inpstr[pos]=='\n':
        print('Successful parsing !!')
    else:
        handleError()
        



    
            
