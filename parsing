import yacc
from lexing import tokens


def p_root(p):
	'''root : function NUMBER option
 			| COLOR colors option
    		| PEN NUMBER option '''
    
    
def p_option(p):
	'''option : root
 			  | LSQB root RSQB root
      		  | EMPTY '''
def p_function(p):
	'''function : FORW 
                | RGHT 
                | LOOP '''
	p[0]=p[1]
def p_colors(p):
	'''colors : RED 
              | BLUE 
              | GREEN 
              | BLACK ''' 
              
def p_error(p):
   print("Syntax error in input!")

from lexing import data

# Build the parser

parser=yacc.yacc()

result=parser.parse(data)

print (result)
