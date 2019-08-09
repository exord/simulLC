#---------------------
# SIMULATION PARAMETERS
#--------------------
simuldict = {'scenario': 'PLA',
             'band': 'Kepler',
             'cadence': 2, # Cadence in minutes
             'lcdir': '/home/rodrigo/ExP/pastisML/lcs'
             }

#---------------------
#        PLANETARY SYSTEM
#--------------------
# =============================================================================
# Planet Host
# =============================================================================

stardict = {'dens': [1.0, 0, ['Normal', 1.79 , 0.3]],
            'teff': [5777.0, 0, ['Normal', 4850.0, 100.0]],
            'z': [0.0, 1, ['Normal', -0.07, 0.18]],
            'dist': [1000.0, 1, ['Uniform', 100.0, 2000.0]],
            'ebmv': [0.1, 1, ['Uniform', 0.0, 0.2]],
            'v0': [-5.0, 1, ['Uniform', -6.0, -4.0]],
            'vsini': [10.0, 0, ['Normal', 0.0, 0.0]],
            'gd': [1.0, 0, ['Normal', 0.0, 0.0]],
}

# =============================================================================
# Planet(s) (repeat as many times as needed)
# =============================================================================
planetdict = {'P': [8.803611, 2, ['Normal', 8.803611, 0.014]],
              'T0': [0.0, 1, ['Normal', 0.0, 0.015]],
              'K1': [6.0, 1, ['Uniform', 0.0, 0.5]],
              'albedo2': [0.0, 0, ['Normal', 0.0, 0.0]],
              'ecc': [0.2, 1, ['Uniform', 0.0, 1.0]],
              'b' : [0.5, 1, ['Uniform', 0.0, 1.0]],
              # 'incl' : [90.0, 1, ['Sine', 60.0, 90.0]],
              'kr': [0.1, 1, ['Jeffreys', 0.01, 0.5]],
              'ar': [5, 1, ['Jeffreys', 5.0, 20.0]],
              'omega': [240.7, 1, ['Uniform', 0.0, 360.0]],
              'q': [0.0, 0, ['Uniform', 0.0, 0.2]],
              }

objectdict = {'PlanetHost1': stardict,
              'FitPlanet1': planetdict,
              'PlanSys1': {'star1': 'PlanetHost1',
                           'planet1': 'FitPlanet1'}
          }
              
              