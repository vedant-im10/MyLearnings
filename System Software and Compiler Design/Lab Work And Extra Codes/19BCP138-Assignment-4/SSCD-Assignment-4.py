# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 22:11:43 2021

@author: vedpa
"""

import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'INT',
    'FLOAT',
    'NAME',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'POWER',
    'LPAREN',
    'RPAREN',
    'EQUALS'
    )
 

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_POWER  = r'\^'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_EQUALS = r'\=' 


def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)    
    return t

def t_INT(t):
    r'\d[0-9]*'
    t.value = int(t.value)    
    return t

def t_NAME(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = 'NAME'    
    return t
 
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'
 
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
 
lexer = lex.lex()
 
def p_calc(p):
    '''
    calc : expression 
    | var_assign
    | empty
    '''
    print(p[1])
    print(run(p[1]))

def p_expression_int_float(p):
    '''
    expression : INT
    | FLOAT
    '''
    p[0]=p[1]

def p_expression_var(p):
    '''
    expression : NAME
    
    '''
    p[0]=('var', p[1])

def p_expression(p):
    '''
    expression : expression TIMES expression 
                | expression POWER expression
                | expression DIVIDE expression
                | expression PLUS expression
                | expression MINUS expression
    '''
    p[0]= (p[2], p[1],p[3])

def p_var_assign(p):
    '''
    var_assign : NAME EQUALS expression
               '''
    p[0]= ('=', p[1],p[3]) 

def p_empty(p):
    '''
    empty :
    '''
    p[0]= None


precedence= (('left','PLUS','MINUS'),
             ('left','TIMES','DIVIDE'),
             ('right','POWER'))

def p_error(p):
    print("Syntax error found")
    
def run(p):
    if type(p) == tuple:
        if p[0] == '+':
            return run(p[1]) + run(p[2])
        elif p[0] == '-':
            return run(p[1]) - run(p[2])
        elif p[0] == '*':
            return run(p[1]) * run(p[2])
        elif p[0] == '/':
            return run(p[1]) / run(p[2])
        elif p[0] == '^':
            return run(p[1]) ** run(p[2])
    else:
        return p

parser=yacc.yacc()

while True:
    try:
        s=input('Enter string: ')
    except EOFError:
        break
    parser.parse(s)