import numpy as np

class Node:

    def __init__(self, name:str, typee:str, scope:str, value:str):
        
        self.name = name
        self.type = typee
        self.scope = scope
        self.value = value
        self.next = None
    

class symbols:

    def __init__(self):
        self.head = None

    def createSymbol(self, name, typee, scope, value):

        newlyCreated = Node(name, typee, scope, value)
        return newlyCreated
    
    def insertIntoTable(self, name, typee, scope, value):

        nodeMini = self.createSymbol(name, typee, scope, value)

        if (self.head == None):
            self.head = nodeMini
        
        elif (self.head != None):

            temp = self.head 
            while (temp!=None):
                if (temp.name == name):
                    print('Symbol Already Exits in Table!!!!\n')
                    return
                
                temp = temp.next
        
            nodeMini.next = self.head
            self.head = nodeMini

        print(f'Symbol {name} inserted Into Table...!\n')
        return
    
    def lookUpForSymbol(self, name):

        temp = self.head

        while(temp!=None):

            if temp.name == name:
                print(f'Found {temp.name}, {temp.type}, {temp.scope}, {temp.value}\n\n')
                return True
            temp = temp.next
        
        print(f'Symbol {name} NOT___FOUND!!!!\n')
    
    def deleteSymbol(self, name):

        temp = self.head
        prev = None

        while temp != None:

            if temp.name == name:

                if prev == None:            #indicating we are still at first node i.e HeadNode...
                    self.head = temp.next   #simply removing the head and moving it forward...
                else :
                    prev.next = temp.next   #simply skipping that node link i.e deleting it...
                
                print(f'Deleted symbol{name} from Table...\n\n')
                return
            
            else:
                prev = temp
                temp = temp.next
        
        print(f'Symbol {name} Not Found.... Try inserting it...\n')

    def displayTable(self):

        temp = self.head
        print('Name\tType\tScope\tValue\n')
        print('---------------------------------\n')

        if self.head == None:
            print('Table is Empty@!!!!. Try inserting new Symbols...!\n')
            return
        
        while temp!=None:
            print(f'{temp.name}\t{temp.type}\t{temp.scope}\t{temp.value}\n')
            print('--------------------------------\n')
            temp = temp.next
        
        return


if __name__ == '__main__':

    symTable = symbols()

    while True:
        print(f'1. InsertSymbol \t 2. LookUpSymbol \n3. DeleteSymbol \t4. DisplayTable\n5.Exit\n')
        x = int(input('Enter choice : '))

        match x:
            case 1: 
                symblName = input('Enter Name : ')
                symblType = input('Enter Type : ')
                symblScope = input('Symbol Scope : ')
                symblValue = input('Enter value : ')

                symTable.insertIntoTable(symblName, symblType, symblScope, symblValue)
            
            case 2:
                symblName = input('Enter Symbol Name to look for : ')
                symTable.lookUpForSymbol(symblName)
            
            case 3:
                symblName = input('Enter Symbol Name to look for : ')
                symTable.deleteSymbol(symblName)
            
            case 4:
                symTable.displayTable()
            
            case 5:
                exit(0)
    
    
