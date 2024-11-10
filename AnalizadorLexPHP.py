import logging

import ply.lex as lex
##Analizador Lexico PHP

#List of token names
lexLog = logging.getLogger('lexical')
illegal=[]

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
    'VARIABLE',

)

reserved={
    #Constantes en tiempo de ejecución
    '__class__': '__CLASS__',
    '__dir__': '__DIR__',
    '__file__': '__FILE__',
    '__function__': '__FUNCTION__',
    '__line__': '__LINE__',
    '__method__': '__METHOD__',
    '__namespace__': '__NAMESPACE__',
    '__trait__': '__TRAIT__',
    #Palabras Reservadas
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
}
tokens= tokens + tuple(reserved.values())

