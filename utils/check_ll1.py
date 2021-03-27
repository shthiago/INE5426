"""Check if grammar is LL(1)"""
from itertools import combinations
from dataclasses import dataclass
from typing import List, Union, Set, Tuple

from loguru import logger


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
    first |= begins - {'&'}
    return len(first) != n


class CfgProcessor:
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

        epsilon = {self.__empty_symbol}

        while True:
            updated = False

            for prod in self.cfg.productions:
                # Calculate FIRST
                for symbol in prod.body:
                    updated |= union(first[prod.head], first[symbol])

                    if symbol not in epsilon:
                        break

                else:
                    first[prod.head] |= {self.__empty_symbol}
                    updated |= union(epsilon, {prod.head})

                # Calcualte FOLLOW
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

    def first_of_prod_body(self, body: List[str]) -> Set[str]:
        first = set()
        for symbol in body:
            symbol_first = self.first(symbol)

            first |= self.first(symbol) - {self.__empty_symbol}

            if self.__empty_symbol not in symbol_first:
                break

        else:
            first |= {self.__empty_symbol}

        return first

    def __theorem_first_clause(self, prod1: Production,
                               prod2: Production) -> bool:
        """First(alpha) intersect First(beta) = {}"""
        prod1_first = self.first_of_prod_body(prod1.body)
        prod2_first = self.first_of_prod_body(prod2.body)

        valid = prod1_first.intersection(prod2_first) == set()

        if not valid:
            logger.info('Prod1 first:: %s ' % prod1_first)
            logger.info('Prod2 first:: %s ' % prod2_first)
            logger.info('First theorem failed')

        return valid

    def __theorem_second_clause(self, prod1: Production,
                                prod2: Production) -> bool:
        """
            If beta ->* &, First(alpha) intersect Follow(A) = {}
            If alpha ->* &, First(beta) intersect Follow(A) = {}

            prod.body ->* & == First(prod.body) contains empty_symbol
        """
        if prod1.head != prod2.head:
            logger.error('Theorem do not apply to different heads: %s, %s' %
                         (prod1, prod2))
            raise ValueError

        valid = True
        head_follow = self.follow(prod1.head)
        prod1_body_first = self.first_of_prod_body(prod1.body)
        prod2_body_first = self.first_of_prod_body(prod2.body)

        if self.__empty_symbol in prod2_body_first:
            valid &= prod1_body_first.intersection(head_follow) == set()

        if self.__empty_symbol in prod1_body_first:
            valid &= prod2_body_first.intersection(head_follow) == set()

        if not valid:
            logger.info('Second theorem failed')
            logger.info('Prod1 first: %s' % prod1_body_first)
            logger.info('Prod2 first: %s' % prod2_body_first)
            logger.info('Head follow: %s' % head_follow)

        return valid

    def __apply_theorem_all_prods_of(self, nt: str) -> bool:
        """Apply theorem for all prods of a non terminal"""
        prods = self.get_productions_of(nt)
        for p1, p2 in combinations(prods, 2):
            first_clause = self.__theorem_first_clause(p1, p2)
            second_clause = self.__theorem_second_clause(p1, p2)
            if not (first_clause and second_clause):
                logger.error('Grammar is not LL(1) due to: %s, %s' %
                             (p1, p2))
                return False

        return True

    def is_ll1(self) -> bool:
        """Check if cfg is LL(1) apply the theorem

            for A -> "alpha" | "beta",

            1 - First(alpha) intersect First(beta) = {}
            2 - If beta ->* &, First(alpha) intersect Follow(A) = {}
                If alpha ->* &, First(beta) intersect Follow(A) = {}
        """
        for nt in self.cfg.non_terminals:
            if not self.__apply_theorem_all_prods_of(nt):
                return False

        return True


if __name__ == '__main__':
    cfg_proc = CfgProcessor()
    cfg_proc.read('ConvCC-2020-1.csf')
    cfg_proc.is_ll1()
