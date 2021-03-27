from dataclasses import dataclass
from typing import List, Set, Dict, Optional


@dataclass
class Production:
    """Production of a Cfg"""
    head: str
    body: List[str]

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f'{self.head} -> ' + ' '.join(self.body)


@dataclass
class Cfg:
    """Cfg tuple"""
    start_symbol: str
    terminals: Set[str]
    non_terminals: Set[str]
    productions: List[Production]


class SyntaticAnalyserMatrix:
    """Syntatic Analyser Matrix"""

    def __init__(self, terminals: Set[str], non_terminals: Set[str],
                 stack_base: str = '$'):
        cols = terminals | {stack_base}
        rows = non_terminals

        self.__matrix: Dict[Dict[str, Optional[Production]]] = {}

        for row in rows:
            self.__matrix[row] = {}
            for col in cols:
                self.__matrix[row][col] = None

    def set_prod(self, non_terminal: str, terminal: str, prod: Production):
        if self.__matrix[non_terminal][terminal] is not None:
            raise ValueError('Table cell cannot be set twice!')
        self.__matrix[non_terminal][terminal] = prod

    def get_prod(self, non_terminal: str, terminal: str
                 ) -> Optional[Production]:
        return self.__matrix[non_terminal][terminal]
