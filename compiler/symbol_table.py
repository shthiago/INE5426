"""Definition of the symbol table"""
from typing import List, Union
from dataclasses import dataclass

from ply.lex import LexToken


SYMBOLS_TO_TABLE = ['IDENT', 'FLOAT_CONSTANT',
                    'INT_CONSTANT', 'STRING_CONSTANT']


@dataclass
class SymbolRow:
    """Data structure for a row in symbols table

    token_position (int): Position of the token into all tokens list
    lineno (int): Line of the token into source code
    col (int): Column of the token into source code
    type (str): Type of the token, from the final symbols of the gramatic
    """
    token_position: int
    lineno: int
    type: str
    value: Union[int, float, str]


def generate_symbol_table(tokens: List[LexToken]) -> List[SymbolRow]:
    """Gerante symbol table using SYMBOLS_TO_TABLE as orientation"""
    symbols_table: List[SymbolRow] = []
    for i, token in enumerate(tokens, 1):
        if token.type in SYMBOLS_TO_TABLE:
            symbols_table.append(SymbolRow(
                token_position=i,
                lineno=token.lineno,
                type=token.type,
                value=token.value
            ))

    return symbols_table
