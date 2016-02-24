[![DOI](https://zenodo.org/badge/20506/integrativemodeling/eif3.svg)](https://zenodo.org/badge/latestdoi/20506/integrativemodeling/eif3)

Data and scripts to model eIF3 from MS data.

## Steps

The method used here is the same as that used for the [MS benchmark](https://github.com/integrativemodeling/ms_benchmark).

To generate models, run the `ms_cg.py` script. This will generate a number of models of the complex, named `conf_eif3.<num>.pym`.

The `.pym` files can be converted to `.tcl` files by running the `pym2tcl.py` script, and then to `.mfj` files by running the `tcl2mfj.py` script.

## Info

_Author(s)_: Argyris Politis, email:argyris.politis@kcl.ac.uk

_Version_: 1.0

_License_: [LGPL](http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html).
This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2 of the License, or (at your option) any later version.

_Last known good IMP version_: [![build info](https://salilab.org/imp/systems/?sysstat=5&branch=master)](http://salilab.org/imp/systems/) [![build info](https://salilab.org/imp/systems/?sysstat=5&branch=develop)](http://salilab.org/imp/systems/)

_Testable_: Yes.

_Parallelizeable_: No

_Publications_:
 - Keren Lasker, Javier A. Velazquez-Muriel, Benjamin M. Webb, Zheng Yang, Thomas E. Ferrin, Andrej Sali, [Macromolecular assembly structures by comparative modeling and electron microscopy](http://salilab.org/pdf/Lasker_MethodsMolBiol_2011.pdf), Methods in Molecular Biology, 2011.
 - Politis A, Stengel F, Hall Z, Hernandez H, Leitner A, Waltzhoeni T, Robinson CV, Aebersold R. [A mass spectrometry-based hybrid method for structural modelling of protein complexes](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3972104/), Nature Methods, 11, 403-406, (2014) 
 - A. Politis, C. Schmidt, E. Tjioe, A. Sandercock, K. Lasker, Y. Gordiyenko, D. Russel, A. Sali, C. Robinson. [Topological models of heteromeric protein assemblies from mass spectrometry: Application to the yeast eIF3:eIF5 complex](http://salilab.org/pdf/Politis_ChemBiol_2015.pdf), Chem Biol 22, 117-128, 2015.
