
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDErightPOWERDIVIDE EQUALS FLOAT INT LPAREN MINUS NAME PLUS POWER RPAREN TIMES\n    calc : expression \n    | var_assign\n    | empty\n    \n    expression : INT\n    | FLOAT\n    \n    expression : NAME\n    \n    \n    expression : expression TIMES expression \n                | expression POWER expression\n                | expression DIVIDE expression\n                | expression PLUS expression\n                | expression MINUS expression\n    \n    var_assign : NAME EQUALS expression\n               \n    empty :\n    '
    
_lr_action_items = {'INT':([0,8,9,10,11,12,13,],[5,5,5,5,5,5,5,]),'FLOAT':([0,8,9,10,11,12,13,],[6,6,6,6,6,6,6,]),'NAME':([0,8,9,10,11,12,13,],[7,15,15,15,15,15,15,]),'$end':([0,1,2,3,4,5,6,7,14,15,16,17,18,19,20,],[-13,0,-1,-2,-3,-4,-5,-6,-7,-6,-8,-9,-10,-11,-12,]),'TIMES':([2,5,6,7,14,15,16,17,18,19,20,],[8,-4,-5,-6,-7,-6,-8,-9,8,8,8,]),'POWER':([2,5,6,7,14,15,16,17,18,19,20,],[9,-4,-5,-6,9,-6,9,9,9,9,9,]),'DIVIDE':([2,5,6,7,14,15,16,17,18,19,20,],[10,-4,-5,-6,-7,-6,-8,-9,10,10,10,]),'PLUS':([2,5,6,7,14,15,16,17,18,19,20,],[11,-4,-5,-6,-7,-6,-8,-9,-10,-11,11,]),'MINUS':([2,5,6,7,14,15,16,17,18,19,20,],[12,-4,-5,-6,-7,-6,-8,-9,-10,-11,12,]),'EQUALS':([7,],[13,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'calc':([0,],[1,]),'expression':([0,8,9,10,11,12,13,],[2,14,16,17,18,19,20,]),'var_assign':([0,],[3,]),'empty':([0,],[4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> calc","S'",1,None,None,None),
  ('calc -> expression','calc',1,'p_calc','SSCD-Assignment-4.py',65),
  ('calc -> var_assign','calc',1,'p_calc','SSCD-Assignment-4.py',66),
  ('calc -> empty','calc',1,'p_calc','SSCD-Assignment-4.py',67),
  ('expression -> INT','expression',1,'p_expression_int_float','SSCD-Assignment-4.py',74),
  ('expression -> FLOAT','expression',1,'p_expression_int_float','SSCD-Assignment-4.py',75),
  ('expression -> NAME','expression',1,'p_expression_var','SSCD-Assignment-4.py',81),
  ('expression -> expression TIMES expression','expression',3,'p_expression','SSCD-Assignment-4.py',88),
  ('expression -> expression POWER expression','expression',3,'p_expression','SSCD-Assignment-4.py',89),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','SSCD-Assignment-4.py',90),
  ('expression -> expression PLUS expression','expression',3,'p_expression','SSCD-Assignment-4.py',91),
  ('expression -> expression MINUS expression','expression',3,'p_expression','SSCD-Assignment-4.py',92),
  ('var_assign -> NAME EQUALS expression','var_assign',3,'p_var_assign','SSCD-Assignment-4.py',98),
  ('empty -> <empty>','empty',0,'p_empty','SSCD-Assignment-4.py',104),
]
