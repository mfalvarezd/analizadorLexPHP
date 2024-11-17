import ply.yacc as yacc
from AnalizadorLexPHP import tokens


def p_programa(p):
    '''programa : sentencia
                | sentencia programa'''

def p_sentencia(p):
    '''sentencia : asignacion
                | impresion
                | comparacion
                | estructurasProgram'''


#asignacion de variable
def p_asignacion(p):
    '''asignacion : VARIABLE EQUALS operaArit SEMICOLON'''


#Imprimir uno o mas valores con echo y print
def p_impresion(p):
    '''impresion : ECHO imprimir SEMICOLON
                | PRINT imprimir SEMICOLON'''

#estructurasPrograma
def p_estructurasProgram(p):
    '''estructurasProgram : controlStructure
                            | dataStructure
                            | funcionDeclarate
                            | classDeclarate'''

def p_controlStructure(p):
    '''controlStructure : if
                        | for
                        | while
                        | switch'''
#SECCION DEL IF
def p_if(p):
    '''if : statementif ELSE statementif
        | statementif ELSE LBRACE condition RBRACE
        | statementif ELSEIF statementif
        | statementif'''

def p_statementif(p):
    '''statementif : IF LPAREN p_conditionProdu RPAREN LBRACE body RBRACE'''

def p_conditionProdu(p):
    '''conditionProdu : condition
                    | condition opSymbol conditionProdu'''
def p_condition(p):
    '''condition : valor opSymbol valor'''

def opSymbol(p):
    '''opSymbol : EQ
                | NEQ
                | STRICTEQ
                | STRICTNEQ
                | LT
                | GT
                | LEQ
                | GEQ'''
def p_opLogic(p):
    '''opLogic : AND
                | OR
                | NOT'''

#SECCION DEL FOR
def p_for(p):
    '''for : forStatement'''

def p_forStatement(p):
    '''forStatement : FOR LPAREN forcondition RPAREN LBRACE body RBRACE'''

def p_forcondition(p):
    '''forcondition : VARIABLE EQUALS INT SEMICOLON VARIABLE opSymbol INT SEMICOLON VARIABLE DOUBLEPLUS
                    | VARIABLE EQUALS INT SEMICOLON VARIABLE opSymbol INT SEMICOLON VARIABLE DOUBLEMINUS'''


def p_while(p):
    '''while : '''

def p_switch(p):
    '''switch : '''

def p_dataStructure(p):
    '''dataStructure : array
                    | map'''

def p_funcionDeclarate(p):
    '''funcionDeclarate : FUNCTION funcionParen brace
                        | FUNCTION funcionParen DOUBLEDOT dataType brace
                        | '''
def p_arrowfunction(p):
    '''arrowfunction : FN LPAREN repiteValores RPAREN ARROWMAP operaArit SEMICOLON body'''

def p_brace(p):
    '''brace : LBRACE body RBRACE'''

def p_funcionParen(p):
    '''funcionParen : ID LPAREN repiteValores RPAREN'''

def classDeclarate(p):
    '''classDeclarate : '''

def p_array(p):
    '''array : VARIABLE EQUALS LBRACKET repiteValores RBRACKET SEMICOLON
             | VARIABLE EQUALS ARRAY LPAREN repiteValores RPAREN SEMICOLON '''

def p_map(p):
    '''map : VARIABLE EQUALS LBRACKET mapProduc RBRACKET SEMICOLON
            | VARIABLE EQUALS ARRAY LPAREN mapProduc RPAREN SEMICOLON'''

def p_mapProduc(p):
    '''mapProduc : mapProduct
            | mapProudct COMMA map'''

def p_mapArrow(p):
    '''mapArrow : valor ARROWMAP valor'''
#definir body
def p_body(p):
    '''body : '''

def p_imprimir(p):
    '''imprimir : LPAREN repiteValores RPAREN
                | LPAREN RPAREN
                | repiteValores'''

def p_valor(t):
    '''valor : INT
            | FLOAT
            | VARIABLE
            | STRING
            | funcionParen'''

def p_dataType(p):
    '''dataType : INTEGER
                | FLOATING
                | STRINGS
                | BOOLEAN
                | VOID'''

def p_comparacion(p):
    '''comparacion : INT operador INT
                    | FLOAT operador FLOAT
                    | INT operador FLOAT
                    | FLOAT operador INT'''

def p_valorBool(p):
    '''valor : TRUE
            | FALSE'''

def p_repiteValores(p):
    '''repiteValores : valor COMMA repiteValores
                | valor
                | empty'''

def p_operaArit(p):
    '''operaArit : valor
                |  valor operador operaArit'''

def p_operador(p):
    '''operador :  PLUS
                | MINUS
                | TIMES
                | DIVIDE
                | MODULO'''

def p_empty(p):
    '''empty :'''

def p_error(p):
    print("Error de sintáxis en la línea %d" % p.lineno)

parser = yacc.yacc()

while True:
    try:
        s = input('python > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)

