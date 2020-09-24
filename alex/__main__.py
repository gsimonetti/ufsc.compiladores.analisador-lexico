from pprint import pprint
from sys import argv, stdin

from alex import Lexer


def run():
    lexer = Lexer()

    if len(argv) < 2:
        print(f"Usage: {argv[0]} <source-file>")

    if argv[1] == '-':
        source = stdin.read()
    else:
        with open(argv[1]) as f:
            source = f.read()

    for token in lexer.tokenize(source):
        print(token)

    print("\nSymbol table:")
    pprint(lexer.symbol_table)


if __name__ == "__main__":
    run()
