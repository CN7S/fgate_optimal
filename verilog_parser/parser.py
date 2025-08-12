#!/usr/bin/env python3

from . import vlex
from . import vyacc


def init():
    vyacc.module_list = []

    vlex.lexer.lineno = 1

def parse(input):
    init()
    vlex.input_data = input
    vyacc.parser.parse(vlex.input_data)
    return vyacc.module_list
