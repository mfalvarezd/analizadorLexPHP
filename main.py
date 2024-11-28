import ply.yacc as yacc
import os
import time
from AnalizadorLexPHP import tokens, lexer  # Reutilizamos el lexer definido en AnalizadorLexPHP

def p_inicio(p):
    '''inicio : OPENTAG programa CLOSETAG'''

def p_programa(p):
    '''programa : sentencia
                | sentencia programa'''

def p_sentencia(p):
    '''sentencia : asignacion
                | asignacion_fgets
                | comparacion
                | impresion
                | estructurasPrograma
                | try
                | funcionDeclaration
                | returnStatement
                | llamadaFuncion
                | classDeclarate
                | interface
                | objeto
                | includes
                | namespace
                | anonymousFunction
                | throw
                | instance
                | constdeclaration
                | thisdeclaration
                | concatenate
                | minuse
                
                '''

def p_returnStatement(p):
    '''returnStatement : RETURN expresion SEMICOLON
                       | RETURN SEMICOLON'''



def p_asignacion(p):
    '''asignacion : VARIABLE EQUALS expresion SEMICOLON'''
def p_expresion(p):
    '''expresion : valor
                 | expresion opLogic expresion
                 | comparacion
                 | LPAREN comparacion RPAREN
                 | operaArit
                 | LPAREN expresion RPAREN
                 '''

def p_asignacion_fgets(p):
    '''asignacion_fgets : VARIABLE EQUALS FGETS LPAREN STDIN RPAREN SEMICOLON'''
    variable = p[1]  # Nombre de la variable
    print(f"Asigna a {variable} el valor ingresado por el usuario.")


#Semántico 1
def p_operaArit(p):
    '''operaArit : valor
                 | operaArit operador operaArit
                 | LPAREN operaArit RPAREN
                 '''

def p_valornumerico(p):
    '''valornumerico : INT
                    | FLOAT
                    | VARIABLE'''

def p_valor(p):
    '''valor : INT
            | VARIABLE
            | FLOAT
            | STRING
            | BOOL
            | NULL
            | ARRAY
            | llamadaFuncion
            
            '''

def p_operador(p):
    '''operador : PLUS
                | MINUS
                | TIMES
                | DIVIDE
                | MODULO
                | POTENCIA
                | PLUSEQUAL'''

#Semántico 2
def p_comparacion(p):
    '''comparacion : valor opSymbol valor
                    | expresion opSymbol expresion'''



def p_impresion(p):
    '''impresion : ECHO imprimir SEMICOLON
                | PRINT imprimir SEMICOLON'''

def p_imprimir(p):
    '''imprimir : LPAREN repiteValores RPAREN
                | LPAREN RPAREN
                | repiteValores
                | empty'''

def p_repiteValores(p):
    '''repiteValores : valor
                    | valor COMMA repiteValores'''

def p_empty(p):
    '''empty :'''

def p_estructurasPrograma(p):
    '''estructurasPrograma : controlStructure
                        | dataStructure'''

def p_controlStructure(p):
    '''controlStructure : if
                        | for
                        | while
                        | dowhile
                        | switch
                        | foreach'''

def p_if(p):
    '''if : IF LPAREN conditions RPAREN LBRACE body RBRACE else_blocks
          | IF LPAREN conditions RPAREN body'''

def p_else_blocks(p):
    '''else_blocks : ELSE LBRACE body RBRACE
                   | ELSEIF LPAREN conditions RPAREN LBRACE body RBRACE else_blocks
                   | empty'''

def p_conditions(p):
     '''conditions : condition
                   | condition opLogic conditions
                   | LPAREN conditions RPAREN'''

def p_condition(p):
     '''condition : valor
                  | valor opSymbol valor
                  | NOT condition
                  | LPAREN conditions RPAREN'''

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
                | LOGICAL_AND
                | OR
                | LOGICAL_OR
                '''

def p_body(p):
     '''body : sentenciaList          
            | empty'''

def p_sentenciaList(p):
    '''sentenciaList : sentencia
                    | sentencia sentenciaList'''

def p_for(p):
    '''for : forStatement'''

def p_forStatement(p):
    '''forStatement : FOR LPAREN forcondition RPAREN LBRACE body RBRACE'''

def p_forcondition(p):
    '''forcondition : VARIABLE EQUALS INT SEMICOLON VARIABLE opSymbol INT SEMICOLON VARIABLE DOUBLEPLUS
                    | VARIABLE EQUALS INT SEMICOLON VARIABLE opSymbol INT SEMICOLON VARIABLE DOUBLEMINUS'''

def p_while(p):
    '''while : WHILE LPAREN condition RPAREN LBRACE body RBRACE
            | WHILE LPAREN condition RPAREN LBRACE RBRACE'''

def p_dowhile(p):
    '''dowhile : DO LBRACE body RBRACE WHILE LPAREN condition RPAREN SEMICOLON'''

def p_switch(p):
    '''switch : SWITCH LPAREN valor RPAREN LBRACE caseLists RBRACE
              | SWITCH LPAREN valor RPAREN COLON caseLists ENDSWITCH SEMICOLON'''

def p_caseLists(p):
    '''caseLists : cases
                 | cases default
                 | default
                 | empty'''

def p_cases(p):
    '''cases : case
             | case cases'''

def p_foreach(p):
    '''foreach : FOREACH LPAREN VARIABLE AS VARIABLE RPAREN LBRACE body RBRACE'''

def p_case(p):
    '''case : CASE valor COLON body BREAK SEMICOLON
            | CASE valor SEMICOLON body BREAK SEMICOLON
            | CASE valor COLON body
            | CASE valor SEMICOLON
            | CASE valor'''

def p_dataStructure(p):
    '''dataStructure : array'''

def p_array(p):
    '''array : VARIABLE EQUALS arrays SEMICOLON
            | VARIABLE EQUALS LBRACKET arrayAnidado RBRACKET SEMICOLON
            | VARIABLE EQUALS ARRAY LPAREN repiteValores RPAREN SEMICOLON
            | map'''

def p_arrays(p):
    '''arrays : LBRACKET repiteValores RBRACKET'''

def p_arrayAnidado(p):
    '''arrayAnidado : arrays
                    | arrays COMMA arrayAnidado'''

def p_map(p):
    '''map : VARIABLE EQUALS LBRACKET maps RBRACKET SEMICOLON
            | VARIABLE EQUALS ARRAY LPAREN maps RPAREN SEMICOLON'''

def p_maps(p):
    '''maps : mapArrow
            | mapArrow COMMA maps'''

def p_mapArrow(p):
    '''mapArrow : valor ARROWMAP valor'''

def p_default(p):
    '''default : DEFAULT COLON body BREAK SEMICOLON
               | DEFAULT SEMICOLON body BREAK SEMICOLON
               | DEFAULT COLON body
               | DEFAULT SEMICOLON body
               | DEFAULT'''

def p_argumentos(p):
    '''argumentos : argumento   
                  | argumento COMMA argumentos
                  | empty'''

def p_argumento(p):
    '''argumento : type VARIABLE
                 | VARIABLE EQUALS valor
                 | type VARIABLE EQUALS valor
                 | operaArit'''

def p_type(p):
    '''type : INT_TYPE
            | FLOAT_TYPE
            | STRING_TYPE
            | BOOL_TYPE
            | ARRAY_TYPE
            | VOID
            '''

def p_try(p):
    '''try : TRY LBRACE body RBRACE catchs
            | TRY LBRACE body RBRACE catchs FINALLY LBRACE body RBRACE '''

def p_catch(p):
    '''catch : CATCH LPAREN EXCEPTION VARIABLE RPAREN LBRACE body RBRACE'''

def p_catchs(p):
    '''catchs : catch
            | catch catchs'''

def p_objeto(p):
    '''objeto : VARIABLE ARROW ID LPAREN argumentos RPAREN SEMICOLON   '''

def p_funcionDeclaration(p):
    '''funcionDeclaration : FUNCTION ID LPAREN argumentos RPAREN LBRACE body RBRACE'''

def p_llamadaFuncion(p):
    '''llamadaFuncion : ID LPAREN argumentos RPAREN SEMICOLON
                      | EMPTY LPAREN argumentos RPAREN
                      | ID LPAREN argumentos RPAREN
                      | EMPTY LPAREN argumentos RPAREN SEMICOLON''' 

def p_classDeclarate(p):
    '''classDeclarate : CLASS ID LBRACE classBody RBRACE
                    | CLASS ID EXTENDS ID LBRACE classBody RBRACE
                    | data CLASS ID LBRACE classBody RBRACE
                    | classInterface'''

def p_classBody(p):
    '''classBody : classMember
                | classMember classBody'''

def p_classMember(p):
    '''classMember : type VARIABLE SEMICOLON
                    | type FUNCTION ID LPAREN argumentos RPAREN LBRACE body RBRACE
                    | objectInstantiation'''

def p_objectInstantiation(p):
    '''objectInstantiation : NEW ID LPAREN argumentos RPAREN
                            | NEW ID LPAREN RPAREN'''

def p_classInterface(p):
    '''classInterface : CLASS ID IMPLEMENTS impInterface LBRACE classBody RBRACE
                    | CLASS ID EXTENDS ID IMPLEMENTS impInterface LBRACE classBody RBRACE
                    | data CLASS ID IMPLEMENTS impInterface LBRACE classBody RBRACE
                    | data CLASS ID EXTENDS ID IMPLEMENTS impInterface LBRACE classBody RBRACE'''

def p_impInterface(p):
    '''impInterface : ID
                    | ID COMMA impInterface'''

def p_data(p):
    '''data : ABSTRACT
            | PRIVATE
            | PROTECTED
            | PUBLIC
            | STATIC
            | FINAL'''

def p_interface(p):
    '''interface : INTERFACE ID LBRACE classBody RBRACE'''

def p_includes(p):
    '''includes : INCLUDE STRING SEMICOLON
                | INCLUDE STRING DOT STRING SEMICOLON'''

def p_namespace(p):
    '''namespace : NAMESPACE ID SEMICOLON'''

def p_anonymousFunction(p):
    'anonymousFunction : VARIABLE EQUALS FN LPAREN RPAREN ARROWMAP comparacion SEMICOLON'

def p_throw(p):
    '''throw : THROW NEW EXCEPTION LPAREN repiteValores RPAREN SEMICOLON
            | THROW valor SEMICOLON'''

def p_instance(p):
    '''instance : VARIABLE INSTANCEOF ID'''

def p_constdeclaration(p):
    '''constdeclaration : CONST ID EQUALS valor SEMICOLON'''

def p_thisdeclaration(p):
    '''thisdeclaration : THIS ARROW ID SEMICOLON
                        | THIS ARROW ID LPAREN RPAREN SEMICOLON'''

#Semántica 3
def p_concatenate(p):
    '''concatenate : VARIABLE CONCATENATEEQUAL STRING'''

#Semántica 4
def p_minuse(p):
    '''minuse : VARIABLE MINUSEQUAL INT'''

#Semántica 5
#def p_pluse(p):
#   '''pluse : VARIABLE PLUSEQUAL INT'''

#Semántica 6
def p_funcion_strlen(p):
    '''funcion : STRLEN LPAREN STRING RPAREN'''

# Diccionario para almacenar las variables y sus valores
variable_types = {}

# Asignación de valor a una variable
def p_statement_valor(p):
    '''statement_valor : VARIABLE EQUALS valornumerico'''
    var_name = p[1]
    value = p[3]

    # Verificar el tipo de la variable antes de asignar el valor
    if isinstance(value, (int, float, str)):  # Verifica si el valor es válido
        variable_types[var_name] = value
        p[0] = f"{var_name} = {value}"
    else:
        raise TypeError(f"Tipo de dato no válido para la asignación a {var_name}")

# Manejo de la operación += con validación de tipos
def p_statement_plusequal(p):
    '''statement_plusequal : VARIABLE EQUALS VARIABLE PLUSEQUAL INT'''
    
    var_name = p[1]  # Nombre de la variable que recibirá el nuevo valor
    variable_name = p[3]  # Nombre de la variable cuyo valor se está modificando
    increment_value = p[4]  # El valor que se va a sumar
    
    # Obtener el valor actual de la variable que se está modificando
    current_value = variable_types.get(variable_name)
    
    if current_value is None:
        raise ValueError(f"Variable {variable_name} no definida")
    
    # Verificar que el tipo de la variable sea un número entero (o flotante)
    if not isinstance(current_value, (int, float)):
        raise TypeError(f"Tipo de variable {variable_name} no es un número. Se esperaba un número para la operación de suma.")
    
    # Realizar la operación de incremento
    new_value = current_value + increment_value
    
    # Asignar el nuevo valor a la variable que está siendo modificada
    variable_types[variable_name] = new_value
    
    # Luego asignamos el resultado de la operación a la nueva variable
    variable_types[var_name] = new_value
    
    # Devolver el resultado para esta regla semántica
    p[0] = f"{var_name} = {variable_name} + {increment_value}"

# Manejo de valores enteros
def p_expr_int(p):
    '''expr : INT'''
    p[0] = int(p[1])  # El valor es de tipo entero

# Manejo de valores de tipo cadena
def p_expr_string(p):
    '''expr : STRING'''
    p[0] = str(p[1])  # El valor es de tipo cadena


# Inicializar la lista de errores sintácticos
errores_sintacticos = []

# Función para manejar errores de sintaxis
def p_error(p):
    if p:
        # Reportar el error sintáctico, su valor y la línea
        mensaje = f"Error de sintaxis - Token: {p.type} ('{p.value}'), Línea: {p.lineno}, Columna: {p.lexpos}"
        errores_sintacticos.append(mensaje)
        print(mensaje)
        parser.errok()
    else:
        errores_sintacticos.append("Error, sentencia incompleta")
        print("Error de sintaxis: Fin de entrada inesperado.")
        

# Crear el parser
lexer.lineno = 1  # Reinicia el contador de líneas del lexer

parser = yacc.yacc()

def getAnalizadorSintactico():
    return yacc.yacc()


