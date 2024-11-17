import ply.yacc as yacc
from AnalizadorLexPHP import tokens


def p_programa(p):
    '''programa : sentencia
                | sentencia programa'''

def p_sentencia(p):
    '''sentencia : asignacion
                | impresion
                | comparacion'''


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

def p_dataStructure(p):
    '''dataStructure : array
                    | '''

def p_funcionDeclarate(p):
    '''funcionDeclarate : '''

def p_classDeclarate(p):
    '''classDeclarate : '''

def p_condition(p):
    '''condition : IF LPAREN valor RPAREN LBRACE RBRACE'''

def p_if(p):
    '''if : IF'''

def p_for(p):
    '''for : FOR'''

def p_while(p):
    '''while : WHILE'''

def p_switch(p):
    '''switch: SWITCH'''

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

#para declaracion de clases o funciones
def p_dataType(p):
    '''dataType : VOID
                | '''

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