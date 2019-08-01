#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:11:17 2019

@author: rodrigo
"""
import numpy as np
from MCMC import priors as priormodule

class Parameters(object):
    
    def __init__(self, priors=(), parameters=None, scenario=None):
        """
        Class containing the prior information on the parameters of a given
        scenario (false positive or planetary system).
        
        :param tuple or list priors: a tuple or list containing information
        of the prior density of each parameter. Each element is a list with
        at two elements: the prior type, and a further list with the prior
        parameters.
        
        :param tuple or list parameters: an optional list containing the names
        of the parameters.   
        :param str scenario: an optional string to identify the scenario.
        """
        self.priordict = {}
        self.scenario = scenario

        # Iteration over all parameter objects
        for i in range(len(priors)):
            
            if parameters is not None:
                param = parameters[i]
            else:
                param = i
            
            priortype = priors[i][0]
            pars = priors[i][1]
            
            try:
                # nparams = distdict[priortype][1] 
                prior = priormodule.distdict[priortype](*pars)
            except KeyError:
                raise priormodule.PriorError('Parameter {}: Unknown type '
                                             'of prior.'.format(param))
            
            self.priordict[param] = prior
        

    def draw(self, n, scenarios=None):
        """
        Draw n parameter sets from the priors.
        :param int n: size of sample to draw.        
        """
        self.draws = dict.fromkeys(self.priordict)
        for param in self.priordict:
            self.draws[param] = self.priordict[param].rvs(size=n)
        return
    
    
    def to_pastis(self):
        """
        Prepare dictonary to pass to PASTIS classes.
        """
        if not hasattr(self, "draws"):
            raise ValueError('Draws from the priors are needed. Run draw '
                             'metod')
        
        par1 = []

        # Dictionary with one dictionary per object
        ppars = dict.fromkeys(np.unique(par1), {})
        ppars = {}

        for par in self.draws:
            par_split = par.split('_')
            if len(par_split) != 2:
                raise ValueError("Parameter {} cannot be converted to PASTIS "
                                 "format".format(par))
                
            if par_split[0] not in ppars:
                # Initialise dictionary
                ppars[par_split[0]] = {}
                
            ppars[par_split[0]][par_split[1]] = self.draws[par]

        return ppars