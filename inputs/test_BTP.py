#---------------------
# SIMULATION PARAMETERS
#--------------------
simuldict = {'scenario': 'BTP',
             'size': 10,
             'band': 'Kepler',
             'cadence': 2, # Cadence in minutes
             'lcdir': '/home/rodrigo/ExP/pastisML/lcs'
             }

#---------------------
#        PLANETARY SYSTEM
#--------------------
# =============================================================================
# Main star
# =============================================================================

stardict = {'logg': [4.44, 0, ['Normal', 1.79 , 0.3]],
            'teff': [5777.0, 0, ['Normal', 4850.0, 100.0]],
            'z': [0.0, 1, ['Normal', -0.07, 0.18]],
            'dist': [1000.0, 1, ['Uniform', 100.0, 2000.0]],
            'ebmv': [0.1, 1, ['Uniform', 0.0, 0.2]],
            'v0': [-5.0, 1, ['Uniform', -6.0, -4.0]],
            'vsini': [10.0, 0, ['Normal', 0.0, 0.0]],
            'gd': [1.0, 0, ['Normal', 0.0, 0.0]],
}

# =============================================================================
# Background binary
# =============================================================================

# Primary
bstar1 = {
        'minit': [4.0, 1, ['DoublePowerLaw', -1.55, -2.70, 1.0, 0.1, 30]],
        'logage': [9.77, 1, ['Uniform', 8.0, 10.0]],
        'z': [0.0, 1, ['Uniform', -2.5, 0.5]],
        ##'dist': [15.0, 1, 'Uniform', 10.0, 10000.0, 0.0, 0.0, ''],
        'albedo': [0.8, 1, ['Uniform', 0.6, 1.0]],
        'dist': [10.0, 1, ['PowerLaw', 2.0, 10.0, 8000.0]],
        'v0': [10, 0, ['Uniform', -100.0, 100.0]],
        'vsini': [2, 0, ['Uniform', 0.0, 30.0]],
        'ebmv': [0.1, 1, ['Uniform', 0.0, 0.2]],
        }

planet1 = {'Mp': [10.0, 1, ['Jeffreys', 0.1, 100.0]],
           'Rp': [1.0, 1, ['Uniform', 0.01, 2.1]],
           'albedo': [0.0, 0, ['Uniform', 0.0, 1.0]],
           'P': [3.0, 1, ['Normal', 3.7566, 0.0012]],
           'T0': [0.0, 0, ['Normal', 0.0, 0.0]],
           'ecc': [0.0, 0, ['Uniform', 0.0, 1.0]],
           #'incl': [90.0, 0, 'Sine', 0.0, 0.0, 0.0, 0.0, ''],
           'b': [0.2, 1, ['Uniform', 0.0, 1.0]],
           'omega': [0.0, 0, ['Uniform', 0.0, 360.0]],
            }

plansysdict = {
            'star1': 'Blend1', 
            'planet1': 'Planet1'
            }

objectdict = {'Target1' : stardict,
              'Blend1': bstar1,
              'Planet1': planet1,
              'PlanSys1' : plansysdict
              }