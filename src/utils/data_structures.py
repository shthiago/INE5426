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

    def __eq__(self, other):
        head_eq = self.head == other.head
        body_eq = self.body == other.body
        return head_eq and body_eq


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

        self.__matrix: Dict[str, Dict[str, Optional[Production]]] = {}

        for row in rows:
            self.__matrix[row] = {}
            for col in cols:
                self.__matrix[row][col] = None

    def set_prod(self, non_terminal: str, terminal: str, prod: Production):
        curr_element = self.__matrix[non_terminal][terminal]
        if curr_element is not None \
                and curr_element != prod:
            raise ValueError('Table cell cannot be set twice!')
        self.__matrix[non_terminal][terminal] = prod

    def get_prod(self, non_terminal: str, terminal: str
                 ) -> Optional[Production]:
        return self.__matrix[non_terminal][terminal]

    def get_matrix(self) -> Dict[str, Dict[str, Optional[Production]]]:
        return self.__matrix


@dataclass
class SymbolRow:
    """Data structure for a row in symbols table

    var_name (str): Variable name
    token_index (int): Index of token at tokens list
    type (str): Variable type
    line_declared (int): token first appearance
    lines_referenced (List[int]): lines where the token is referenced
    """
    var_name: str
    token_index: int
    type: str
    line_declared: int
    lines_referenced: List[int]


SymbolTableType = Dict[str, SymbolRow]


@dataclass
class TableEntry:
    identifier_label: str
    datatype: str
    dimesions: List[int]
    line: int

    def as_json(self):
        return {
            'identifier_label': self.identifier_label,
            'datatype': self.datatype,
            'dimesions': self.dimesions,
            'line': self.line
        }


class Scope:
    def __init__(self, upper_scope=None, is_loop: bool = False):
        self.table = []

        self.upper_scope = upper_scope

        self.inner_scopes = []

        self.is_loop = is_loop

    def add_entry(self, entry: TableEntry):
        self.table.append(entry)

    def add_inner(self, scope):
        self.inner_scopes.append(scope)

    def __str__(self):
        return '\n'.join([
            str(entry)
            for entry in self.table
        ]) + '\n'

    def as_json(self) -> Dict:
        return {
            'table': [
                entry.as_json() for entry in self.table
            ],
            'inner_scopes': [scope.as_json() for scope in self.inner_scopes]
        }


class ScopeStack:
    def __init__(self):
        self.stack = []

    def pop(self):
        return self.stack.pop()

    def push(self, scope: Scope):
        self.stack.append(scope)

    def seek(self) -> Scope:
        if self.stack:
            return self.stack[-1]

        else:
            return None

    def __len__(self):
        return len(self.stack)
