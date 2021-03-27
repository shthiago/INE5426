from dataclasses import dataclass
from typing import List, Set, Dict


@dataclass
class Production:
    """Production of a Cfg"""
    head: str
    body: List[str]


@dataclass
class Cfg:
    """Cfg tuple"""
    start_symbol: str
    terminals: Set[str]
    non_terminals: Set[str]
    productions: List[Production]


class SyntaticAnalyserMatrix:
    """Syntatic Analyser Matrix"""

    def __init__(self, terminals: List[str], non_terminals: List[str],
                 stack_base: str = '$'):
        cols = non_terminals + [stack_base]
        rows = terminals

        self.__matrix: Dict[Dict[str, Production]] = {}

        for row in rows:
            self.__matrix[row] = {}
            for col in cols:
                self.__matrix[row][col] = None

    def set_prod(self, non_terminal: str, terminal: str, prod: Production):
        self.__matrix[non_terminal][terminal] = prod

    def get_prod(self, non_terminal: str, terminal: str) -> Production:
        return self.__matrix[non_terminal][terminal]
