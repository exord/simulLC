#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 12:06:28 2019

@author: rodrigo
"""

def test_module(module):
    assert hasattr(module, 'objectdict'), ('Input file does not define '
              'attribute \"objectdict\"')
    assert hasattr(module, 'simuldict'), ('Input file does not define '
              'attribute \"simuldict\"')
    return

def test_simulparameters(paramdict):
    
    critical = {'size': 'number of simulations', 
                'band': 'photometric band',
                'cadence': 'time cadence of simulations',
                'lcdir': 'directory where lightcurves will be saved',
                'scenario': 'scenario to simulate'}
    
    missing = []
    message = ''
    for par in critical:
        if not par in paramdict:
            missing.append(par)
            
    if len(missing) == 0:
        return
    else:
        for par in missing:
            message += ('Critical parameter \"{}\" ({}) missing in '
            'simuldict.'.format(par, critical[par]))
        assert False, message
        
