#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 10:49:39 2019

@author: rodrigo
"""
import sys
import os
import datetime
import imp
import numpy as np

import tools
import parameters
import assertions

# =============================================================================
# Read configuration file and test compliance
# =============================================================================
if len(sys.argv) < 2:
    infile = 'test_BEB.py'
else:
    infile = sys.argv[1]
    
scriptpath = os.path.split(os.path.realpath(__file__))[0]
inputfile = os.path.join(scriptpath, 'inputs', infile)
inconfig = imp.load_source('inconfig', inputfile)

# Test that necessary dictionaries are defined in input file.
assertions.test_module(inconfig)

# Test that the necessary parameters for the simulations are defined
assertions.test_simulparameters(inconfig.simuldict)

# =============================================================================
# If all these tests passed, initialise pastis
# =============================================================================
import pastis
pastis.initialize()

import pastis.ObjectBuilder as ob
import pastis.models.PHOT as phot

# =============================================================================
# Read parameters for simulation
# =============================================================================
n = inconfig.simuldict['size'] # size of sample
band = inconfig.simuldict['band'] # photmetric band
cadence = inconfig.simuldict['cadence'] / 60. / 24. # in days
scen = inconfig.simuldict['scenario']
lcdir = inconfig.simuldict['lcdir']

# =============================================================================
# Create directory with date of simulation
# =============================================================================
lcdir = os.path.join(lcdir, datetime.date.today().isoformat())

if not os.path.exists(lcdir):
    os.makedirs(lcdir)


# =============================================================================
# Draw parameter from priors
# =============================================================================

# Prepare inputs for Parameters class
priors, params = tools.prepare_priors(inconfig.objectdict)
           
# Instatianate parameters
mypars = parameters.Parameters(priors, params)

# Draw random parameters from priors
mypars.draw(n)

# Construct dictionary with draws and Pastis-like keys
paramdict = mypars.to_pastis()

# =============================================================================
# Iterate over draws
# =============================================================================
for i in range(n):
    
    # Assign draw values to objectdict
    for obj in paramdict:
        for par in paramdict[obj]:
            inconfig.objectdict[obj][par][0] = paramdict[obj][par][i]
    
    # Find longest orbital period for this iteration
    maxper = 0
    
    for obj in inconfig.objectdict:
        for par in inconfig.objectdict[obj]:
         
         if par == 'P':
             if inconfig.objectdict[obj][par][0] > maxper:
                 maxper = inconfig.objectdict[obj][par][0]
    
             
    # Construct time array for this iteration
    print('Build time array based on maximum found period, {} d, and provided ' 
          'cadence, {} minutes.'.format(maxper, inconfig.simuldict['cadence']))
    t = np.arange(-maxper/2., maxper/2 + cadence, cadence)
    print('Number of elements in time array: {}'.format(len(t)))
    
    
    # Construct PASTIS instances for this iteration
    objects = ob.ObjectBuilder(inconfig.objectdict)
    
    # Build PASTIS light curve for this iteration
    isphase = False
    contamination = 0
    fluxoot = 1
    lc = phot.PASTIS_PHOT(t, band, isphase, contamination, fluxoot, 
                          *objects)
    
    # Write to file
    data_to_write = np.vstack([t, lc])
    filename = os.path.join(lcdir, 'lc_{}_{:05d}.dat'.format(scen, i))
    tools.write_to_file(data_to_write, filename, sep='\t', fmt='.6f')
