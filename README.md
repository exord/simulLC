# simulLC
Code to produce simulated lightcurves based on PASTIS

## Dependency
The package uses the PASTIS package (not public yet; sorry!)

The PASTIS code is available on request, and the main paper describing it is:

```
@ARTICLE{pastis,
       author = {{D{\'\i}az}, R.~F. and {Almenara}, J.~M. and {Santerne}, A. and
         {Moutou}, C. and {Lethuillier}, A. and {Deleuil}, M.},
        title = "{PASTIS: Bayesian extrasolar planet validation - I. General framework, models, and performance}",
      journal = {\mnras},
     keywords = {methods: statistical, techniques: photometric, techniques: radial velocities, planetary systems, Astrophysics - Earth and Planetary Astrophysics},
         year = "2014",
        month = "Jun",
       volume = {441},
       number = {2},
        pages = {983-1004},
          doi = {10.1093/mnras/stu601},
archivePrefix = {arXiv},
       eprint = {1403.6725},
 primaryClass = {astro-ph.EP},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2014MNRAS.441..983D},
      }
```
    
## Usage
The main file is `simulator.py`, which can be run from a terminal as a stand alone script (but requires access to the pastisML sub-package) or from inside a running python3.

The code reads a configuration file with a format that depends on the astrophysical scneario that is being modelled. Some examples are shown in the inputs/ folder. Most global parameters are in the `simuldict` dictionary, at the top of these files. Then, details on the physical model are provided (more details soon!).

Then, the code is run
```
$ python3 PATH_TO_SCRIPT/simulator.py PATH_TO_CONFIG
```

The resulting light curves are stored in the the file `lcdir`, under a subdirectory with the current date. Currently, one tab-separated file is produced for each light curve being produced, and the scenario label `scenario` is appended to the file names.
