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
                
                '''
def p_returnStatement(p):
    '''returnStatement : RETURN valor SEMICOLON
                       | RETURN SEMICOLON'''
def p_asignacion(p):
    '''asignacion : VARIABLE EQUALS operaArit SEMICOLON'''

def p_asignacion_fgets(p):
    '''asignacion_fgets : VARIABLE EQUALS FGETS LPAREN STDIN RPAREN SEMICOLON'''
    variable = p[1]  # Nombre de la variable
    print(f"Asigna a {variable} el valor ingresado por el usuario.")


def p_operaArit(p):
    '''operaArit : valor
                | valor operador operaArit'''

def p_valor(p):
    '''valor : INT
            | FLOAT
            | VARIABLE
            | STRING
            | BOOL
            | NULL
            | ARRAY
            '''

def p_operador(p):
    '''operador : PLUS
                | MINUS
                | TIMES
                | DIVIDE
                | MODULO'''

def p_comparacion(p):
    '''comparacion : valor comparador valor'''

def p_comparador(p):
    '''comparador : LT
                | GT
                | LEQ
                | GEQ'''

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
                        | switch'''

def p_if(p):
    '''if : IF LPAREN conditions RPAREN LBRACE body RBRACE
         | IF LPAREN conditions RPAREN LBRACE body RBRACE else_blocks
         | IF LPAREN conditions RPAREN body
         '''

def p_else_blocks(p):
    '''else_blocks : ELSE LBRACE body RBRACE
                   | ELSE COLON body
                   | ELSEIF LPAREN conditions RPAREN LBRACE body RBRACE else_blocks
                   | ELSEIF LPAREN conditions RPAREN COLON body else_blocks'''


def p_conditions(p):
    '''conditions : LPAREN condition RPAREN
                | condition opLogic conditions
                | unaryLogic condition
                | condition'''

def p_condition(p):
    '''condition : valor
                 | valor opSymbol valor
                 | operaArit opSymbol operaArit'''

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
                | LOGICAL_OR'''
def p_unaryLogic(p):
    '''unaryLogic : NOT
                  | LOGICAL_NOT'''
def p_body(p):
     '''body : sentenciaList
            | sentencia
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

def foreach(p):
    '''foreach'''

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
    '''argumento : VARIABLE
                 | type VARIABLE
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
    '''objeto : '''

def p_funcionDeclaration(p):
    '''funcionDeclaration : FUNCTION ID LPAREN argumentos RPAREN LBRACE body RBRACE''' 
def p_llamadaFuncion(p):
    '''llamadaFuncion : ID LPAREN argumentos RPAREN SEMICOLON''' 
                      
# Función para manejar errores de sintaxis
def p_error(p):
    if p:
        # Reportar el error sintáctico, su valor y la línea
        error_msg = f"Error de sintaxis: '{p.value}' en la linea {p.lineno}"
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
