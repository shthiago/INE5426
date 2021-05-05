"""Semantic analyser"""
from typing import List, Optional, Dict
from dataclasses import dataclass

from ply import yacc

from compiler.lexer.CC20202_lexer import lexer


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
    def __init__(self, entries: Optional[List[TableEntry]] = None,
                 upper_scope=None):
        if entries:
            self.entries = entries
        else:
            self.entries = []

        self.upper_scope = upper_scope

        self.inner_scopes = []

    def add_entry(self, entry: TableEntry):
        self.entries.append(entry)

    def add_inner(self, scope):
        self.inner_scopes.append(scope)

    def __str__(self):
        return '\n'.join([
            str(entry)
            for entry in self.entries
        ]) + '\n'

    def as_json(self) -> Dict:
        return {
            'table': [
                entry.as_json() for entry in self.entries
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


# Necessary for yacc instatiation
tokens = lexer.tokens

# Used for controlling scopes
scope_stack = ScopeStack()


def p_empty(p):
    """empty :"""
    pass


def p_new_scope(p):
    """new_scope :"""
    top_scope = scope_stack.seek()
    new_scope = Scope(upper_scope=top_scope)
    if top_scope:
        top_scope.add_inner(new_scope)
    scope_stack.push(new_scope)


def p_pop_scope(p):
    """pop_scope :"""
    scope_stack.pop()


def p_prog_statment(p):
    """PROGRAM : new_scope STATEMENT
               | new_scope FUNCLIST
               | empty
    """
    global_scope = scope_stack.pop()
    p[0] = global_scope.as_json()

    # Grants that all all tables where used and popper correctly
    assert len(scope_stack) == 0  # nosec


def p_funclist_funcdef(p):
    """FUNCLIST : FUNCDEF FUNCLISTAUX"""
    pass


def p_funclistaux_funclist(p):
    """FUNCLISTAUX : FUNCLIST
                   | empty
    """
    pass


def p_funcdef(p):
    """FUNCDEF : DEF IDENT new_scope LPAREN PARAMLIST RPAREN LBRACKETS STATELIST RBRACKETS"""
    # Go back to upper scope
    scope_stack.pop()

    # Add function declaration to current scope
    scope = scope_stack.seek()
    entry = TableEntry(p[2], 'function', [], p.lineno(2))
    scope.add_entry(entry)


def p_paralist_param(p):
    """PARAMLIST : DATATYPE IDENT PARAMLISTAUX
                 | empty
    """
    if len(p) > 2:
        scope = scope_stack.seek()
        entry = TableEntry(p[2], p[1], [], p.lineno(2))
        scope.add_entry(entry)


def p_paramlistaux_paramlist(p):
    """PARAMLISTAUX : COMMA PARAMLIST
                    | empty
    """
    pass


def p_datatype(p):
    """DATATYPE : INT_KEYWORD
                | FLOAT_KEYWORD
                | STRING_KEYWORD
    """
    p[0] = p[1]


def p_statement_vardecl(p):
    """STATEMENT : VARDECL SEMICOLON"""
    pass


def p_statement_atrib(p):
    """STATEMENT : ATRIBSTAT SEMICOLON"""
    pass


def p_statement_print(p):
    """STATEMENT : PRINTSTAT SEMICOLON"""
    pass


def p_statement_read(p):
    """STATEMENT : READSTAT SEMICOLON"""
    pass


def p_statement_return(p):
    """STATEMENT : RETURNSTAT SEMICOLON"""
    pass


def p_statement_if(p):
    """STATEMENT : IFSTAT"""
    pass


def p_statement_for(p):
    """STATEMENT : FORSTAT"""
    pass


def p_statement_statelist(p):
    """STATEMENT : new_scope LBRACKETS STATELIST RBRACKETS """
    # Return to previous scope
    scope_stack.pop()


def p_statement_break(p):
    """STATEMENT : BREAK SEMICOLON"""
    pass


def p_statement_end(p):
    """STATEMENT : SEMICOLON"""
    pass


def p_vardecl(p):
    """VARDECL : DATATYPE IDENT OPT_VECTOR"""
    entry = TableEntry(p[2], p[1], p[3], p.lineno(2))
    scope = scope_stack.seek()
    scope.add_entry(entry)


def p_opt_vector(p):
    """OPT_VECTOR : LSQBRACKETS INT_CONSTANT RSQBRACKETS OPT_VECTOR
                  | empty
    """
    if len(p) > 2:
        p[0] = [p[2], *p[4]]
    else:
        p[0] = []


def p_atribstat(p):
    """ATRIBSTAT : LVALUE ATTRIBUTION ATRIB_RIGHT"""
    pass


def p_atribright_func_or_exp(p):
    """ATRIB_RIGHT : FUNCCALL_OR_EXPRESSION"""
    pass


def p_atribright_alloc(p):
    """ATRIB_RIGHT : ALLOCEXPRESSION"""
    pass


def p_funccall_or_exp_plus(p):
    """FUNCCALL_OR_EXPRESSION : PLUS FACTOR REC_UNARYEXPR REC_PLUS_MINUS_TERM OPT_REL_OP_NUM_EXPR"""
    pass


def p_funccall_or_exp_minus(p):
    """FUNCCALL_OR_EXPRESSION : MINUS FACTOR REC_UNARYEXPR REC_PLUS_MINUS_TERM OPT_REL_OP_NUM_EXPR"""
    pass


def p_funccall_or_exp_int(p):
    """FUNCCALL_OR_EXPRESSION : INT_CONSTANT REC_UNARYEXPR REC_PLUS_MINUS_TERM OPT_REL_OP_NUM_EXPR"""
    pass


def p_funccall_or_exp_float(p):
    """FUNCCALL_OR_EXPRESSION : FLOAT_CONSTANT REC_UNARYEXPR REC_PLUS_MINUS_TERM OPT_REL_OP_NUM_EXPR"""
    pass


def p_funccall_or_exp_string(p):
    """FUNCCALL_OR_EXPRESSION : STRING_CONSTANT REC_UNARYEXPR REC_PLUS_MINUS_TERM OPT_REL_OP_NUM_EXPR"""
    pass


def p_funccall_or_exp_null(p):
    """FUNCCALL_OR_EXPRESSION : NULL REC_UNARYEXPR REC_PLUS_MINUS_TERM OPT_REL_OP_NUM_EXPR"""
    pass


def p_funccall_or_exp_parentesis(p):
    """FUNCCALL_OR_EXPRESSION : LPAREN NUMEXPRESSION RPAREN REC_UNARYEXPR REC_PLUS_MINUS_TERM OPT_REL_OP_NUM_EXPR"""
    pass


def p_funccall_or_exp_ident(p):
    """FUNCCALL_OR_EXPRESSION : IDENT FOLLOW_IDENT"""
    pass


def p_follow_ident_alloc(p):
    """FOLLOW_IDENT : OPT_ALLOC_NUMEXP REC_UNARYEXPR REC_PLUS_MINUS_TERM OPT_REL_OP_NUM_EXPR"""
    pass


def p_follow_ident_parentesis(p):
    """FOLLOW_IDENT : LPAREN PARAMLISTCALL RPAREN """
    pass


def p_funccall_ident(p):
    """FUNCCALL : IDENT LPAREN PARAMLISTCALL RPAREN """
    pass


def p_paramlistcall_ident(p):
    """PARAMLISTCALL : IDENT PARAMLISTCALLAUX
                     | empty
    """
    pass


def p_paramlistcallaux(p):
    """PARAMLISTCALLAUX : COMMA PARAMLISTCALL
                        | empty
    """
    pass


def p_printstat(p):
    """PRINTSTAT : PRINT EXPRESSION"""
    pass


def p_readstat(p):
    """READSTAT : READ LVALUE"""
    pass


def p_returnstat(p):
    """RETURNSTAT : RETURN"""
    pass


def p_ifstat(p):
    """IFSTAT : IF LPAREN EXPRESSION RPAREN new_scope LBRACKETS STATELIST RBRACKETS OPT_ELSE"""
    # Go back to previous scope
    scope_stack.pop()


def p_opt_else(p):
    """OPT_ELSE : ELSE new_scope LBRACKETS STATELIST RBRACKETS
                | empty
    """
    if len(p) > 2:
        # Go back to previous scope
        scope_stack.pop()


def p_forstat(p):
    """FORSTAT : FOR LPAREN ATRIBSTAT SEMICOLON EXPRESSION SEMICOLON ATRIBSTAT RPAREN STATEMENT"""
    pass


def p_statelist(p):
    """STATELIST : STATEMENT OPT_STATELIST"""
    pass


def p_opt_statelist(p):
    """OPT_STATELIST : STATELIST
                     | empty
    """
    pass


def p_allocexp(p):
    """ALLOCEXPRESSION : NEW DATATYPE LSQBRACKETS NUMEXPRESSION RSQBRACKETS OPT_ALLOC_NUMEXP"""
    pass


def p_opt_allocexp(p):
    """OPT_ALLOC_NUMEXP : LSQBRACKETS NUMEXPRESSION RSQBRACKETS OPT_ALLOC_NUMEXP
                        | empty
    """
    pass


def p_expression(p):
    """EXPRESSION : NUMEXPRESSION OPT_REL_OP_NUM_EXPR"""
    pass


def p_opt_rel_op_num_expr(p):
    """OPT_REL_OP_NUM_EXPR : REL_OP NUMEXPRESSION
                           | empty
    """
    pass


def p_relop_lt(p):
    """REL_OP : LOWER_THAN"""
    pass


def p_relop_gt(p):
    """REL_OP : GREATER_THAN"""
    pass


def p_relop_lte(p):
    """REL_OP : LOWER_OR_EQUALS_THAN"""
    pass


def p_relop_gte(p):
    """REL_OP : GREATER_OR_EQUALS_THAN"""


def p_relop_eq(p):
    """REL_OP : EQ_COMPARISON"""
    pass


def p_relop_neq(p):
    """REL_OP : NEQ_COMPARISON"""
    pass


def p_numexp(p):
    """NUMEXPRESSION : TERM REC_PLUS_MINUS_TERM"""
    pass


def p_rec_plus_minus(p):
    """REC_PLUS_MINUS_TERM : PLUS_OR_MINUS TERM REC_PLUS_MINUS_TERM
                           | empty
    """
    pass


def p_plus(p):
    """PLUS_OR_MINUS : PLUS """
    pass


def p_minus(p):
    """PLUS_OR_MINUS : MINUS """
    pass


def p_term_unary_exp(p):
    """TERM : UNARYEXPR REC_UNARYEXPR"""
    pass


def p_rec_unaryexp_op(p):
    """REC_UNARYEXPR : UNARYEXPR_OP TERM
                     | empty
    """
    pass


def p_rec_unaryexp_times(p):
    """UNARYEXPR_OP : TIMES """
    pass


def p_rec_unaryexp_duv(p):
    """UNARYEXPR_OP : DIVIDE """
    pass


def p_rec_unaryexp_mod(p):
    """UNARYEXPR_OP : MODULE """
    pass


def p_rec_unaryexp_plusminus(p):
    """UNARYEXPR : PLUS_OR_MINUS FACTOR"""
    pass


def p_rec_unaryexp_factor(p):
    """UNARYEXPR : FACTOR"""
    pass


def p_factor_int_cte(p):
    """FACTOR : INT_CONSTANT """
    pass


def p_factor_float_cte(p):
    """FACTOR : FLOAT_CONSTANT """
    pass


def p_factor_string_cte(p):
    """FACTOR : STRING_CONSTANT """
    pass


def p_factor_null(p):
    """FACTOR : NULL """
    pass


def p_factor_lvalue(p):
    """FACTOR : LVALUE"""
    pass


def p_factor_expr(p):
    """FACTOR : LPAREN NUMEXPRESSION RPAREN """
    pass


def p_lvalue_ident(p):
    """LVALUE : IDENT OPT_ALLOC_NUMEXP"""
    pass


_parser = yacc.yacc(start='PROGRAM', check_recursion=False)


def parse(text: str):
    return _parser.parse(text, lexer=lexer)
