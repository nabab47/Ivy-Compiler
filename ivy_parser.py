"""
***!!PLEASE READ!!***
---------------------------------------------------------
This file is ugly and complicated. To get a better idea
of the actual grammar, see the ivy-grammar.pdf file in the 
repository. As far as what is happening in this file:


****************************
All the description below is still under development. Right
now basic parsing is the only functionality. But read below 
for the plan!
****************************

TL;DR -> We create a Node object for each production rule
that will be used later in a syntax tree.

TL;WILL STILL READ ANYWAY :) -> There is a separate Node 
class created (see node.py) which will be the individual 
nodes in our syntax tree. Each node consists of the 
following:
-> production rule type (typically the left hand side of 
the rule)
-> the child nodes and elements (in the case of terminal 
symbols - these are the things our lexer matched) associated
with the production rule
-> a boolean indicating whether the node is a leaf or not. 
This is one of those things that the lexer matched.
-> the value of the node. This only applies to expressions.
This will be utilized when we evaluate nodes later on.
"""

def p_program(p):
    'program : statements'
    p[0] = p[1]

def p_statements(p):
    '''statements   : statements statement 
                    | statement'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        """
        This is a weird case where the last statement
        will be in it's own sublist because when there are 
        N statements, N-1 of them match `statements` and the 
        last statement matches `statement`. This is just a way 
        to flatten the overall array.
        """
        tmp = p[1]
        tmp.append(p[2])
        p[0] = tmp

def p_statement(p):
    '''statement    : assignment SEMIC
                    | print_st SEMIC
                    | cond_block'''
    p[0] = p[1]

def p_assignement(p):
    '''assignment : ID EQ exprs'''
    p[0] = [p[1],p[2],p[3]]
    
def p_exprs(p):
    '''exprs    : exprs expr
                | expr'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        """
        See the note on statements above 
        to understand this bit.
        """
        tmp = p[1]
        tmp.append(p[2])
        p[0] = tmp

def p_expr(p):
    '''expr : add_expr
            | sub_expr
            | term'''
    p[0] = p[1]

def p_add_expr(p):
    '''add_expr : expr ADD term'''
    p[0] = [p[1],p[2],p[3]]

def p_sub_expr(p):
    '''sub_expr : expr SUB term'''
    p[0] = [p[1],p[2],p[3]]

def p_term(p):
    '''term : ID
            | NUM'''
    p[0] = p[1]

def p_cond_block(p):
    '''cond_block : IF OPAREN term COMP term CPAREN body ELSE body'''
    p[0] = [p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9]]

def p_body(p):
    '''body : OCB statements CCB'''
    p[0] = p[2]

def p_print(p):
    '''print_st : PRINT ID'''
    p[0] = [p[1],p[2]]

def p_error(p):
    print("Syntax Error. %s" % p)

