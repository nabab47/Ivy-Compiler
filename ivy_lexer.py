"""
The following words/tokens are reserved in the Ivy programming 
at this time.
"""
reserved_words = ["IF","ELSE","PRINT"]

"""
The following tokens are valid in the Ivy programming at this 
time. See below for the definitions of these tokens.
"""
tokens = (
    'NUM',
    'IF',
    'ELSE',
    'PRINT',
    'ADD',
    'SUB',
    'EQ',
    'COMP',
    'OPAREN',
    'CPAREN',
    'SEMIC',
    'OCB',
    'CCB',
    'ID'
)

"""
The following tokens are basic.
"""
t_ADD =     r'\+'
t_SUB =     r'-'
t_EQ =      r'='
t_COMP =    r'=='
t_OPAREN =  r'\('
t_CPAREN =  r'\)'
t_OCB =     r"\{"
t_CCB =     r"\}"
t_SEMIC =   r'\;'

"""
Defining a separate rule for periods because
we only use them for floating point numbers at
this point and don't need to keep them around;
this way, we can just skip them.
"""
def t_PER(t):
    r"\."
    t.lexer.skip(1)


"""
This regex encompasses integers (4, 21, 105, etc.)
as well as floating point numbers (4.5, 0.2, 13.44, 
etc.) In Ivy, all numeric values are automatically 
converted to floats. This may change as the language
evolves.
"""
def t_NUM(t):
    r'\d+\.\d+|\d+'
    t.value = float(t.value)
    return t

"""
New lines are not stored as tokens, but by capturing
them, we are able to increment the line number variable 
internal to PLY lex. Note that this rule will capture
multiple consecutive new lines and increment the line 
number appropriately.
"""
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

"""
Since we already matched new lines, we only need to match
spaces and tab characters here as far as whitespace goes.
"""
t_ignore = ' \t'

"""
Identifiers in the Ivy language must start with a letter, 
and can then include numbers, letters, or underscores. There
is also a check to see if the identifier found matches a 
keyword. This was much easier to implement than to differentiate 
between matching a keyword or identifier because the ID 
regex would match a keyword and capture it regardless of 
the order that the rules were placed in.
"""
def t_ID(t) :
    r'[a-zA-Z][a-zA-Z0-9_]{0,9}'
    if t.value in reserved_words:
        t.type = t.value
    return t

"""
PLY lex requires the `t_error` function be defined. My
custom code in the function gives the unrecognized character
as well the line number in which it occured. Currently we just
skip over this occurance, though in the future, we will terminate
compilation upon encountering a lexical error.
"""
def t_error(t):
    print("Lexical Error: Encountered unrecognized character `%s` on line %d. Compilation Terminated." % (t.value[0],t.lexer.lineno))
    t.lexer.skip(1)

