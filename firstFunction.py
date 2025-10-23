
def isTerminal(sym:str):
    return not sym.isupper()

def getFirst(symbol:str, grammar:dict, first_set:dict, visited:set):

    if symbol in first_set:
        return first_set[symbol]
    
    if symbol in visited:
        return ()
    
    visited.add(symbol)
    first = set()

    if isTerminal(symbol):
        first.add(symbol)
        return first
    
    for x in grammar.get(symbol, []):    
        first_symbol = x[0]
        sub_first = getFirst(first_symbol, grammar, first_set, visited)
        first.update(sub_first)

    first_set[symbol] = first
    return first
        

if __name__ == '__main__':

    n = int(input("Enter no.of inputs : "))
    grammar = {}

    for _ in range(n):

        line = input().replace(" ", "")
        lhs, rhs = line.split("->")
        rhs_chars = rhs.split("|")

        grammar[lhs] = [list(x) for x in rhs_chars]

    print(grammar.items())

    first_set = {}

    for nonTerminals in grammar:
        getFirst(nonTerminals, grammar, first_set, set())

    for symbol in grammar:
        print(f'{symbol} = {first_set.get(symbol)}')