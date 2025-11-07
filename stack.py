class Node:

    def __init__(self, datas):
        
        self.data = datas
        self.next = None
    
class Stack:

    def __init__(self):
        self.top = None
    
    def isEmpty(self):

        if self.top == None:
            return True
        return False
    
    def push(self, d):
        temp = Node(d)

        if self.isEmpty():
            self.top = temp
            return True
        
        temp.next = self.top
        self.top = temp
        return True
    
    def pop(self):

        if self.isEmpty():
            print('Stack is Empty!!!\n')
            return None
        
        tmpData = self.top.data
        self.top = self.top.next
        return tmpData
    
    def display(self):

        temp = self.top

        if self.isEmpty():
            print("Stack is empty !!\n")
            return False
        
        while(temp):
            print(f'{temp.data} -> ', end='')
            temp = temp.next
        
        print('None')
    
if __name__ == "__main__":

    tmpStack = Stack()

    while(True):
        print('1.PUsh\n2.Pop\n3.Display\n4.Exit\n')
        ch = int(input())

        match ch:
            case 1:
                inp = input('Enter data : ')
                tmpStack.push(inp)

            case 2:
                removed = tmpStack.pop()
                if removed :print(removed)
                tmpStack.display()

            case 3:

                tmpStack.display()

            case 4:

                exit(1)
        



