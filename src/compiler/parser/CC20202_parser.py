"""Parser for CC-2020-2 language"""
import os
from typing import List
from collections import deque

from ply.lex import LexToken

from utils.cfg_processor import CfgProcessor
from utils.data_structures import SyntaticAnalyserMatrix, SymbolTableType
from compiler.exceptions import SyntaticError


class CC20202Parser:
    def __init__(self):
        curr_file_folder = os.path.dirname(__file__)
        grammar_path = os.path.join(curr_file_folder,
                                    '..', '..',
                                    'grammar',
                                    'ConvCC-2020-2.csf')

        cfg_proc = CfgProcessor()
        cfg_proc.read(grammar_path)

        self.cfg = cfg_proc.cfg
        self.start_symbol = cfg_proc.cfg.start_symbol
        self.mat = cfg_proc.generate_matrix()

    def parse(self, symbols_table: SymbolTableType,
              tokens: List[LexToken]):
        """Validate symbols and update symbols_table"""
        stack = deque()

        stack.append('$')
        stack.append(self.start_symbol)

        for token in tokens:
            while True:
                # Terminal on top of stack and on code pointer
                # are equals, pop the stack and move the pointer
                if token == stack[-1]:
                    stack.pop()
                    break

                # Get production to be applied
                prod = self.mat.get_prod(stack[-1], token.value)

                # Reconize syntatic error
                if prod is None:
                    raise SyntaticError(
                        f'Invalid combination: {stack[-1]}, {token}')

                # Remove the top of the stack
                stack.pop()

                # Stack the symbols from corresponding production
                for symbol in prod.body:
                    stack.append(symbol)

        if len(stack) > 0:
            raise SyntaticError(f'{stack}')


parser = CC20202Parser()
