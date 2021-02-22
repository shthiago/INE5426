"""Main script file"""
import argparse

from loguru import logger

from compiler.lexer.CC20202_lexer import lexer
from compiler.exceptions import InvalidTokenError
from compiler.symbol_table import generate_symbol_table


def main(filepath: str):
    """Main function"""
    with open(filepath) as f:
        source_code = f.read()

    tokens = []
    lexer.input(source_code)
    while True:
        try:
            token = lexer.token()
        except InvalidTokenError as exp:
            logger.error(exp)
            exit(1)

        if not token:
            break
        else:
            tokens.append(token)

    logger.info('Total tokens: %s' % len(tokens))
    symbols_table = generate_symbol_table(tokens)

    # Print table
    header = ['Indice',
              'Linha',
              'Column',
              'Tipo',
              'Lexema']
    row_print = "{:<15} " * len(header)
    print(row_print.format(*header))
    for row in symbols_table:
        print(row_print.format(
            row.token_position,
            row.lineno,
            row.col,
            row.type,
            row.value)
        )


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Auxiliar script to execute compiler')
    parser.add_argument('filepath',
                        help='Target source code file')

    args = parser.parse_args()
    main(args.filepath)
