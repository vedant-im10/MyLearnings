# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 09:15:37 2021

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
data = '2 + 3 + 4 + 5 + 6'

lexer.input(data)
count = 0
while(True):
    tok = lexer.token()
    count = count + 1
    if not tok: break
    print(tok)
print("Number of tokens:", count-1)