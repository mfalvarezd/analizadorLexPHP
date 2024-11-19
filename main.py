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

def p_sentencias(p):
    '''sentencias : sentencia
                  | sentencia sentencias
                  | empty'''
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
## corregi lo que deberia ir despues de cada else simplemente, creo que asi queda bien
def p_if(p):
    '''if : statementif ELSE body
          | statementif ELSE if
          | statementif ELSEIF if
          | statementif'''

def p_statementif(p):
    '''statementif : IF LPAREN conditionProdu RPAREN LBRACE body RBRACE'''
##coregio la produccion de condicion porque despues de condicion debi ir un operador logico
def p_conditionProdu(p):
    '''conditionProdu : condition
                    | condition opLogic conditionProdu'''
def p_condition(p):
    '''condition : valor opSymbol valor
                 | LPAREN conditionProdu RPAREN'''

def p_opSymbol(p):
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

##moises Alvarez
def p_while(p):
    '''while : WHILE LPAREN condition RPAREN LBRACE body RBRACE
             | WHILE LPAREN condition RPAREN LBRACE RBRACE'''

def p_switch(p):
    '''switch : SWITCH LPAREN condition RPAREN LBRACE caseLists RBRACE
              | SWITCH LPAREN condition RPAREN LBRACE RBRACE'''
def p_caseLists(p):
    '''caseLists : cases default
                | cases
                | default
                | empty'''
def p_cases(p):
    '''cases : case cases
             | case'''            
def p_case(p):
    '''case : CASE valor COLON body BREAK SEMICOLON'''
def p_default(p):
    '''default : DEFAULT COLON body BREAK SEMICOLON'''

def p_dataStructure(p):
    '''dataStructure : array
                    | map'''

def p_funcionDeclarate(p):
    '''funcionDeclarate : FUNCTION ID LPAREN parametros RPAREN LBRACE funcionBody RBRACE
                        | FUNCTION ID LPAREN parametros RPAREN DOUBLEDOT dataType LBRACE funcionBody RBRACE'''
def p_funcionBody(p):
    '''funcionBody : body
                   | RETURN expresion SEMICOLON'''
                        
def p_parametros(p):
    '''parametros : parametro
                 | parametro COMMA parametros
                 | empty'''  
def p_parametro(p):
    '''parametro : ID
                | dataType ID
                | ID EQUALS valor
                | dataType ID EQUALS valor'''                                   
def p_arrowfunction(p):
    '''arrowfunction : FN LPAREN parametros RPAREN ARROWMAP expresion SEMICOLON'''

def p_brace(p):
    '''brace : LBRACE body RBRACE'''

def p_funcionParen(p):
    '''funcionParen : ID LPAREN parametros RPAREN'''

def p_funcionAnonima(p):
    '''funcionAnonima : VARIABLE EQUALS FUNCTION LPAREN parametros RPAREN LBRACE RETURN expresion SEMICOLON RBRACE SEMICOLON'''

#moises Alvarez
def p_classDeclarate(p):
    '''classDeclarate : CLASS ID LBRACE classBody RBRACE
                      | CLASS ID EXTENDS ID LBRACE classBody RBRACE'''
def p_classBody(p):
    '''classBody : classMember classBody
                 | empty'''   
def p_classMember(p):
    '''classMember : dataType VARIABLE SEMICOLON
                   | dataType FUNCTION ID LPAREN parametros RPAREN brace'''                                         
def p_accessMember(p):
    '''accessMember : VARIABLE ARROW ID
                    | VARIABLE ARROW funcionParen'''

def p_array(p):
    '''array : VARIABLE EQUALS LBRACKET repiteValores RBRACKET SEMICOLON
             | VARIABLE EQUALS ARRAY LPAREN repiteValores RPAREN SEMICOLON
             | VARIABLE EQUALS ARRAY LPAREN mapProduc RPAREN SEMICOLON
             | VARIABLE EQUALS LBRACKET mapProduc RBRACKET SEMICOLON'''

def p_map(p):
    '''map : VARIABLE EQUALS LBRACKET mapProduc RBRACKET SEMICOLON
            | VARIABLE EQUALS ARRAY LPAREN mapProduc RPAREN SEMICOLON'''

def p_mapProduc(p):
    '''mapProduc : mapArrow
                 | mapArrow COMMA mapProduc'''

def p_mapArrow(p):
    '''mapArrow : valor ARROWMAP valor'''
#definir body
def p_body(p):
    '''body : sentencia
            | sentencia sentencias
            | empty'''

def p_imprimir(p):
    
    '''imprimir : LPAREN repiteValores RPAREN
                | LPAREN RPAREN
                | repiteValores'''

def p_valor(p):
    '''valor : INT
            | FLOAT
            | VARIABLE
            | STRING
            | TRUE
            | FALSE
            | THIS
            | funcionParen'''
    p[0]=p[1]

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



def p_repiteValores(p):
    '''repiteValores : valor COMMA repiteValores
                     | valor'''
def p_operaArit(p):
    '''operaArit : valor
                |  valor operador operaArit
                | valor DOT valor'''
def p_expresion(p):
    '''expresion : valor
                 | operaArit
                 | conditionProdu
                 | ternario
                 | accessMember'''
def p_operador(p):
    '''operador :  PLUS
                | MINUS
                | TIMES
                | DIVIDE
                | MODULO'''
def p_ternario(p):
    '''ternario : conditionProdu QUESTION expresion COLON expresion'''
                

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

