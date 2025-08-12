#!/usr/bin/env python3

import ply.yacc as yacc

from .saiflex import tokens

saif_file = dict()

header = dict()


def remove_quotation(s):
    return s.replace('"', '')


def p_saif_file(p):
    '''saif_file : LPAR SAIFILE saif_header RPAR
                | LPAR SAIFILE saif_header cell_list RPAR'''
    saif_file['header'] = p[3]
    if p[4] != ')':
        saif_file['cells'] = p[4]

    p[0] = saif_file


def p_saif_header(p):
    '''saif_header : saif_header_qstring
                  | saif_header saif_header_qstring
                  | saif_header divider
                  | saif_header timescale
                  | saif_header duration'''

    p[0] = p[1]


def p_saif_header_qstring(p):
    '''saif_header_qstring : LPAR qstring_header_entry QSTRING RPAR
                          | LPAR qstring_header_entry RPAR'''
    if len(p) == 5:
        header[p[2].lower()] = remove_quotation(p[3])
        p[0] = header


def p_qstring_header_entry(p):
    '''qstring_header_entry : SAIFVERSION
                            | DIRECTION
                            | DESIGN
                            | DATE
                            | VENDOR
                            | PROGRAM_NAME
                            | VERSION
                            | DIVIDER
                            | TIMESCALE
                            | DURATION'''
    p[0] = p[1]

def p_divider(p):
    '''divider : LPAR DIVIDER STRING RPAR'''
    header['divider'] = p[3]
    p[0] = header
def p_timescale(p):
    '''timescale : LPAR TIMESCALE NUMBER STRING RPAR'''
    header['timescale'] = p[3]
    p[0] = header
def p_duration(p) :
    '''duration : LPAR DURATION NUMBER RPAR'''
    header['duration'] = p[3]
    p[0] = header


def p_cell_list(p):
    '''cell_list : cell
                 | cell_list cell'''
    if len(p) == 2:
        cell_list = dict()
        cell_list[p[1]['name']] = p[1]
        p[0] = cell_list
    else:
        cell_list = p[1]
        cell_list[p[2]['name']] = p[2]
        p[0] = cell_list

def p_cell(p) :
    '''cell : LPAR INSTANCE STRING net cell_list RPAR
            | LPAR INSTANCE STRING net RPAR
            | LPAR INSTANCE STRING cell_list RPAR
            | LPAR INSTANCE STRING RPAR'''
    cell = dict()
    cell['name'] = p[3]
    if len(p) == 7:
        cell['cells'] = p[5]
        cell['net_list'] = p[4]
    elif len(p) == 6:
        first_value = next(iter(p[4].values()))
        if 't0' in first_value.keys():
            cell['net_list'] = p[4]
        else :
            cell['cells'] = p[4]
    p[0] = cell

def p_net(p):
    '''net : LPAR NET net_list RPAR'''
    p[0] = p[3]

def p_net_list(p) :
    '''net_list : single_net
                | net_list single_net'''
    if len(p) == 2:
        net_list = dict()
        net_list[p[1]['name']] = p[1]
        p[0] = net_list
    else:
        net_list = p[1]
        net_list[p[2]['name']] = p[2]
        p[0] = net_list


def p_single_net(p) :
    '''single_net : LPAR STRING t0 t1 tx tc ig RPAR'''
    single_net = dict()
    single_net['name'] = p[2]
    single_net['t0'] = p[3]
    single_net['t1'] = p[4]
    single_net['tx'] = p[5]
    single_net['tc'] = p[6]
    single_net['ig'] = p[7] 
    p[0] = single_net

def p_t0(p) : 
    '''t0 : LPAR T0 NUMBER RPAR'''
    p[0] = p[3]
def p_t1(p) : 
    '''t1 : LPAR T1 NUMBER RPAR'''
    p[0] = p[3]
def p_tx(p) : 
    '''tx : LPAR TX NUMBER RPAR'''
    p[0] = p[3]
def p_tc(p) : 
    '''tc : LPAR TC NUMBER RPAR'''
    p[0] = p[3]
def p_ig(p) : 
    '''ig : LPAR IG NUMBER RPAR'''
    p[0] = p[3]

def p_error(p):
    raise Exception("Syntax error at '%s' line: %d" % (p.value, p.lineno))


parser = yacc.yacc(debug=False, write_tables=False)
