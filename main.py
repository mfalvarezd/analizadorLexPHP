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
                | comparacion
                | impresion'''

def p_asignacion(p):
    '''asignacion : VARIABLE EQUALS operaArit SEMICOLON'''

def p_operaArit(p):
    '''operaArit : valor
                | valor operador operaArit'''

def p_valor(p):
    '''valor : INT
            | FLOAT
            | VARIABLE
            | STRING'''

def p_operador(p):
    '''operador : PLUS
                | MINUS
                | TIMES
                | DIVIDE
                | MODULO'''

def p_comparacion(p):
    '''comparacion : INT comparador INT'''
    
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
