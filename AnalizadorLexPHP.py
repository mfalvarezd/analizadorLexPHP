#Estudiante 1: Jair Alexander Chaguay
#Matrícula 1: 202112082

#Estudiante 2: Moisés Fernando Alvarez
#Matrícula 2: 202005526

#Estudiante 3: Piero Valentino Pazmiñp
#Matrícula 3:202204053
import logging
import os
import time
import re
import ply.lex as lex

##Analizador Lexico PHP

#Reserved
reserved={
#Inicio contribuciones Jair
    'abstract':'ABSTRACT',
    'and': 'AND',
    'array':'ARRAY',
    'as':'AS',
    'break': 'BREAK',
    'case': 'CASE',
    'catch':'CATCH',
    'class': 'CLASS',
    'const':'CONST',
    'default':'DEFAULT',
    'do': 'DO',
    'echo':'ECHO',
    'else': 'ELSE',
    'elseif': 'ELSEIF',
    'empty':'EMPTY',
    'endswitch':'ENDSWITCH',
    'extends': 'EXTENDS',
    'exception':'EXCEPTION',
#inicio contribuciones Fernando
    'finally': 'FINALLY',
    'for': 'FOR',
    'foreach':'FOREACH',
    'fn': 'FN',
    'function':'FUNCTION',
    'if':'IF',
    'implements': 'IMPLEMENTS',
    'include':'INCLUDE',
    'instanceof':'INSTANCEOF',
    'interface': 'INTERFACE',
    'namespace':'NAMESPACE',
    'new':'NEW',
    'not': 'NOT',
    'or': 'OR',
    'print':'PRINT',
#inicio contribuciones Piero
    'private': 'PRIVATE',
    'protected':'PROTECTED',
    'public':'PUBLIC',
    'return':'RETURN',
    'static': 'STATIC',
    'switch': 'SWITCH',
    'this':'THIS',
    'throw':'THROW',
    'try':'TRY',
    'while': 'WHILE',
    'final':'FINAL',
    'void' : 'VOID',
    'null' :'NULL'
}

#List of token names
tokens=(
    'ARROW',
    'ARROWMAP',
    'INT',
    'FLOAT',
    'STRING',
    'BOOL',
    'PLUS',
    'DOUBLEPLUS',
    'DOUBLEMINUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'VARIABLE',
    'EQUALS',
    'COMMA',
    'SEMICOLON',
    'DOT',
    'ID',
    'LT',
    'GT',
    'OPENTAG',
    'POTENCIA',
    'PLUSEQUAL',
    'CONCATENATEEQUAL',
    'STRICTEQ',
    'STRICTNEQ',
    'CLOSETAG',
    'MINUSEQUAL',
    'EQ',
    'NEQ',
    'LEQ',
    'GEQ',
    'MODULO',
    'DOUBLEDOT',
    'FGETS',
    'STDIN',
    'QUESTION',
    'COLON',
     'LOGICAL_AND',
       'LOGICAL_OR',
       'LOGICAL_NOT'
)+ tuple(reserved.values())

#REGULAR EXPRESSIONS
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_EQUALS = r'='
t_SEMICOLON = r';'
t_COMMA = r','
t_DOT = r'\.'
t_MODULO = r'%'
t_POTENCIA = r'\*\*'
t_PLUSEQUAL = r'\+='
t_MINUSEQUAL = r'-='
t_CONCATENATEEQUAL = r'\.='
t_LOGICAL_AND = r'&&'
t_LOGICAL_OR = r'\|\|'
t_LOGICAL_NOT = r'!'
t_EQ = r'=='
t_STRICTEQ = r'==='
t_NEQ = r'!='
t_STRICTNEQ = r'!=='
t_LT = r'<'
t_GT = r'>'
t_LEQ = r'<='
t_GEQ = r'>='
t_OPENTAG = r'<\?php'
t_CLOSETAG = r'\?>'
t_ARROW = r'\->'
t_ARROWMAP=r'\=>'
t_DOUBLEDOT= r'\:'
t_FGETS=r'fgets'
t_STDIN=r'STDIN'
t_DOUBLEPLUS=r'\+\+'
t_DOUBLEMINUS=r'--'
t_QUESTION = r'\?'
t_COLON = r':'



##MOISES ALVAREZ

def t_NULL(t):
    r'null'  # Detecta la palabra null
    t.type = 'NULL'
    return t
def t_BOOL(t):
    r'\b(true|false)\b'
    t.value = t.value.lower() == 'true'
    t.type = 'BOOL'
    return t
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value.lower(), 'ID')
    return t

def t_STRING(t):
    r'\"([^\\\"]|\\.)*\"|\'([^\\\']|\\.)*\''
    t.value = t.value[1:-1]
    return t

def t_VARIABLE(t):
    r'\$[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t


##detecta solo palabras reservadas

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}' en la línea {t.lineno}, columna {t.lexpos}")
    t.lexer.skip(1)


def t_COMMENT(t):
    r'//.*'
    pass  # No incrementar línea

def t_MCOMMENT(t):
    r'/\*[\s\S]*?\*/'
    t.lexer.lineno += t.value.count('\n')  # Incrementa líneas correctamente



lexer = lex.lex()

# Test it out
data = '''
$a = true;
$b = True;
$c = TRUE;
break
Break
BREAK

'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)

'''# Definir las rutas del directorio actual
current_directory = os.path.dirname(os.path.abspath(__file__))

# Definir las carpetas "algoritmos" y "logs"
algoritmos_directory = os.path.join(current_directory, "algoritmos")
logs_directory = os.path.join(current_directory, "logs")

# Crear las carpetas si no existen
os.makedirs(algoritmos_directory, exist_ok=True)
os.makedirs(logs_directory, exist_ok=True)

# Preguntar al usuario qué tipo de análisis realizar
tipo_analisis = input("¿Desea realizar un análisis léxico o sintáctico? (l/s): ").strip().lower()
usuario_git = input("Ingrese su usuario de Git: ")
archivo_numero = input("Ingrese el número del archivo a analizar (por ejemplo, '1' para algoritmo1.php): ")

# Crear logs en el formato requerido
fecha_hora = time.strftime("%d%m%Y-%Hh%M")
log_filename = f"{tipo_analisis}-{usuario_git}-{fecha_hora}.txt"
log_filepath = os.path.join(logs_directory, log_filename)

# Procesar el archivo
algoritmo_filename = f"algoritmo{archivo_numero}.php"
algoritmo_filepath = os.path.join(algoritmos_directory, algoritmo_filename)

try:
    with open(algoritmo_filepath, "r") as file:
        data = file.read()
except FileNotFoundError:
    print(f"El archivo {algoritmo_filename} no se encontró en la carpeta 'algoritmos'.")
    exit(1)

# Ejecutar el análisis según la opción seleccionada
with open(log_filepath, "w") as log_file:
    if tipo_analisis == 'l':
        lexer.input(data)
        while True:
            tok = lexer.token()
            if not tok:
                break
            log_file.write(f"Token: {tok.type}, Valor: {tok.value}, Línea: {tok.lineno}\n")
        print(f"El análisis léxico se completó y el log se guardó en: {log_filepath}")
    elif tipo_analisis == 's':
        if result is None:
            log_file.write("No se encontraron errores sintácticos.\n")
        else:
            log_file.write(f"Errores sintácticos encontrados: {result}\n")
        print(f"El análisis sintáctico se completó y el log se guardó en: {log_filepath}")
    else:
        print("Opción inválida. Por favor elija 'l' o 's'.")'''


