import lex
# List of token names
tokens = (
    'NUMBER',
    'RED',
    'GREEN',
    'BLUE',
    'BLACK',
    'FORW',
    'RIGHT',
    'LOOP',
    'COLOR',
    'PEN',
    'LSQB',
    'RSQB',
) 
# Regular expression rules for simple tokens
t_FORW    = r'F'
t_RIGHT   = r'R'
t_LOOP   = r'L'
t_COLOR  = r'COLOR'
t_PEN  = r'PEN'
t_LSQB  = r'\['
t_RSQB  = r'\]'
t_RED  = r'K'
t_GREEN  = r'Y'
t_BLUE  = r'M'
t_BLACK  = r'S'
 
# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t 
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value) 
# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t' 
# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1) 
# Build the lexer
lexer = lex.lex()
# Test it out
data = '''
F 50 R 90
''' 
# Give the lexer some input
lexer.input(data)
# Tokenize 
for tok in lexer:
    print(tok)



