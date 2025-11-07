top = -1

stackSize = 4

stackS = [_ for _ in range(stackSize)]

def push(d):

    global top
    if top >= stackSize:
        print("Stack full!!")
        return False
    
    top = top + 1
    stackS[top] = d
    return

def pop():
    global top
    if top == -1:
        print('Stack Empty!!')
        return False
    temp = stackS[top]
    top = top - 1
    return temp

def display():
    global top
    if top == -1:
        print("Stack is Empty!!")
        return True
    x = top
    while(x>=0):
        print(f'{stackS[x]} -> ', end='')
        x = x-1
    print("End")

push(10)
push(20)
push(30)
display()
pop()

display()
