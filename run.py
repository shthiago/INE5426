"""Main script file"""
import argparse

from loguru import logger

from compiler.lexer.CC20202_lexer import lexer
from compiler.exceptions import InvalidTokenError


def main(filepath: str):
    """Main function"""
    with open(filepath) as f:
        source_code = f.read()

    token_count = 0
    symbol_table = []
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
            symbol_table.append(token)
            token_count += 1

    logger.info('Total tokens: %s' % token_count)
    print("{:<25} {:<5} {}".format('Token', 'Line', 'Value'))
    for token in symbol_table:
        print("{:<25} {:<5} {}".format(token.type, token.lineno, token.value))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Auxiliar script to execute compiler')
    parser.add_argument('filepath',
                        help='Target source code file')

    args = parser.parse_args()
    main(args.filepath)
