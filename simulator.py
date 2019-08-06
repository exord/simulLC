#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 10:49:39 2019

@author: rodrigo
"""
import os
import datetime
import imp

import pastis.AstroClasses as ac

import parameters

# Define directory were lightcurves will be saved
home = os.getenv('HOME')

# Create directory with date of simulation
lcdir = os.path.join(home, 'ExP/pastisML/lcs/',
                     datetime.date.today().isoformat())

# Read configuration file
infile = 'test.py'
inputfile = os.path.join(home, 'ExP/pastisML/', infile)

inconfig = imp.load_source('inconfig', inputfile)

# Prepare inputs for Parameters class
priors = []
params = []
for obj in inconfig.objectdict:
    for par in inconfig.objectdict[obj]:
        if inconfig.objectdict[obj][par][1] == 0:
            continue
        else:
            priors.append([inconfig.objectdict[obj][par][2][0],
                          [inconfig.objectdict[obj][par][2][1],
                           inconfig.objectdict[obj][par][2][2]]])
            params.append('{}_{}'.format(obj, par))
            
   
# Instatianate parameters
mypars = parameters.Parameters(priors, params)

# Define number of cases per scenario
n = 10

# Draw random parameters from priors
mypars.draw(n)

""""
for scenario in ids:    
    # Instantaniate a planetary system
    planet = ac.Planet
"""