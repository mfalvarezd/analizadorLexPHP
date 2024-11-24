import ply.yacc as yacc
from AnalizadorLexPHP import tokens
import os
import time
from AnalizadorLexPHP import tokens, lexer  # Reutilizamos el lexer definido en AnalizadorLexPHP

def p_programa(p):
    '''programa : sentencia
                | sentencia programa'''

def p_sentencia(p):
    '''sentencia : asignacion
                | impresion
                | comparacion
                | estructurasProgram
                | asignacion_fgets
                | sentenceTryCatch
                | namespace'''


#Jair Chaguay - Entrada de datos
def p_asignacion_fgets(p):
    '''asignacion_fgets : VARIABLE EQUALS FGETS LPAREN STDIN RPAREN SEMICOLON'''
    variable = p[1]  # Nombre de la variable
    print(f"Asigna a {variable} el valor ingresado por el usuario.")


def p_sentencias(p):
    '''sentencias : sentencia
                  | sentencia sentencias
                  | empty'''

# Jair Chaguay asignacion de variable
def p_asignacion(p):
    '''asignacion : VARIABLE EQUALS operaArit SEMICOLON'''


#Jair Chaguay Imprimir uno o mas valores con echo y print
def p_impresion(p):
    '''impresion : ECHO imprimir SEMICOLON
                | PRINT imprimir SEMICOLON'''

#Jair Chaguay estructurasPrograma
def p_estructurasProgram(p):
    '''estructurasProgram : controlStructure
                            | dataStructure
                            | funcionDeclarate
                            | classDeclarate'''

#Jair Chaguay Estructuras de Control
def p_controlStructure(p):
    '''controlStructure : if
                        | for
                        | while
                        | switch
                        | dowhile'''
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
                    | condition opLogic condition conditionProdu'''
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
    '''for : forStatement
            | forEachStatement'''

def p_forStatement(p):
    '''forStatement : FOR LPAREN forcondition RPAREN LBRACE body RBRACE
                    | FOREACH LPAREN forcondition RPAREN LBRACE body BREAK SEMICOLON RBRACE'''

def p_forEachStatement(p):
    '''forEachStatement : FOREACH LPAREN VARIABLE AS VARIABLE RPAREN LBRACE body RBRACE
                        | FOREACH LPAREN VARIABLE AS VARIABLE DOUBLEARROW VARIABLE RPAREN LBRACE body RBRACE'''

def p_forcondition(p):
    '''forcondition : VARIABLE EQUALS INT SEMICOLON VARIABLE opSymbol INT SEMICOLON VARIABLE DOUBLEPLUS
                    | VARIABLE EQUALS INT SEMICOLON VARIABLE opSymbol INT SEMICOLON VARIABLE DOUBLEMINUS'''

def p_namespace(p):
    '''namespace : NAMESPACE ID SEMICOLON'''
##moises Alvarez
def p_while(p):
    '''while : WHILE LPAREN condition RPAREN LBRACE body RBRACE
             | WHILE LPAREN condition RPAREN LBRACE RBRACE'''

def dowhile(p):
    '''dowhile : DO LBRACE body RBRACE WHILE LPAREN condition RPAREN SEMICOLON'''

#Corregir SWITCH NO ES ASI LA ESTRUCUTRA DEL SWITCH
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

def p_exception(p):
    '''exception : '''

def p_sentenceTryCatch(p):
    '''sentenceTryCatch : TRY LBRACE body RBRACE catchBlocks finallyBlock
                        | TRY LBRACE body RBRACE catchBlocks'''

def p_catchBlocks(p):
    '''catchBlocks : CATCH LPAREN EXCEPTION ID RPAREN LBRACE body RBRACE catchBlocks
                    | CATCH LPAREN EXCEPTION ID RPAREN LBRACE body RBRACE
                    | empty'''

def p_finallyBlock(p):
    '''finallyBlock : FINALLY LBRACE body RBRACE'''

def p_catchs(p):
    '''catchs : CATCH LPAREN EXCEPTION ID RPAREN LBRACE RBRACE'''

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

def p_brace(p):
    '''brace : LBRACE body RBRACE'''

def p_funcionParen(p):
    '''funcionParen : ID LPAREN parametros RPAREN'''

def p_funcionAnonima(p):
    '''funcionAnonima : VARIABLE EQUALS FUNCTION LPAREN parametros RPAREN LBRACE RETURN expresion SEMICOLON RBRACE SEMICOLON'''

#moises Alvarez
def p_classDeclarate(p):
    '''classDeclarate : CLASS ID LBRACE classBody RBRACE
                      | CLASS ID EXTENDS ID LBRACE classBody RBRACE
                      | ABSTRACT CLASS ID LBRACE classBody RBRACE'''
def p_classBody(p):
    '''classBody : classMember classBody
                 | empty'''   
def p_classMember(p):
    '''classMember : dataType VARIABLE SEMICOLON
                   | dataType FUNCTION ID LPAREN parametros RPAREN brace
                   | objectInstantiation'''
def p_accessMember(p):
    '''accessMember : VARIABLE ARROW ID
                    | VARIABLE ARROW funcionParen'''

def p_objectInstantiation(p):
    '''objectInstantiation : NEW ID LPAREN argumentos RPAREN
                           | NEW ID LPAREN RPAREN'''
def p_argumentos(p):
    '''argumentos : expresion
                 | expresion COMMA argumentos
                 | empty'''


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
            | funcionParen
            | funcionAnonima'''
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

# Función para manejar errores de sintaxis
def p_error(p):
    if p:
        # Reportar solo el error sintáctico y la línea
        error_msg = f"Error de sintaxis:'{p.value}'"
        print(error_msg)
        errores_sintacticos.append(error_msg)
    else:
        # Manejar caso de fin inesperado del archivo
        error_msg = "Error de sintaxis: Fin inesperado del archivo."
        print(error_msg)
        errores_sintacticos.append(error_msg)

# Crear el parser
parser = yacc.yacc()

# Directorios de archivos
current_directory = os.path.dirname(os.path.abspath(__file__))
algoritmos_directory = os.path.join(current_directory, "algoritmos")
logs_directory = os.path.join(current_directory, "logs")
os.makedirs(algoritmos_directory, exist_ok=True)
os.makedirs(logs_directory, exist_ok=True)

# Preguntar al usuario qué tipo de análisis realizar
tipo_analisis = input("¿Desea realizar un análisis léxico o sintáctico? (l/s): ").strip().lower()
usuario_git = input("Ingrese su usuario de Git: ")
archivo_numero = input("Ingrese el número del archivo a analizar (por ejemplo, '1' para algoritmo1.php): ")

# Crear el nombre del archivo log
fecha_hora = time.strftime("%d%m%Y-%Hh%M")
log_filename = f"{tipo_analisis}-{usuario_git}-{fecha_hora}.txt"
log_filepath = os.path.join(logs_directory, log_filename)

# Procesar el archivo seleccionado
algoritmo_filename = f"algoritmo{archivo_numero}.php"
algoritmo_filepath = os.path.join(algoritmos_directory, algoritmo_filename)

try:
    with open(algoritmo_filepath, "r") as file:
        data = file.read()
except FileNotFoundError:
    print(f"El archivo {algoritmo_filename} no se encontró en la carpeta 'algoritmos'.")
    exit(1)

# Inicializar la lista de errores sintácticos
errores_sintacticos = []

# Realizar el análisis y guardar los logs
with open(log_filepath, "w") as log_file:
    if tipo_analisis == 'l':  # Análisis léxico
        lexer.input(data)
        while True:
            tok = lexer.token()
            if not tok:
                break
            log_file.write(f"Token: {tok.type}, Valor: {tok.value}, Línea: {tok.lineno}\n")
        print(f"El análisis léxico se completó y el log se guardó en: {log_filepath}")

    elif tipo_analisis == 's':  # Análisis sintáctico
        errores_sintacticos.clear()  # Limpiar la lista de errores antes de comenzar
        result = parser.parse(data)
        if errores_sintacticos:  # Si hay errores, escribirlos en el log
            for error in errores_sintacticos:
                log_file.write(error + "\n")
        else:  # Si no hay errores
            log_file.write("No se encontraron errores sintácticos.\n")
        print(f"El análisis sintáctico se completó y el log se guardó en: {log_filepath}")

    else:
        print("Opción inválida. Por favor elija 'l' o 's'.")
