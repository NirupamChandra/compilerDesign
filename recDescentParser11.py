pos = 0
inpstr = ''

def handleError():
    global pos
    print(f'parsing failed at {pos}')
    exit(1)

def peek():

    return inpstr[pos]

def match(x):
    global pos

    if inpstr[pos] == x:
        print(f'Matched ~> {x} <~')
        pos+=1
        return
    handleError()

def L():
    
    print('Entering L..')
    if S():
        if Lprime():
            print('Exiting L..')
            return True
        
    return False

def Lprime():
    print("Entering L'.. ")

    if peek() == ',':
        match(',')
        if S():
            if Lprime():
                print("Exiting L' ..")
                return True
        
        return False
    
    else:
        print("L' -> Epsilon\n")
        return True
        
def S():
    print('Entering S..')

    if peek() == '(':
        match('(')
        if L():
            if peek() == ')':
                match(')')
                print('Exiting S..\n')
                return True
            else:
                handleError()
    elif peek() == 'a':
        match('a')
        print('S -> a')
        return True
    else:
        handleError()

if __name__ == '__main__':

    inpstr = input("ENter expression : ")+'\n'

    if S() and inpstr[pos] == '\n':
        print('Parsing sucessful!!')
    else:
        handleError()

