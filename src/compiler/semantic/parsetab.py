
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'PROGRAMATTRIBUTION BREAK COMMA DEF DIVIDE ELSE EQ_COMPARISON FLOAT_CONSTANT FLOAT_KEYWORD FOR GREATER_OR_EQUALS_THAN GREATER_THAN IDENT IF INT_CONSTANT INT_KEYWORD LBRACKETS LOWER_OR_EQUALS_THAN LOWER_THAN LPAREN LSQBRACKETS MINUS MODULE NEQ_COMPARISON NEW NULL PLUS PRINT RBRACKETS READ RETURN RPAREN RSQBRACKETS SEMICOLON STRING_CONSTANT STRING_KEYWORD TIMESempty :new_scope :new_loop_scope :PROGRAM : new_scope STATEMENT\n               | new_scope FUNCLIST\n               | empty\n    FUNCLIST : FUNCDEF FUNCLISTAUXFUNCLISTAUX : FUNCLIST\n                   | empty\n    FUNCDEF : DEF IDENT new_scope LPAREN PARAMLIST RPAREN LBRACKETS STATELIST RBRACKETSPARAMLIST : DATATYPE IDENT PARAMLISTAUX\n                 | empty\n    PARAMLISTAUX : COMMA PARAMLIST\n                    | empty\n    DATATYPE : INT_KEYWORD\n                | FLOAT_KEYWORD\n                | STRING_KEYWORD\n    STATEMENT : VARDECL SEMICOLONSTATEMENT : ATRIBSTAT SEMICOLONSTATEMENT : PRINTSTAT SEMICOLONSTATEMENT : READSTAT SEMICOLONSTATEMENT : RETURNSTAT SEMICOLONSTATEMENT : IFSTATSTATEMENT : FORSTATSTATEMENT : new_scope LBRACKETS STATELIST RBRACKETS STATEMENT : BREAK SEMICOLONSTATEMENT : SEMICOLONVARDECL : DATATYPE IDENT OPT_VECTOROPT_VECTOR : LSQBRACKETS INT_CONSTANT RSQBRACKETS OPT_VECTOR\n                  | empty\n    ATRIBSTAT : LVALUE ATTRIBUTION ATRIB_RIGHTATRIB_RIGHT : FUNCCALL_OR_EXPRESSIONATRIB_RIGHT : ALLOCEXPRESSIONFUNCCALL_OR_EXPRESSION : PLUS FACTOR REC_UNARYEXPR REC_PLUS_MINUS_TERM OPT_REL_OP_NUM_EXPRFUNCCALL_OR_EXPRESSION : MINUS FACTOR REC_UNARYEXPR REC_PLUS_MINUS_TERM OPT_REL_OP_NUM_EXPRFUNCCALL_OR_EXPRESSION : INT_CONSTANT REC_UNARYEXPR REC_PLUS_MINUS_TERM OPT_REL_OP_NUM_EXPRFUNCCALL_OR_EXPRESSION : FLOAT_CONSTANT REC_UNARYEXPR REC_PLUS_MINUS_TERM OPT_REL_OP_NUM_EXPRFUNCCALL_OR_EXPRESSION : STRING_CONSTANT REC_UNARYEXPR REC_PLUS_MINUS_TERM OPT_REL_OP_NUM_EXPRFUNCCALL_OR_EXPRESSION : NULL REC_UNARYEXPR REC_PLUS_MINUS_TERM OPT_REL_OP_NUM_EXPRFUNCCALL_OR_EXPRESSION : LPAREN NUMEXPRESSION RPAREN REC_UNARYEXPR REC_PLUS_MINUS_TERM OPT_REL_OP_NUM_EXPRFUNCCALL_OR_EXPRESSION : IDENT FOLLOW_IDENTFOLLOW_IDENT : OPT_ALLOC_NUMEXP REC_UNARYEXPR REC_PLUS_MINUS_TERM OPT_REL_OP_NUM_EXPRFOLLOW_IDENT : LPAREN PARAMLISTCALL RPAREN PARAMLISTCALL : IDENT PARAMLISTCALLAUX\n                     | empty\n    PARAMLISTCALLAUX : COMMA PARAMLISTCALL\n                        | empty\n    PRINTSTAT : PRINT EXPRESSIONREADSTAT : READ LVALUERETURNSTAT : RETURNIFSTAT : IF LPAREN EXPRESSION RPAREN new_scope LBRACKETS STATELIST RBRACKETS OPT_ELSEOPT_ELSE : ELSE new_scope LBRACKETS STATELIST RBRACKETS\n                | empty\n    FORSTAT : FOR LPAREN ATRIBSTAT SEMICOLON EXPRESSION SEMICOLON ATRIBSTAT RPAREN new_loop_scope LBRACKETS STATELIST RBRACKETSSTATELIST : STATEMENT OPT_STATELISTOPT_STATELIST : STATELIST\n                     | empty\n    ALLOCEXPRESSION : NEW DATATYPE LSQBRACKETS NUMEXPRESSION RSQBRACKETS OPT_ALLOC_NUMEXPOPT_ALLOC_NUMEXP : LSQBRACKETS NUMEXPRESSION RSQBRACKETS OPT_ALLOC_NUMEXP\n                        | empty\n    EXPRESSION : NUMEXPRESSION OPT_REL_OP_NUM_EXPROPT_REL_OP_NUM_EXPR : REL_OP NUMEXPRESSION\n                           | empty\n    REL_OP : LOWER_THANREL_OP : GREATER_THANREL_OP : LOWER_OR_EQUALS_THANREL_OP : GREATER_OR_EQUALS_THANREL_OP : EQ_COMPARISONREL_OP : NEQ_COMPARISONNUMEXPRESSION : TERM REC_PLUS_MINUS_TERMREC_PLUS_MINUS_TERM : PLUS_OR_MINUS TERM REC_PLUS_MINUS_TERM\n                           | empty\n    PLUS_OR_MINUS : PLUS PLUS_OR_MINUS : MINUS TERM : UNARYEXPR REC_UNARYEXPRREC_UNARYEXPR : UNARYEXPR_OP TERM\n                     | empty\n    UNARYEXPR_OP : TIMES\n                    | MODULE\n                    | DIVIDE UNARYEXPR : PLUS_OR_MINUS FACTORUNARYEXPR : FACTORFACTOR : INT_CONSTANT FACTOR : FLOAT_CONSTANT FACTOR : STRING_CONSTANT FACTOR : NULL FACTOR : LVALUEFACTOR : LPAREN NUMEXPRESSION RPARENLVALUE : IDENT OPT_ALLOC_NUMEXP'
    
_lr_action_items = {'BREAK':([0,2,8,13,14,29,30,31,32,33,34,35,63,103,161,173,179,183,185,189,190,193,194,],[-2,15,-27,-23,-24,15,-18,-19,-20,-21,-22,-26,15,-25,15,15,-1,-51,-53,15,15,-54,-52,]),'SEMICOLON':([0,2,7,8,9,10,11,12,13,14,15,18,22,29,30,31,32,33,34,35,39,40,42,44,45,46,47,49,52,53,54,55,56,58,63,64,66,68,69,70,73,74,75,76,78,80,82,89,91,92,94,98,101,103,108,109,110,111,112,113,114,116,117,120,121,122,123,127,128,129,130,131,132,133,134,135,136,141,143,147,148,149,150,151,152,153,154,155,156,161,165,166,167,168,170,173,177,178,179,183,185,189,190,193,194,],[-2,8,30,-27,31,32,33,34,-23,-24,35,-1,-50,8,-18,-19,-20,-21,-22,-26,-1,-89,-60,-48,-1,-1,-1,-82,-83,-84,-85,-86,-87,-49,8,-28,-30,-31,-32,-33,-1,-1,-1,-1,-1,-61,-63,-70,-72,-75,-77,-81,125,-25,-1,-1,-1,-1,-1,-1,-1,-41,-1,-62,-1,-76,-88,-1,-59,-1,-1,-1,-1,-1,-1,-1,-1,-71,162,-29,-1,-1,-36,-37,-38,-39,-1,-1,-43,8,-34,-35,-1,-42,-1,8,-40,-58,-1,-51,-53,8,8,-54,-52,]),'PRINT':([0,2,8,13,14,29,30,31,32,33,34,35,63,103,161,173,179,183,185,189,190,193,194,],[-2,20,-27,-23,-24,20,-18,-19,-20,-21,-22,-26,20,-25,20,20,-1,-51,-53,20,20,-54,-52,]),'READ':([0,2,8,13,14,29,30,31,32,33,34,35,63,103,161,173,179,183,185,189,190,193,194,],[-2,21,-27,-23,-24,21,-18,-19,-20,-21,-22,-26,21,-25,21,21,-1,-51,-53,21,21,-54,-52,]),'RETURN':([0,2,8,13,14,29,30,31,32,33,34,35,63,103,161,173,179,183,185,189,190,193,194,],[-2,22,-27,-23,-24,22,-18,-19,-20,-21,-22,-26,22,-25,22,22,-1,-51,-53,22,22,-54,-52,]),'IF':([0,2,8,13,14,29,30,31,32,33,34,35,63,103,161,173,179,183,185,189,190,193,194,],[-2,23,-27,-23,-24,23,-18,-19,-20,-21,-22,-26,23,-25,23,23,-1,-51,-53,23,23,-54,-52,]),'FOR':([0,2,8,13,14,29,30,31,32,33,34,35,63,103,161,173,179,183,185,189,190,193,194,],[-2,24,-27,-23,-24,24,-18,-19,-20,-21,-22,-26,24,-25,24,24,-1,-51,-53,24,24,-54,-52,]),'DEF':([0,2,16,187,],[-2,25,25,-10,]),'INT_KEYWORD':([0,2,8,13,14,29,30,31,32,33,34,35,63,79,103,126,161,173,175,179,183,185,189,190,193,194,],[-2,26,-27,-23,-24,26,-18,-19,-20,-21,-22,-26,26,26,-25,26,26,26,26,-1,-51,-53,26,26,-54,-52,]),'FLOAT_KEYWORD':([0,2,8,13,14,29,30,31,32,33,34,35,63,79,103,126,161,173,175,179,183,185,189,190,193,194,],[-2,27,-27,-23,-24,27,-18,-19,-20,-21,-22,-26,27,27,-25,27,27,27,27,-1,-51,-53,27,27,-54,-52,]),'STRING_KEYWORD':([0,2,8,13,14,29,30,31,32,33,34,35,63,79,103,126,161,173,175,179,183,185,189,190,193,194,],[-2,28,-27,-23,-24,28,-18,-19,-20,-21,-22,-26,28,28,-25,28,28,28,28,-1,-51,-53,28,28,-54,-52,]),'IDENT':([0,2,8,13,14,17,20,21,25,26,27,28,29,30,31,32,33,34,35,41,43,48,50,51,57,59,60,63,71,72,77,81,83,84,85,86,87,88,90,93,95,96,97,103,118,125,140,145,158,161,162,173,179,183,185,189,190,193,194,],[-2,18,-27,-23,-24,39,18,18,61,-15,-16,-17,18,-18,-19,-20,-21,-22,-26,18,78,18,-73,-74,18,18,18,18,18,18,18,18,-64,-65,-66,-67,-68,-69,18,18,-78,-79,-80,-25,138,18,18,164,138,18,18,18,-1,-51,-53,18,18,-54,-52,]),'LBRACKETS':([0,2,4,8,13,14,29,30,31,32,33,34,35,63,103,124,142,161,163,173,179,180,183,184,185,186,188,189,190,193,194,],[-2,-2,29,-27,-23,-24,-2,-18,-19,-20,-21,-22,-26,-2,-25,-2,161,-2,173,-2,-1,-3,-51,-2,-53,189,190,-2,-2,-54,-52,]),'$end':([0,1,3,5,6,8,13,14,16,30,31,32,33,34,35,36,37,38,103,179,183,185,187,193,194,],[-1,0,-6,-4,-5,-27,-23,-24,-1,-18,-19,-20,-21,-22,-26,-7,-8,-9,-25,-1,-51,-53,-10,-54,-52,]),'RBRACKETS':([8,13,14,30,31,32,33,34,35,62,63,103,104,105,106,171,179,181,183,185,191,192,193,194,],[-27,-23,-24,-18,-19,-20,-21,-22,-26,103,-1,-25,-55,-56,-57,179,-1,187,-51,-53,193,194,-54,-52,]),'LSQBRACKETS':([18,26,27,28,39,78,108,119,127,170,],[41,-15,-16,-17,65,41,41,140,65,41,]),'ATTRIBUTION':([18,19,40,42,108,128,],[-1,43,-89,-60,-1,-59,]),'TIMES':([18,40,42,47,49,52,53,54,55,56,73,74,75,76,78,98,108,109,110,117,123,128,135,],[-1,-89,-60,95,-82,-83,-84,-85,-86,-87,95,95,95,95,-1,-81,-1,95,95,95,-88,-59,95,]),'MODULE':([18,40,42,47,49,52,53,54,55,56,73,74,75,76,78,98,108,109,110,117,123,128,135,],[-1,-89,-60,96,-82,-83,-84,-85,-86,-87,96,96,96,96,-1,-81,-1,96,96,96,-88,-59,96,]),'DIVIDE':([18,40,42,47,49,52,53,54,55,56,73,74,75,76,78,98,108,109,110,117,123,128,135,],[-1,-89,-60,97,-82,-83,-84,-85,-86,-87,97,97,97,97,-1,-81,-1,97,97,97,-88,-59,97,]),'PLUS':([18,20,40,41,42,43,46,47,49,50,51,52,53,54,55,56,57,59,73,74,75,76,77,78,81,83,84,85,86,87,88,90,92,93,94,95,96,97,98,108,109,110,111,112,113,114,117,121,122,123,125,128,129,130,135,136,140,154,],[-1,50,-89,50,-60,71,50,-1,-82,-73,-74,-83,-84,-85,-86,-87,50,50,-1,-1,-1,-1,50,-1,50,-64,-65,-66,-67,-68,-69,50,-75,50,-77,-78,-79,-80,-81,-1,-1,-1,50,50,50,50,-1,50,-76,-88,50,-59,50,50,-1,50,50,50,]),'MINUS':([18,20,40,41,42,43,46,47,49,50,51,52,53,54,55,56,57,59,73,74,75,76,77,78,81,83,84,85,86,87,88,90,92,93,94,95,96,97,98,108,109,110,111,112,113,114,117,121,122,123,125,128,129,130,135,136,140,154,],[-1,51,-89,51,-60,72,51,-1,-82,-73,-74,-83,-84,-85,-86,-87,51,51,-1,-1,-1,-1,51,-1,51,-64,-65,-66,-67,-68,-69,51,-75,51,-77,-78,-79,-80,-81,-1,-1,-1,51,51,51,51,-1,51,-76,-88,51,-59,51,51,-1,51,51,51,]),'LOWER_THAN':([18,40,42,45,46,47,49,52,53,54,55,56,73,74,75,76,78,89,91,92,94,98,108,109,110,111,112,113,114,117,121,122,123,128,129,130,131,132,133,134,135,136,141,148,149,154,155,167,],[-1,-89,-60,83,-1,-1,-82,-83,-84,-85,-86,-87,-1,-1,-1,-1,-1,-70,-72,-75,-77,-81,-1,-1,-1,-1,-1,-1,-1,-1,-1,-76,-88,-59,-1,-1,83,83,83,83,-1,-1,-71,83,83,-1,83,83,]),'GREATER_THAN':([18,40,42,45,46,47,49,52,53,54,55,56,73,74,75,76,78,89,91,92,94,98,108,109,110,111,112,113,114,117,121,122,123,128,129,130,131,132,133,134,135,136,141,148,149,154,155,167,],[-1,-89,-60,84,-1,-1,-82,-83,-84,-85,-86,-87,-1,-1,-1,-1,-1,-70,-72,-75,-77,-81,-1,-1,-1,-1,-1,-1,-1,-1,-1,-76,-88,-59,-1,-1,84,84,84,84,-1,-1,-71,84,84,-1,84,84,]),'LOWER_OR_EQUALS_THAN':([18,40,42,45,46,47,49,52,53,54,55,56,73,74,75,76,78,89,91,92,94,98,108,109,110,111,112,113,114,117,121,122,123,128,129,130,131,132,133,134,135,136,141,148,149,154,155,167,],[-1,-89,-60,85,-1,-1,-82,-83,-84,-85,-86,-87,-1,-1,-1,-1,-1,-70,-72,-75,-77,-81,-1,-1,-1,-1,-1,-1,-1,-1,-1,-76,-88,-59,-1,-1,85,85,85,85,-1,-1,-71,85,85,-1,85,85,]),'GREATER_OR_EQUALS_THAN':([18,40,42,45,46,47,49,52,53,54,55,56,73,74,75,76,78,89,91,92,94,98,108,109,110,111,112,113,114,117,121,122,123,128,129,130,131,132,133,134,135,136,141,148,149,154,155,167,],[-1,-89,-60,86,-1,-1,-82,-83,-84,-85,-86,-87,-1,-1,-1,-1,-1,-70,-72,-75,-77,-81,-1,-1,-1,-1,-1,-1,-1,-1,-1,-76,-88,-59,-1,-1,86,86,86,86,-1,-1,-71,86,86,-1,86,86,]),'EQ_COMPARISON':([18,40,42,45,46,47,49,52,53,54,55,56,73,74,75,76,78,89,91,92,94,98,108,109,110,111,112,113,114,117,121,122,123,128,129,130,131,132,133,134,135,136,141,148,149,154,155,167,],[-1,-89,-60,87,-1,-1,-82,-83,-84,-85,-86,-87,-1,-1,-1,-1,-1,-70,-72,-75,-77,-81,-1,-1,-1,-1,-1,-1,-1,-1,-1,-76,-88,-59,-1,-1,87,87,87,87,-1,-1,-71,87,87,-1,87,87,]),'NEQ_COMPARISON':([18,40,42,45,46,47,49,52,53,54,55,56,73,74,75,76,78,89,91,92,94,98,108,109,110,111,112,113,114,117,121,122,123,128,129,130,131,132,133,134,135,136,141,148,149,154,155,167,],[-1,-89,-60,88,-1,-1,-82,-83,-84,-85,-86,-87,-1,-1,-1,-1,-1,-70,-72,-75,-77,-81,-1,-1,-1,-1,-1,-1,-1,-1,-1,-76,-88,-59,-1,-1,88,88,88,88,-1,-1,-71,88,88,-1,88,88,]),'RSQBRACKETS':([18,40,42,46,47,49,52,53,54,55,56,67,89,91,92,94,98,107,108,121,122,123,128,141,160,],[-1,-89,-60,-1,-1,-82,-83,-84,-85,-86,-87,108,-70,-72,-75,-77,-81,127,-1,-1,-76,-88,-59,-71,170,]),'RPAREN':([18,40,42,45,46,47,49,52,53,54,55,56,68,69,70,73,74,75,76,78,80,82,89,91,92,94,98,99,100,108,109,110,111,112,113,114,115,116,117,118,120,121,122,123,126,128,129,130,131,132,133,134,135,136,137,138,139,141,144,146,148,149,150,151,152,153,154,155,156,157,158,159,164,165,166,167,168,169,170,172,174,175,176,177,178,182,],[-1,-89,-60,-1,-1,-1,-82,-83,-84,-85,-86,-87,-31,-32,-33,-1,-1,-1,-1,-1,-61,-63,-70,-72,-75,-77,-81,123,124,-1,-1,-1,-1,-1,-1,-1,135,-41,-1,-1,-62,-1,-76,-88,-1,-59,-1,-1,-1,-1,-1,-1,-1,-1,156,-1,-45,-71,163,-12,-1,-1,-36,-37,-38,-39,-1,-1,-43,-44,-1,-47,-1,-34,-35,-1,-42,-46,-1,180,-11,-1,-14,-40,-58,-13,]),'INT_CONSTANT':([20,41,43,48,50,51,57,59,65,71,72,77,81,83,84,85,86,87,88,90,93,95,96,97,125,140,],[52,52,73,52,-73,-74,52,52,107,52,52,52,52,-64,-65,-66,-67,-68,-69,52,52,-78,-79,-80,52,52,]),'FLOAT_CONSTANT':([20,41,43,48,50,51,57,59,71,72,77,81,83,84,85,86,87,88,90,93,95,96,97,125,140,],[53,53,74,53,-73,-74,53,53,53,53,53,53,-64,-65,-66,-67,-68,-69,53,53,-78,-79,-80,53,53,]),'STRING_CONSTANT':([20,41,43,48,50,51,57,59,71,72,77,81,83,84,85,86,87,88,90,93,95,96,97,125,140,],[54,54,75,54,-73,-74,54,54,54,54,54,54,-64,-65,-66,-67,-68,-69,54,54,-78,-79,-80,54,54,]),'NULL':([20,41,43,48,50,51,57,59,71,72,77,81,83,84,85,86,87,88,90,93,95,96,97,125,140,],[55,55,76,55,-73,-74,55,55,55,55,55,55,-64,-65,-66,-67,-68,-69,55,55,-78,-79,-80,55,55,]),'LPAREN':([20,23,24,41,43,48,50,51,57,59,61,71,72,77,78,81,83,84,85,86,87,88,90,93,95,96,97,102,125,140,],[57,59,60,57,77,57,-73,-74,57,57,-2,57,57,57,118,57,-64,-65,-66,-67,-68,-69,57,57,-78,-79,-80,126,57,57,]),'NEW':([43,],[79,]),'COMMA':([138,164,],[158,175,]),'ELSE':([179,],[184,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'PROGRAM':([0,],[1,]),'new_scope':([0,2,29,61,63,124,161,173,184,189,190,],[2,4,4,102,4,142,4,4,188,4,4,]),'empty':([0,16,18,39,45,46,47,63,73,74,75,76,78,108,109,110,111,112,113,114,117,118,121,126,127,129,130,131,132,133,134,135,136,138,148,149,154,155,158,164,167,170,175,179,],[3,38,42,66,82,91,94,106,94,94,94,94,42,42,94,94,91,91,91,91,94,139,91,146,66,91,91,82,82,82,82,94,91,159,82,82,91,82,139,176,82,42,146,185,]),'STATEMENT':([2,29,63,161,173,189,190,],[5,63,63,63,63,63,63,]),'FUNCLIST':([2,16,],[6,37,]),'VARDECL':([2,29,63,161,173,189,190,],[7,7,7,7,7,7,7,]),'ATRIBSTAT':([2,29,60,63,161,162,173,189,190,],[9,9,101,9,9,172,9,9,9,]),'PRINTSTAT':([2,29,63,161,173,189,190,],[10,10,10,10,10,10,10,]),'READSTAT':([2,29,63,161,173,189,190,],[11,11,11,11,11,11,11,]),'RETURNSTAT':([2,29,63,161,173,189,190,],[12,12,12,12,12,12,12,]),'IFSTAT':([2,29,63,161,173,189,190,],[13,13,13,13,13,13,13,]),'FORSTAT':([2,29,63,161,173,189,190,],[14,14,14,14,14,14,14,]),'FUNCDEF':([2,16,],[16,16,]),'DATATYPE':([2,29,63,79,126,161,173,175,189,190,],[17,17,17,119,145,17,17,145,17,17,]),'LVALUE':([2,20,21,29,41,48,57,59,60,63,71,72,77,81,90,93,125,140,161,162,173,189,190,],[19,56,58,19,56,56,56,56,19,19,56,56,56,56,56,56,56,56,19,19,19,19,19,]),'FUNCLISTAUX':([16,],[36,]),'OPT_ALLOC_NUMEXP':([18,78,108,170,],[40,117,128,178,]),'EXPRESSION':([20,59,125,],[44,100,143,]),'NUMEXPRESSION':([20,41,57,59,77,81,125,140,],[45,67,99,45,115,120,45,160,]),'TERM':([20,41,57,59,77,81,90,93,125,140,],[46,46,46,46,46,46,121,122,46,46,]),'UNARYEXPR':([20,41,57,59,77,81,90,93,125,140,],[47,47,47,47,47,47,47,47,47,47,]),'PLUS_OR_MINUS':([20,41,46,57,59,77,81,90,93,111,112,113,114,121,125,129,130,136,140,154,],[48,48,90,48,48,48,48,48,48,90,90,90,90,90,48,90,90,90,48,90,]),'FACTOR':([20,41,48,57,59,71,72,77,81,90,93,125,140,],[49,49,98,49,49,109,110,49,49,49,49,49,49,]),'STATELIST':([29,63,161,173,189,190,],[62,105,171,181,191,192,]),'OPT_VECTOR':([39,127,],[64,147,]),'ATRIB_RIGHT':([43,],[68,]),'FUNCCALL_OR_EXPRESSION':([43,],[69,]),'ALLOCEXPRESSION':([43,],[70,]),'OPT_REL_OP_NUM_EXPR':([45,131,132,133,134,148,149,155,167,],[80,150,151,152,153,165,166,168,177,]),'REL_OP':([45,131,132,133,134,148,149,155,167,],[81,81,81,81,81,81,81,81,81,]),'REC_PLUS_MINUS_TERM':([46,111,112,113,114,121,129,130,136,154,],[89,131,132,133,134,141,148,149,155,167,]),'REC_UNARYEXPR':([47,73,74,75,76,109,110,117,135,],[92,111,112,113,114,129,130,136,154,]),'UNARYEXPR_OP':([47,73,74,75,76,109,110,117,135,],[93,93,93,93,93,93,93,93,93,]),'OPT_STATELIST':([63,],[104,]),'FOLLOW_IDENT':([78,],[116,]),'PARAMLISTCALL':([118,158,],[137,169,]),'PARAMLIST':([126,175,],[144,182,]),'PARAMLISTCALLAUX':([138,],[157,]),'PARAMLISTAUX':([164,],[174,]),'OPT_ELSE':([179,],[183,]),'new_loop_scope':([180,],[186,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAM","S'",1,None,None,None),
  ('empty -> <empty>','empty',0,'p_empty','CC20202_semantic.py',52),
  ('new_scope -> <empty>','new_scope',0,'p_new_scope','CC20202_semantic.py',57),
  ('new_loop_scope -> <empty>','new_loop_scope',0,'p_new_loop_scope','CC20202_semantic.py',62),
  ('PROGRAM -> new_scope STATEMENT','PROGRAM',2,'p_prog_statment','CC20202_semantic.py',67),
  ('PROGRAM -> new_scope FUNCLIST','PROGRAM',2,'p_prog_statment','CC20202_semantic.py',68),
  ('PROGRAM -> empty','PROGRAM',1,'p_prog_statment','CC20202_semantic.py',69),
  ('FUNCLIST -> FUNCDEF FUNCLISTAUX','FUNCLIST',2,'p_funclist_funcdef','CC20202_semantic.py',79),
  ('FUNCLISTAUX -> FUNCLIST','FUNCLISTAUX',1,'p_funclistaux_funclist','CC20202_semantic.py',84),
  ('FUNCLISTAUX -> empty','FUNCLISTAUX',1,'p_funclistaux_funclist','CC20202_semantic.py',85),
  ('FUNCDEF -> DEF IDENT new_scope LPAREN PARAMLIST RPAREN LBRACKETS STATELIST RBRACKETS','FUNCDEF',9,'p_funcdef','CC20202_semantic.py',91),
  ('PARAMLIST -> DATATYPE IDENT PARAMLISTAUX','PARAMLIST',3,'p_paralist_param','CC20202_semantic.py',102),
  ('PARAMLIST -> empty','PARAMLIST',1,'p_paralist_param','CC20202_semantic.py',103),
  ('PARAMLISTAUX -> COMMA PARAMLIST','PARAMLISTAUX',2,'p_paramlistaux_paramlist','CC20202_semantic.py',112),
  ('PARAMLISTAUX -> empty','PARAMLISTAUX',1,'p_paramlistaux_paramlist','CC20202_semantic.py',113),
  ('DATATYPE -> INT_KEYWORD','DATATYPE',1,'p_datatype','CC20202_semantic.py',119),
  ('DATATYPE -> FLOAT_KEYWORD','DATATYPE',1,'p_datatype','CC20202_semantic.py',120),
  ('DATATYPE -> STRING_KEYWORD','DATATYPE',1,'p_datatype','CC20202_semantic.py',121),
  ('STATEMENT -> VARDECL SEMICOLON','STATEMENT',2,'p_statement_vardecl','CC20202_semantic.py',127),
  ('STATEMENT -> ATRIBSTAT SEMICOLON','STATEMENT',2,'p_statement_atrib','CC20202_semantic.py',132),
  ('STATEMENT -> PRINTSTAT SEMICOLON','STATEMENT',2,'p_statement_print','CC20202_semantic.py',137),
  ('STATEMENT -> READSTAT SEMICOLON','STATEMENT',2,'p_statement_read','CC20202_semantic.py',142),
  ('STATEMENT -> RETURNSTAT SEMICOLON','STATEMENT',2,'p_statement_return','CC20202_semantic.py',147),
  ('STATEMENT -> IFSTAT','STATEMENT',1,'p_statement_if','CC20202_semantic.py',152),
  ('STATEMENT -> FORSTAT','STATEMENT',1,'p_statement_for','CC20202_semantic.py',157),
  ('STATEMENT -> new_scope LBRACKETS STATELIST RBRACKETS','STATEMENT',4,'p_statement_statelist','CC20202_semantic.py',162),
  ('STATEMENT -> BREAK SEMICOLON','STATEMENT',2,'p_statement_break','CC20202_semantic.py',168),
  ('STATEMENT -> SEMICOLON','STATEMENT',1,'p_statement_end','CC20202_semantic.py',176),
  ('VARDECL -> DATATYPE IDENT OPT_VECTOR','VARDECL',3,'p_vardecl','CC20202_semantic.py',181),
  ('OPT_VECTOR -> LSQBRACKETS INT_CONSTANT RSQBRACKETS OPT_VECTOR','OPT_VECTOR',4,'p_opt_vector','CC20202_semantic.py',188),
  ('OPT_VECTOR -> empty','OPT_VECTOR',1,'p_opt_vector','CC20202_semantic.py',189),
  ('ATRIBSTAT -> LVALUE ATTRIBUTION ATRIB_RIGHT','ATRIBSTAT',3,'p_atribstat','CC20202_semantic.py',198),
  ('ATRIB_RIGHT -> FUNCCALL_OR_EXPRESSION','ATRIB_RIGHT',1,'p_atribright_func_or_exp','CC20202_semantic.py',203),
  ('ATRIB_RIGHT -> ALLOCEXPRESSION','ATRIB_RIGHT',1,'p_atribright_alloc','CC20202_semantic.py',208),
  ('FUNCCALL_OR_EXPRESSION -> PLUS FACTOR REC_UNARYEXPR REC_PLUS_MINUS_TERM OPT_REL_OP_NUM_EXPR','FUNCCALL_OR_EXPRESSION',5,'p_funccall_or_exp_plus','CC20202_semantic.py',213),
  ('FUNCCALL_OR_EXPRESSION -> MINUS FACTOR REC_UNARYEXPR REC_PLUS_MINUS_TERM OPT_REL_OP_NUM_EXPR','FUNCCALL_OR_EXPRESSION',5,'p_funccall_or_exp_minus','CC20202_semantic.py',218),
  ('FUNCCALL_OR_EXPRESSION -> INT_CONSTANT REC_UNARYEXPR REC_PLUS_MINUS_TERM OPT_REL_OP_NUM_EXPR','FUNCCALL_OR_EXPRESSION',4,'p_funccall_or_exp_int','CC20202_semantic.py',223),
  ('FUNCCALL_OR_EXPRESSION -> FLOAT_CONSTANT REC_UNARYEXPR REC_PLUS_MINUS_TERM OPT_REL_OP_NUM_EXPR','FUNCCALL_OR_EXPRESSION',4,'p_funccall_or_exp_float','CC20202_semantic.py',228),
  ('FUNCCALL_OR_EXPRESSION -> STRING_CONSTANT REC_UNARYEXPR REC_PLUS_MINUS_TERM OPT_REL_OP_NUM_EXPR','FUNCCALL_OR_EXPRESSION',4,'p_funccall_or_exp_string','CC20202_semantic.py',233),
  ('FUNCCALL_OR_EXPRESSION -> NULL REC_UNARYEXPR REC_PLUS_MINUS_TERM OPT_REL_OP_NUM_EXPR','FUNCCALL_OR_EXPRESSION',4,'p_funccall_or_exp_null','CC20202_semantic.py',238),
  ('FUNCCALL_OR_EXPRESSION -> LPAREN NUMEXPRESSION RPAREN REC_UNARYEXPR REC_PLUS_MINUS_TERM OPT_REL_OP_NUM_EXPR','FUNCCALL_OR_EXPRESSION',6,'p_funccall_or_exp_parentesis','CC20202_semantic.py',243),
  ('FUNCCALL_OR_EXPRESSION -> IDENT FOLLOW_IDENT','FUNCCALL_OR_EXPRESSION',2,'p_funccall_or_exp_ident','CC20202_semantic.py',248),
  ('FOLLOW_IDENT -> OPT_ALLOC_NUMEXP REC_UNARYEXPR REC_PLUS_MINUS_TERM OPT_REL_OP_NUM_EXPR','FOLLOW_IDENT',4,'p_follow_ident_alloc','CC20202_semantic.py',253),
  ('FOLLOW_IDENT -> LPAREN PARAMLISTCALL RPAREN','FOLLOW_IDENT',3,'p_follow_ident_parentesis','CC20202_semantic.py',258),
  ('PARAMLISTCALL -> IDENT PARAMLISTCALLAUX','PARAMLISTCALL',2,'p_paramlistcall_ident','CC20202_semantic.py',263),
  ('PARAMLISTCALL -> empty','PARAMLISTCALL',1,'p_paramlistcall_ident','CC20202_semantic.py',264),
  ('PARAMLISTCALLAUX -> COMMA PARAMLISTCALL','PARAMLISTCALLAUX',2,'p_paramlistcallaux','CC20202_semantic.py',270),
  ('PARAMLISTCALLAUX -> empty','PARAMLISTCALLAUX',1,'p_paramlistcallaux','CC20202_semantic.py',271),
  ('PRINTSTAT -> PRINT EXPRESSION','PRINTSTAT',2,'p_printstat','CC20202_semantic.py',277),
  ('READSTAT -> READ LVALUE','READSTAT',2,'p_readstat','CC20202_semantic.py',282),
  ('RETURNSTAT -> RETURN','RETURNSTAT',1,'p_returnstat','CC20202_semantic.py',287),
  ('IFSTAT -> IF LPAREN EXPRESSION RPAREN new_scope LBRACKETS STATELIST RBRACKETS OPT_ELSE','IFSTAT',9,'p_ifstat','CC20202_semantic.py',292),
  ('OPT_ELSE -> ELSE new_scope LBRACKETS STATELIST RBRACKETS','OPT_ELSE',5,'p_opt_else','CC20202_semantic.py',298),
  ('OPT_ELSE -> empty','OPT_ELSE',1,'p_opt_else','CC20202_semantic.py',299),
  ('FORSTAT -> FOR LPAREN ATRIBSTAT SEMICOLON EXPRESSION SEMICOLON ATRIBSTAT RPAREN new_loop_scope LBRACKETS STATELIST RBRACKETS','FORSTAT',12,'p_forstat','CC20202_semantic.py',307),
  ('STATELIST -> STATEMENT OPT_STATELIST','STATELIST',2,'p_statelist','CC20202_semantic.py',312),
  ('OPT_STATELIST -> STATELIST','OPT_STATELIST',1,'p_opt_statelist','CC20202_semantic.py',317),
  ('OPT_STATELIST -> empty','OPT_STATELIST',1,'p_opt_statelist','CC20202_semantic.py',318),
  ('ALLOCEXPRESSION -> NEW DATATYPE LSQBRACKETS NUMEXPRESSION RSQBRACKETS OPT_ALLOC_NUMEXP','ALLOCEXPRESSION',6,'p_allocexp','CC20202_semantic.py',324),
  ('OPT_ALLOC_NUMEXP -> LSQBRACKETS NUMEXPRESSION RSQBRACKETS OPT_ALLOC_NUMEXP','OPT_ALLOC_NUMEXP',4,'p_opt_allocexp','CC20202_semantic.py',329),
  ('OPT_ALLOC_NUMEXP -> empty','OPT_ALLOC_NUMEXP',1,'p_opt_allocexp','CC20202_semantic.py',330),
  ('EXPRESSION -> NUMEXPRESSION OPT_REL_OP_NUM_EXPR','EXPRESSION',2,'p_expression','CC20202_semantic.py',339),
  ('OPT_REL_OP_NUM_EXPR -> REL_OP NUMEXPRESSION','OPT_REL_OP_NUM_EXPR',2,'p_opt_rel_op_num_expr','CC20202_semantic.py',344),
  ('OPT_REL_OP_NUM_EXPR -> empty','OPT_REL_OP_NUM_EXPR',1,'p_opt_rel_op_num_expr','CC20202_semantic.py',345),
  ('REL_OP -> LOWER_THAN','REL_OP',1,'p_relop_lt','CC20202_semantic.py',351),
  ('REL_OP -> GREATER_THAN','REL_OP',1,'p_relop_gt','CC20202_semantic.py',356),
  ('REL_OP -> LOWER_OR_EQUALS_THAN','REL_OP',1,'p_relop_lte','CC20202_semantic.py',361),
  ('REL_OP -> GREATER_OR_EQUALS_THAN','REL_OP',1,'p_relop_gte','CC20202_semantic.py',366),
  ('REL_OP -> EQ_COMPARISON','REL_OP',1,'p_relop_eq','CC20202_semantic.py',370),
  ('REL_OP -> NEQ_COMPARISON','REL_OP',1,'p_relop_neq','CC20202_semantic.py',375),
  ('NUMEXPRESSION -> TERM REC_PLUS_MINUS_TERM','NUMEXPRESSION',2,'p_numexp','CC20202_semantic.py',380),
  ('REC_PLUS_MINUS_TERM -> PLUS_OR_MINUS TERM REC_PLUS_MINUS_TERM','REC_PLUS_MINUS_TERM',3,'p_rec_plus_minus','CC20202_semantic.py',385),
  ('REC_PLUS_MINUS_TERM -> empty','REC_PLUS_MINUS_TERM',1,'p_rec_plus_minus','CC20202_semantic.py',386),
  ('PLUS_OR_MINUS -> PLUS','PLUS_OR_MINUS',1,'p_plus','CC20202_semantic.py',392),
  ('PLUS_OR_MINUS -> MINUS','PLUS_OR_MINUS',1,'p_minus','CC20202_semantic.py',397),
  ('TERM -> UNARYEXPR REC_UNARYEXPR','TERM',2,'p_term_unary_exp','CC20202_semantic.py',402),
  ('REC_UNARYEXPR -> UNARYEXPR_OP TERM','REC_UNARYEXPR',2,'p_rec_unaryexp_op','CC20202_semantic.py',407),
  ('REC_UNARYEXPR -> empty','REC_UNARYEXPR',1,'p_rec_unaryexp_op','CC20202_semantic.py',408),
  ('UNARYEXPR_OP -> TIMES','UNARYEXPR_OP',1,'p_rec_unaryexp_times','CC20202_semantic.py',417),
  ('UNARYEXPR_OP -> MODULE','UNARYEXPR_OP',1,'p_rec_unaryexp_times','CC20202_semantic.py',418),
  ('UNARYEXPR_OP -> DIVIDE','UNARYEXPR_OP',1,'p_rec_unaryexp_times','CC20202_semantic.py',419),
  ('UNARYEXPR -> PLUS_OR_MINUS FACTOR','UNARYEXPR',2,'p_rec_unaryexp_plusminus','CC20202_semantic.py',424),
  ('UNARYEXPR -> FACTOR','UNARYEXPR',1,'p_rec_unaryexp_factor','CC20202_semantic.py',430),
  ('FACTOR -> INT_CONSTANT','FACTOR',1,'p_factor_int_cte','CC20202_semantic.py',435),
  ('FACTOR -> FLOAT_CONSTANT','FACTOR',1,'p_factor_float_cte','CC20202_semantic.py',440),
  ('FACTOR -> STRING_CONSTANT','FACTOR',1,'p_factor_string_cte','CC20202_semantic.py',445),
  ('FACTOR -> NULL','FACTOR',1,'p_factor_null','CC20202_semantic.py',450),
  ('FACTOR -> LVALUE','FACTOR',1,'p_factor_lvalue','CC20202_semantic.py',455),
  ('FACTOR -> LPAREN NUMEXPRESSION RPAREN','FACTOR',3,'p_factor_expr','CC20202_semantic.py',460),
  ('LVALUE -> IDENT OPT_ALLOC_NUMEXP','LVALUE',2,'p_lvalue_ident','CC20202_semantic.py',465),
]
