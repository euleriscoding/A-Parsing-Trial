import yacc
from lexing import tokens
import turtle

pattern = turtle.Turtle()   
#PARSER
import yacc

########################## ABSTARCT SYNTAX TREE #########################################
class Expr:
    pass
# class Node:
#      def __init__(self,type,children=None,leaf=None):
#           self.type = type
#           if children:
#                self.children = children
#           else:
#                self.children = [ ]
#           self.leaf = leaf

def forw(num1):
    pattern.forward(num1)
def right(num2):
    pattern.right(num2)
    
class Loop(Expr):
    def __init__(self, stmt):
        self.stmt=stmt
        
def pensize(num4):
    if num4 == 1:
        pattern.pensize(1)
    elif num4 == 2:
        pattern.pensize(3)
    elif num4 == 3:
       pattern.pensize(5)

precedence = (
     ('left', 'FORW', 'RIGHT'),
     ('left', 'COLOR', 'PEN'),
 )
 
########################################### PARSER ##############################################
def p_start(p):
    '''start : function 
             | function option 
             | errormessage'''
    if len(p)==2:
        p[0]=p[1]
    elif len(p)==3:
        p[0]= (p[1],p[2])

def p_function(p):
    '''
    function : forward
             | right
             | loop
             | color
             | pen
    '''
    p[0]=p[1] 

def p_empty(p):
    'empty :'
    pass
 
def p_option(p):
    '''option : start
              | empty '''
    p[0]=p[1]
    

def p_forward(p):
    'forward : FORW NUMBER' 
    p[0]= forw(p[2])
    
 
def p_right(p):
    'right : RIGHT NUMBER'
    p[0]= right(p[2])
    

def p_loop(p):
    'loop : LOOP NUMBER LSQB start RSQB '
    p[0]= Loop(p[4])
    i=1
    while i<=p[2]:
        p_start('start')
        i+=1

    

def p_color(p):
    'color : COLOR colors'
    p[0]=Color(p[1],p[2])
    
def p_colors(p):
    '''colors : BLACK 
              | BLUE
              | GREEN
              | RED '''
    if p[1] == 'S':
        p[0]=pattern.color("black")
    elif p[1] == 'M':
        p[0]=pattern.color("blue")
    elif p[1] == 'Y':
        p[0]=pattern.color("green")
    elif p[1] == 'K':
        p[0]=pattern.color("red")
   

def p_pen(p):
    'pen : PEN NUMBER'
    p[0]=pensize(p[2])
    
################################# ERROR #################################

def p_error(p):
    print("error: invalid syntax ")
    
def p_WrongCommandError(p):
    '''errormessage : FORW RED option
                    | FORW BLUE option
                    | FORW BLACK option
                    | FORW GREEN option
                    | RIGHT RED option
                    | RIGHT BLUE option
                    | RIGHT BLACK option
                    | RIGHT GREEN option
                    | PEN RED option
                    | PEN BLUE option
                    | PEN BLACK option
                    | PEN GREEN option
                    | COLOR NUMBER option'''
    if p[1]=='F':
        print("error: incorrect value after F command")
    elif p[1]=='R':
        print("error: incorrect value after R command")
    elif p[1]=='PEN':
        print("error: incorrect value after PEN command")
    elif p[1]=='COLOR':
        print("error: incorrect value after COLOR command")

def p_MissingValueError(p):
    '''errormessage : FORW empty option
                    | RIGHT empty option
                    | COLOR empty option
                    | PEN empty option '''
             
    if p[1] == 'F':
        print("error : missing value after F command")
    elif p[1] == 'R':
        print("error : missing value after R command")
    elif p[1] == 'COLOR':
        print("error : missing value after COLOR command")
    elif p[1] == 'PEN':
        print("error : missing value after PEN command")
        
def p_MissingCommandError(p):
    '''errormessage : option empty NUMBER option
                    | option empty RED option 
                    | option empty BLUE option 
                    | option empty GREEN option 
                    | option empty BLACK option '''
    if p[3] == 'K':
        print("error : missing command before '%s'" % (p[3]))
    elif p[3] == 'M':
        print("error : missing command before '%s'" % (p[3]))
    elif p[3] == 'Y':
        print("error : missing command before '%s'" % (p[3]))
    elif p[3] == 'S':
        print("error : missing command before '%s'" % (p[3]))
    else:
        print("error : missing command before '%s'" % (p[3]))

from lexing import data

# Build the parser

parser=yacc.yacc()

result=parser.parse(data)
turtle.done()
#print (result)
