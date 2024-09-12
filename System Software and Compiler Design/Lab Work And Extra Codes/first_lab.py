# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 14:43:36 2021

@author: vedpa
"""

import ply.lex as lex
tokens = (
    'INT',
    'FLOAT',
    'PLUS',
    'MINUS',
    'LPAREN',
    'RPAREN'
    )

t_PLUS = r'\+'
t_MINUS = r'-'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += lex(t.value)
    
t_ignore = ' \t'

def t_error(t):
    print("Illegal Character %s"%t.value[0])
    t.lexer.skip(1)
    
lexer = lex.lex()
data = '3 + 4 -35'

lexer.input(data)
while(True):
    tok = lexer.token()
    if not tok: break
    print(tok)