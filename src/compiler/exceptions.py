"""Shared exceptions"""


class InvalidTokenError(Exception):
    """Lexical analyser fails to parse source code"""


class SyntaticError(Exception):
    """Invalid production to be applied on parsing"""


class BreakWithoutLoopError(Exception):
    """Semantic error when a break is written without a loop scope"""


class InvalidTypeOperationError(Exception):
    """Semantic error when two variables are invalid operated"""
