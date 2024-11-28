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
    '''returnStatement : RETURN valor SEMICOLON
                       | RETURN SEMICOLON'''

def p_asignacion(p):
    '''asignacion : VARIABLE EQUALS operaArit SEMICOLON
                  | VARIABLE EQUALS valor SEMICOLON'''

def p_asignacion_fgets(p):
    '''asignacion_fgets : VARIABLE EQUALS FGETS LPAREN STDIN RPAREN SEMICOLON'''
    variable = p[1]  # Nombre de la variable
    print(f"Asigna a {variable} el valor ingresado por el usuario.")

def p_operador_ternario(p):
    '''operador_ternario : LPAREN conditions RPAREN QUESTION valor COLON valor
                        | LPAREN conditions RPAREN QUESTION COLON valor
                        '''

#Semántico 1
def p_operaArit(p):
    '''operaArit : valor
                | valor operador operaArit'''

def p_valor(p):
    '''valor : INT
            | VARIABLE
            | FLOAT
            | STRING
            | BOOL
            | NULL
            | ARRAY
            | llamadaFuncion
            | operador_ternario
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
                   | condition opLogic condition
                   | LPAREN conditions RPAREN'''

def p_condition(p):
     '''condition : valor
                  | valor opSymbol valor
                  | NOT condition'''

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
    '''statement_valor : VARIABLE EQUALS valor'''
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
