# sixs_json
This repository contains the modified 6S Fortran code to output json files and a Python wrapper to run the code and read the output.

It is intended to be used to generate look up tables or integrated in other software and is optimized for speed.

# Instalation

This software can be installed from this repository with the `build.sh` script on unix and `bld.bat` on windows.

It will be available from the conda-forge channel soon.

# Acknowledgements

The 6S code was developed by:
1. E.F. Vermote and S.Y. Kotchenova;
2. J.C. Roger;
3. D. Tanre, J.L. Deuze, M. Herman;
4. J.J. Morcrette;
5. T. Miura.

affiliated with:
1. Department of Geography, University of Maryland (4321 Hartwick Road, College Park, MD 20740, USA) and NASA Goddard Space Flight Center (code 614.5, Greenbelt, MD 20771, USA)
2. Observatoire de Physique du Globe de Clermont-Ferrand Universite Blaise Pascal (24 Avenue des Landais, 63177 Aubiere, France)
3. Laboratoire d'Optique Atmospherique,Universite des Sciences et Techniques de Lille (u.e.r. de Physique Fondamentale, 59655 Villeneuve d'Ascq Cedex, France)
4. European Center for Medium-Range Weather Forecasts (Shinfield Park, Reading, RG29AX, United Kingdom)
5. University of Hawaii at Manoa (1910 East_West Road, Sherman Lab 101 Honolulu, HI 96822)

The original code can be found at: https://salsa.umd.edu/6spage.html

A Python wrapper was developed by Robin Wilson and is available at: https://github.com/robintw/Py6S
I´ve reused some of his code to compile 6s in a platform independent way and build on conda-forge (https://github.com/conda-forge/sixs-feedstock).
