#!/usr/bin/env python3

import ply.lex as lex

input_data = ""

reserved = {
    'SAIFILE' : 'SAIFILE',
    'SAIFVERSION' : 'SAIFVERSION',
    'DIRECTION' : 'DIRECTION',
    'DESIGN' : 'DESIGN',
    'DATE' : 'DATE',
    'VENDOR' : 'VENDOR',
    'PROGRAM_NAME' : 'PROGRAM_NAME',
    'VERSION' : 'VERSION',
    'DIVIDER' : 'DIVIDER',
    'TIMESCALE' : 'TIMESCALE',
    'DURATION' : 'DURATION',
    'INSTANCE' : 'INSTANCE',
    'NET' : 'NET',
    'T0' : 'T0',
    'T1' : 'T1',
    'TX' : 'TX',
    'TC' : 'TC',
    'IG' : 'IG',
}

tokens = (
    'LPAR',
    'RPAR',
    'QSTRING',
    'STRING',
    'NUMBER',
) + tuple(reserved.values())

t_LPAR = r'\('
t_RPAR = r'\)'
t_QSTRING = r'\"[a-zA-Z0-9_!#$%&\'()*+,\-./:;<=>?@\[\\\]^`{|}~ \t\n]+\"'

t_ignore = ' \t'


def t_NUMBER(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t


def t_STRING(t):
    r'[a-zA-Z0-9_\/.\[\]\\]+'
    t.type = reserved.get(t.value, 'STRING')
    return t


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
