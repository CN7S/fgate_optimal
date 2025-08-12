#!/usr/bin/env python3

from . import saiflex
from . import saifyacc


def init():
    saifyacc.saif_file = dict()

    saifyacc.header = dict()

    saiflex.lexer.lineno = 1

def parse(input):
    init()
    saiflex.input_data = input
    saifyacc.parser.parse(saiflex.input_data, lexer = saiflex.lexer)
    return saifyacc.saif_file
