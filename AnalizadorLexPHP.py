#Estudiante 1: Jair Alexander Chaguay
#Matrícula 1: 202112082

#Estudiante 2: Moisés Fernando Alvarez
#Matrícula 2: 202005526

#Estudiante 3: Piero Valentino Pazmiñp
#Matrícula 3:202204053

import ply.lex as lex

##Analizador Lexico PHP

#Reserved
reserved={
#Inicio contribuciones Jair
    'stdin':'STDIN',
    'fgets':'FGETS',
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
    'null' :'NULL',
    'int':'INT_TYPE',
    'float':'FLOAT_TYPE',
    'string':'STRING_TYPE',
    'boolean': 'BOOL_TYPE',
    'object': 'OBJECT_TYPE',

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
    'COLON',
    'LOGICAL_AND',
    'LOGICAL_OR',
    'ARRAY_TYPE',
    'NOT'

    
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
t_ARROW = r'\->'
t_ARROWMAP=r'\=>'
t_DOUBLEPLUS=r'\+\+'
t_DOUBLEMINUS=r'--'
t_COLON = r'\:'



##MOISES ALVAREZ


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


echo ($v) ? 'xd': 'No Value';
 

'''
def getListaTokens(lexer,lista):
    while True:
        tok =  lexer.token()
        if not tok:
            break
        lista.append(tok)
def getAnalizadorLexico():
    return lex.lex()

