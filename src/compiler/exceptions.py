"""Shared exceptions"""


class InvalidTokenError(Exception):
    """Lexical analyser fails to parse source code"""


class SyntaticError(Exception):
    """Invalid production to be applied on parsing"""
