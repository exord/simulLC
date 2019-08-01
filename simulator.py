#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 10:49:39 2019

@author: rodrigo
"""
import os
import datetime

import pastis.AstroClasses as ac

from . import parameters

# Define directory were lightcurves will be saved
home = os.getenv('HOME')

# Create directory with date of simulation
lcdir = os.path.join(home, 'ExP/pastisML/lcs/',
                     datetime.date.today().isoformat())

# Define number of cases per scenario
n = 10

# Draw random parameters from priors, and scenarios ids
ids, params = parameters.draw(n)

for scenario in ids:    
    # Instantaniate a planetary system
    planet = ac.Planet