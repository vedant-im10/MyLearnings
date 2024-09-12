# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 14:05:36 2021

@author: vedpa
"""

import ply.lex as lex

tokens = (
    'INT',
    'FLOAT',
    'PLUS',
    'MINUS',
    'LPAREN',
    'RPAREN',
    'NAME',
    'INAME',
    'QUOTES',
    'COMMA',
    'SEMICOLON'
    )

t_PLUS = r'\+'
t_MINUS = r'-'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r'\,'
t_SEMICOLON = r'\;'


def t_QUOTES(t):
    r'".*"'               #Can write the ? too, r'".*?"' only
    t.type = 'QUOTES'
    return t

def t_INAME(t):
    r'[0-9]+[a-zA-Z]+[0-9]*'
    print("Invalid Token %s" %t.value)
    t.lexer.skip(1)

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
     r'\d+'
     t.value = int(t.value)
     return t


def t_NAME(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type ='NAME'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'


def t_error(t):
    print("Illegal character %s"%t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
data = 'print("Number of tokens %d=", x)' 
#Write to read whole program not just a single line.
lexer.input(data)
count = 0
while True:
    tok = lexer.token()
    count = count + 1
    if not tok: break
    print(tok)
print("Number of tokens", count-1)