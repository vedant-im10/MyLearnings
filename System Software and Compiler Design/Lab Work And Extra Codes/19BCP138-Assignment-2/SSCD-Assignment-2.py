# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 09:16:36 2021

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
    'SEMICOLON',
    'SCOMMENT',
    'DCOMMENT'
    )

t_PLUS = r'\+'
t_MINUS = r'-'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r'\,'
t_SEMICOLON = r'\;'

def t_SCOMMENT(t):
    r'\#.*'
    print("Single-Line Comment %s" %t.value)
    t.lexer.skip(1)

def t_DCOMMENT(t):
    r'""".*"""'
    print("Double-Line Comment %s" %t.value)
    t.lexer.skip(1)

def t_QUOTES(t):
    r'".*"'
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
data = ' """ 3 + 5 + 5 + 5 """ 5+5  #vedant' 

lexer.input(data)
count = 0
while True:
    tok = lexer.token()
    count = count + 1
    if not tok: break
    print(tok)
print("Number of tokens", count-1)