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
    'ARRAY',
)

reserved={
    'abstract':'ABSTRACT',
    'and': 'AND',
    'break': 'BREAK',
    'case': 'CASE',
    'class': 'CLASS',
    'clone':'CLONE',
    'continue': 'CONTINUE',
    'default':'DEFAULT',
    'do': 'DO',
    'echo':'ECHO',
    'else': 'ELSE',
    'elseif': 'ELSEIF',
    'extends': 'EXTENDS',
    'false':'FALSE',
    'final': 'FINAL',
    'for': 'FOR',
    'function':'FUNCTION',
    'global':'GLOBAL',
    'if':'IF',
    'implements': 'IMPLEMENTS',
    'include':'INCLUDE',
    'instanceof':'INSTANCEOF',
    'interface': 'INTERFACE',
    'namespace':'NAMESPACE',
    'new':'NEW',
    'not': 'NOT',
    'or': 'OR',
    'private': 'PRIVATE',
    'public':'PUBLIC',
    'return':'RETURN',
    'static': 'STATIC',
    'switch': 'SWITCH',
    'this':'THIS',
    'throw':'THROW',
    'true':'TRUE',
    'while': 'WHILE',


}
tokens= tokens + tuple(reserved.values())