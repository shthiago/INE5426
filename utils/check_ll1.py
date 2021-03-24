"""Check if grammar is LL(1)"""
from dataclasses import dataclass
from typing import List, Union, Set, Tuple


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


class CfgParser():
    def __init__(self):
        self.__current_symbol: Union[None, str] = None

        self.__empty = '&'

        self.__productions: List[Production] = []
        self.__start_symbol: Union[None, str] = None
        self.__non_terminals: Set[str] = set()
        self.__terminals: Set[str] = set()

    def parse(self, filepath: str) -> Cfg:
        with open(filepath) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                self.__parse_line(line)

        return Cfg(start_symbol=self.__start_symbol,
                   terminals=self.__terminals,
                   non_terminals=self.__non_terminals,
                   productions=self.__productions)

    def __parse_line(self, line: str) -> None:
        """Parse a single line"""
        if self.__is_first_production_line(line):
            head, body = self.__split_head_body(line)
            self.__current_symbol = head

            if self.__start_symbol is None:
                self.__start_symbol = head

            self.__parse_production(head, body)

        else:
            self.__parse_production(self.__current_symbol, line.split('|')[-1])

    def __split_head_body(self, prod: str) -> str:
        return prod.split(':')

    def __is_first_production_line(self, line: str) -> bool:
        return len(line.split(':')) == 2

    def __parse_production(self, head: str, str_body: str) -> None:
        body: List[str] = []
        self.__non_terminals.add(head)
        for item in str_body.split():
            if item == '':
                continue

            if item == self.__empty:
                body.append(item)

            elif (item[0] == '"' and item[-1] == '"'):
                nt_symbol = item[1:-1]
                body.append(nt_symbol)

                self.__terminals.add(nt_symbol)

            else:
                self.__non_terminals.add(item)
                body.append(item)

        self.__productions.append(Production(head, body))


def union(first: Set[str], begins: Set[str]):
    n = len(first)
    first |= begins
    return len(first) != n


class CfgProccessor:
    def __init__(self):
        self.__empty_symbol = '&'
        self.__stack_base_symbol = '$'
        self.cfg: Union[None, Cfg] = None

    def load_cfg(self, cfg: Cfg):
        self.cfg = cfg
        first = {i: set() for i in self.cfg.non_terminals}
        first.update((i, {i}) for i in self.cfg.terminals)
        first[self.__empty_symbol] = {self.__empty_symbol}

        follow = {i: set() for i in self.cfg.non_terminals}
        follow[self.__empty_symbol] = {self.__stack_base_symbol}
        follow[self.cfg.start_symbol] = {self.__stack_base_symbol}

        epsilon = set()

        while True:
            updated = False

            for prod in self.cfg.productions:
                for symbol in prod.body:
                    updated |= union(first[prod.head], first[symbol])

                    if symbol not in epsilon:
                        break

                else:
                    updated |= union(epsilon, {prod.head})

                aux = follow[prod.head]
                for symbol in reversed(prod.body):
                    if symbol in follow:
                        updated |= union(follow[symbol], aux)

                    if symbol in epsilon:
                        aux = aux.union(first[symbol])
                    else:
                        aux = first[symbol]

            if not updated:
                break

        self.__first = first
        self.__follow = follow
        self.__epsilon = epsilon

    def read(self, filepath: str):
        """Parse Cfg from a file

        Args:
            filepath (str)
        """
        parser = CfgParser()
        self.load_cfg(parser.parse(filepath))

    def get_productions_of(self, head: str) -> List[Production]:
        return list(filter(lambda k: k.head == head, self.cfg.productions))

    def get_productions_with(self, symbol) -> List[Production]:
        return list(filter(lambda k: symbol in k.body, self.cfg.productions))

    def is_terminal(self, symbol: str) -> bool:
        return symbol in self.cfg.terminals

    def is_empty(self, symbol) -> bool:
        return symbol == self.__empty_symbol

    def is_non_terminal(self, symbol: str) -> bool:
        return not self.is_terminal(symbol) and not self.is_empty(symbol)

    def first(self, symbol: str) -> Set[str]:
        return self.__first[symbol]

    def follow(self, symbol: str) -> Set[str]:
        return self.__follow[symbol]


if __name__ == '__main__':
    # test pseudo-suite
    filepath = 'ConvCC-2020-1.csf'

    cfg_proc = CfgProccessor()
    cfg_proc.read(filepath)

    cfg_proc.follow('FORSTAT')

    for symbol in cfg_proc.cfg.terminals.union(cfg_proc.cfg.non_terminals):
        print(f'FIRST({symbol})= {cfg_proc.first(symbol)}')

    for symbol in cfg_proc.cfg.non_terminals:
        print(f'FOLLOW({symbol})= {cfg_proc.follow(symbol)}')
