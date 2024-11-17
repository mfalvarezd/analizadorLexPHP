#Estudiante 1: Jair Alexander Chaguay
#Matrícula 1: 202112082

#Estudiante 2: Moisés Fernando Alvarez
#Matrícula 2: 202005526

#Estudiante 3: Piero Valentino Pazmiñp
#Matrícula 3:202204053
import logging
import os
import time

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
    'clone':'CLONE',
    'continue': 'CONTINUE',
    'const':'CONST',
    'declare':'DECLARE',
    'default':'DEFAULT',
    'do': 'DO',
    'echo':'ECHO',
    'else': 'ELSE',
    'elseif': 'ELSEIF',
    'empty':'EMPTY',
    'endswitch':'ENDSWITCH',
    'extends': 'EXTENDS',
    'exception':'EXCEPTION',
    'false':'FALSE',
#inicio contribuciones Fernando
    'finally': 'FINALLY',
    'for': 'FOR',
    'foreach':'FOREACH',
    'fn': 'FN',
    'function':'FUNCTION',
    'global':'GLOBAL',
    'if':'IF',
    'implements': 'IMPLEMENTS',
    'include':'INCLUDE',
    'instanceof':'INSTANCEOF',
    'interface': 'INTERFACE',
    'isset':'ISSET',
    'list':'LIST',
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
    'true':'TRUE',
    'try':'TRY',
    'while': 'WHILE',
    'final':'FINAL',
    'include':'INCLUDE',
    'interface':'INTERFACE',
    'int': 'INTEGER',
    'float': 'FLOATING',
    'string': 'STRINGS',
    'bool':'BOOLEAN',
    'void' : 'VOID'
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
    'STDIN'
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
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
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
_ARROW = r'\->'
t_ARROWMAP=r'\=>'
t_DOUBLEDOT= r'\:'
t_FGETS=r'\fgets'
t_STDIN=r'\STDIN',
t_DOUBLEPLUS=r'\+\+'
t_DOUBLEMINUS=r'--'



##MOISES ALVAREZ
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
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

def t_BOOL(t):
    r'true|false'
    t.value = True if t.value == 'true' else False
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
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_COMMENT(t):
    r'//.*'
    pass  # Ignorar comentarios de una línea

def t_MCOMMENT(t):
    r'/\*[\s\S]*?\*/'
    pass  # Ignorar comentarios de múltiples líneas


lexer = lex.lex()

# Test it out
data = '''
    $variable = 10 + 20.5;
    $booleano = true;
    array
    switch
    for
    if
    while
    $if = "String"
    $string1 = "Hello\\nWorld!";
    $string2 = 'This is a \\ttab.';
    $escaped = "She said, \\"Hello!\\"";
    $newLine = "First Line\nSecond Line";
    4 >=5
    5> 2
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)

# Solicitar el usuario de Git y el número del archivo a analizar
usuario_git = input("Ingrese su usuario de Git: ")
archivo_numero = input("Ingrese el número del archivo a analizar (por ejemplo, '1' para algoritmo1.php): ")

# Obtener la ruta del directorio actual donde se encuentra "lexico.py"
current_directory = os.path.dirname(os.path.abspath(__file__))

# Definir las rutas para las carpetas "algoritmos" y "logs" en el mismo nivel que "lexico.py"
algoritmos_directory = os.path.join(current_directory, "algoritmos")
logs_directory = os.path.join(current_directory, "logs")

# Crear las carpetas "algoritmos" y "logs" si no existen
os.makedirs(algoritmos_directory, exist_ok=True)
os.makedirs(logs_directory, exist_ok=True)

# Nombre del archivo log según el formato
fecha_hora = time.strftime("%d%m%Y-%Hh%M")
log_filename = f"lexico-{usuario_git}-{fecha_hora}.txt"

# Ruta del archivo de prueba en la carpeta "algoritmos"
algoritmo_filename = f"algoritmo{archivo_numero}.php"
algoritmo_filepath = os.path.join(algoritmos_directory, algoritmo_filename)

# Ruta completa para el archivo de log en la carpeta "logs"
log_filepath = os.path.join(logs_directory, log_filename)

# Inicializar el lexer y el almacenamiento de errores
lexer = lex.lex()
lexer.errors = []

# Procesa el archivo de prueba
try:
    with open(algoritmo_filepath, "r") as file:
        data = file.read()
except FileNotFoundError:
    print(f"El archivo {algoritmo_filename} no se encontró en la carpeta 'algoritmos'.")
    exit(1)

# Genera el log en la carpeta "logs"
with open(log_filepath, "w") as log_file:
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        log_file.write(f"Token: {tok.type}, Valor: {tok.value}, Linea: {tok.lineno}\n")

    # Si hay errores, escríbelos en el log
    if lexer.errors:
        for error in lexer.errors:
            log_file.write(f"Error: {error}\n")

print(f"El análisis léxico se completó y el log se guardó en: {log_filepath}")

