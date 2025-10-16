import re

# Define C language keywords
keywords = {
    "int", "float", "if", "else", "while", "return", "for",
    "char", "double", "void", "break", "continue", "do"
}

# Regular expressions for tokens
token_patterns = {
    "COMMENT_MULTI": re.compile(r"/\*[\s\S]*?\*/"),
    "COMMENT_SINGLE": re.compile(r"//.*"),
    "IDENTIFIER": re.compile(r"\b[_a-zA-Z][_a-zA-Z0-9]*\b"),
    "CONSTANT": re.compile(r"\b\d+(\.\d+)?\b"),
    "OPERATOR": re.compile(r"[+\-*/=<>]"),
    "SYMBOL": re.compile(r"[;{},()]+"),
}

def lexical_analyzer(code):
    tokens = []

    # First handle comments separately (since they can contain other symbols)
    while True:
        multi = token_patterns["COMMENT_MULTI"].search(code)
        single = token_patterns["COMMENT_SINGLE"].search(code)
        if multi:
            tokens.append(("<Comment>", multi.group()))
            code = code.replace(multi.group(), " ")
        elif single:
            tokens.append(("<Comment>", single.group()))
            code = code.replace(single.group(), " ")
        else:
            break

    # Tokenize remaining code
    words = re.findall(r"[A-Za-z_]\w*|\d+\.\d+|\d+|[+\-*/=<>;{},()]", code)

    for word in words:
        if word in keywords:
            tokens.append(("<Keyword>", word))
        elif re.fullmatch(token_patterns["CONSTANT"], word):
            tokens.append(("<Constant>", word))
        elif re.fullmatch(token_patterns["IDENTIFIER"], word):
            tokens.append(("<Identifier>", word))
        elif re.fullmatch(token_patterns["OPERATOR"], word):
            tokens.append(("<Operator>", word))
        elif re.fullmatch(token_patterns["SYMBOL"], word):
            tokens.append(("<Symbol>", word))

    return tokens


# Example usage
if __name__ == "__main__":
    with open("input.c", "r") as f:
        code = f.read()

    tokens = lexical_analyzer(code)

    print("Tokens:\n")
    for token_type, value in tokens:
        print(f"{token_type} {value}")
