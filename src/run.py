"""Main script file"""
import argparse
import linecache
from dataclasses import asdict

from loguru import logger

from compiler.lexer.CC20202_lexer import lexer
from compiler.exceptions import InvalidTokenError, SyntaticError
from compiler.symbol_table import generate_symbol_table
from compiler.parser.CC20202_parser import parser


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
    # logger.info('Lista de tokens:')
    # for token in tokens:
    #     print('<%s, %s>' % (token.type, token.value))

    symbols_table = generate_symbol_table(tokens)
    logger.info('Imprimindo tabela de símbolos...')

    # Print table
    header = [
        'var_name',
        'token_index',
        'type',
        'line_declared',
        'lines_referenced']

    row_print = "{:<15} " * len(header)
    print(row_print.format(*header))
    for _, symbol_row in symbols_table.items():
        print(row_print.format(
            str(symbol_row.var_name),
            str(symbol_row.token_index),
            str(symbol_row.type),
            str(symbol_row.line_declared),
            str(symbol_row.lines_referenced)))

    logger.info('Running parser for list of tokens...')
    success, fail_token = parser.parse(symbols_table=symbols_table,
                                       tokens=tokens)

    if not success:
        line = linecache.getline(filepath, fail_token.lineno)
        logger.info('Invalid sintax at line %s:\n\t%s' %
                    (fail_token.lineno, line.strip()))
        logger.info('Token: %s' % fail_token)
        logger.error('Syntatic error detected!')


if __name__ == '__main__':
    # arg_parser = argparse.ArgumentParser(
    #     description='Auxiliar script to execute compiler')
    # arg_parser.add_argument('filepath',
    #                         help='Target source code file')

    # args = arg_parser.parse_args()
    # main(args.filepath)
    main('examples/exemplo2.ccc')
