#!/usr/bin/env python3

import ply.lex as lex

input_data = ""

reserved = {
    "module" : "MODULE",
    "endmodule" : "ENDMODULE",
    "wire" : "WIRE",
    "assign" : "ASSIGN",
    "input" : "INPUT",
    "output" : "OUTPUT"
}

tokens = (
    'LPAR',
    'RPAR',
    'LBRA',
    'RBRA',
    'EQUAL',
    'COLON',
    'DOT',
    'COMMA',
    'SEMICOLON',
    'STRING',
    #'SSTRING',
    'NUMBER',
) + tuple(reserved.values())

t_LPAR = r'\('
t_RPAR = r'\)'
t_LBRA = r'\['
t_RBRA = r'\]'
t_EQUAL = r'='
t_COLON = r':'
t_SEMICOLON = r';'
t_DOT = r'\.'
t_COMMA = r','

# t_QSTRING = r'\"[a-zA-Z0-9_!#$%&\'()*+,\-./:;<=>?@\[\\\]^`{|}~ \t\n]+\"'



t_ignore = ' \t'


def t_NUMBER(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t


def t_STRING(t):
    # r'[a-zA-Z0-9_\/.\[\]\\]+'
    r'[a-zA-Z0-9_]+'
    t.type = reserved.get(t.value, 'STRING')
    return t

def t_SSTRING(t):
    # r'[a-zA-Z0-9_\/.\[\]\\]+'
    r'\\[a-zA-Z0-9_\/.\[\]\\]+'
    t.type = reserved.get(t.value, 'STRING')
    return t

def t_COMMEND(t):
    # r'[a-zA-Z0-9_\/.\[\]\\]+'
    r'\/\/[a-zA-Z0-9_!#$%&\'()*+,\-./:;<=>?@\[\\\]^`{|}~ \t]*'
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    raise Exception("Illegal character '%s' in line %d, column %d"
                    % (t.value[0], t.lineno, find_column(input_data, t)))

# Compute column.
# input is the input text string
# token is a token instance


def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


lexer = lex.lex()

if __name__ == '__main__':
    with open('test.v') as file:
        input_data = file.read()
    lexer.input(input_data)
    with open("test.o", 'w') as file:
        for tok in lexer :
            file.write(f'{tok.type} ')
            
