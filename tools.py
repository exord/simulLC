#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 12:27:49 2019

@author: rodrigo
"""
import numpy as np

def prepare_priors(inputdict):
    priors = []
    params = []

    for obj in inputdict:
        for par in inputdict[obj]:
        
# =============================================================================
#             # Keep track of largest period
#             if par == 'P':
#                 if inputdict[obj][par][0] > maxper:
#                     maxper = inputdict[obj][par][0]
# =============================================================================
            
            # For fixed parameters, do not make draw
            if inputdict[obj][par][1] == 0:
                continue
            # Compound objects are also skipped
            elif isinstance(inputdict[obj][par], str):
                continue
            else:
                priors.append([inputdict[obj][par][2][0],
                               inputdict[obj][par][2][1:]])
                                
                params.append('{}_{}'.format(obj, par))
                
    return priors, params
    

def write_to_file(array_to_write, file, sep=',', fmt='.6f'):
    """
    Write a single 2-d floating point array to a file.
    
    Destroys file
    
    array_to_write
    sep: column separator
    fmt: format string to use for data
    """
    
    assert array_to_write.ndim <= 2
    
    a = np.atleast_2d(array_to_write)
    
    f = open(file, 'w')
    for i in range(a.shape[1]):
        for j, element in enumerate(a[:, i]):
            fmtstr = '{:'+fmt+'}'
            f.write(fmtstr.format(element))
            
            # If not last column, write separator
            if not j == a.shape[0] - 1:
                f.write(sep)
            # Break line
        f.write('\n')
        
            
        