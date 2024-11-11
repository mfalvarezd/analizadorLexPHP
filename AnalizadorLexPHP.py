import logging

import ply.lex as lex

##Analizador Lexico PHP

#Reserved
reserved={
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
    'false':'FALSE',
    'finally': 'FINALLY',
    'for': 'FOR',
    'foreach':'FOREACH',
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
}

#List of token names
tokens=(
    'INT',
    'FLOAT',
    'STRING',
    'BOOL',
    'PLUS',
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
    'MODULO'
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

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
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
