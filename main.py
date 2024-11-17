import ply.yacc as yacc
from AnalizadorLexPHP import tokens


def p_programa(p):
    '''programa : sentencia
                | sentencia programa'''

def p_sentencia(p):
    '''sentencia : asignacion
                | impresion
                | comparacion'''

def p_asignacion(p):
    '''asignacion : VARIABLE EQUALS operaArit SEMICOLON'''

#Imprimir uno o mas valores con echo y print
def p_impresion(p):
    '''impresion : ECHO imprimir SEMICOLON
                | PRINT imprimir SEMICOLON'''

def p_imprimir(p):
    '''imprimir : LPAREN repiteValores RPAREN
                | LPAREN RPAREN
                | repiteValores
                | empty'''

def p_valor(t):
    '''valor : INT
            | FLOAT
            | VARIABLE
            | STRING'''

def p_comparacion(p):
    '''comparacion : INT comparador INT'''

def p_comparador(p):
    '''comparador : LT
                | GT
                | LEQ
                | GEQ'''

def p_valorBool(p):
    '''valor : TRUE
            | FALSE'''

def p_repiteValores(p):
    '''repiteValores : valor COMMA repiteValores
                | valor'''

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