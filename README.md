# eIF3

Data and scripts to model eIF3 from MS data.

## Steps

MS connectivity module for structural prediction of protein complexes
The MS connectivity module was implemented in C++ as a separate module within he open source IMP programme. It is capable of sampling and evaluating candidate structures from information derived from connectivity information (e.g. native MS, cross-linking MS). The method exploits a Monte Carlo search followed by a conjugate gradient (CG) optimization step4. From a large number of candidate model structures generated by sampling the conformational spaces of input structures (at the moment two input coordinate files are allowed), the algorithm gives a score (MS connectivity score) based on a Minimal Spanning Tree approach1.
Folder structure
•	DATA:
o	SCRIPTS: to run and analyse the benchmark
•	SAMPLING/MODEL GENERATION: scripts to generate the models
•	ANALYSIS: scripts to analyse the results
•	RESULTS:  Directory where the results and models are stored
o	OUTPUT: Results of the benchmark	
o	MODELS: Generated models

DATA:
 Generation and optimization of structural models
Script name: ms-cg.py
Input Fields:
•	Proteins in the system 
The input proteins, defined as a coarse grained format, are given the code as follows:
    create_protein("ProteinA", ResidsNumber)
    create_protein("ProteinB", ResidsNumber) 
    create_protein("ProteinC", ResidsNumber)
    …………………………………………………………………
    create_protein("ProteinX", ResidsNumber)
The first argument denotes the name of the protein and the second the number of residues and should be given as an integer.
•	Multiple copies of proteins
        r= IMP.core.MSConnectivityRestraint(score)
        iA = r.add_type([rps[0], rps[1], rps[2]]) # three copies of protein A
        iB = r.add_type([rps[3]]) # one copy of protein B
        iC = r.add_type([rps[4]]) # one copy of protein C
	        ………………………………………………………….
         iX = r.add_type([rps[X1]]) # one copy of protein X
•	Disassembly pathway of protein complexes
        n1 = r.add_composite([iA, iB, iC, iD])
        n2 = r.add_composite([iA, iB, iC], n1)
        n3 = r.add_composite([iA, iB], n2)
        n4 = r.add_composite([iA, iC], n2)
        n5 = r.add_composite([iA, iB, iD], n1)
        n6 = r.add_composite([iB, iD], n5)
        ………………………………………………………..

The above commands correspond to the disassembly pathway below:
 
   
•	Number of structural models to be generated: 
This specifies the number of models to generate as an output. The number of models is strongly depending on the topological complexity, number of subunits involved in the system.

Optional Input Fields (Optimization runs):
•	number_of_monte_carlo_steps:  Specify the number of Monte Carlo steps to take for each optimization step.
•	number_of_conjugate_gradient_steps: Specify the number of conjugated gradient optimization steps (default number:100)
•	Clustering: Specify the number of clusters to be generated and the number iterations. A k-means clustering approach is followed for generation of the clusters. Overall, more iterations produce better clusters.
RESULTS
Output:
The output of Sampling.py is a list of structural models generated by putting together the input proteins and their number of copies. The list of models is given to the user in the *.pym type of file ready to be opened by Pymol package. The scores for each structure calculated using the MS connectivity restraint is produced in *.csv type of file.
CSV Format:
•	Model number: Number of solution generated
•	Score: MS connectivity restraint. The produced score for each solution generated is calculated using the Minimal Spanning Tree (MST) algorithm

Usage:  To run the sampling script you should first specify the above 
usage: python sampling.py  

Visualization of generated structures:
The produced structures are generated as *.pym type of file to be readily displayed in Pymol visualization programme. 
Comparing the generated models with the known topologies
The output structures are subjects to comparison by measuring their closeness-to-fit with the known structures. The first step is to convert the *.pym type of files into *.mfj that can be read by Mobcal Code (Calculation of theoretical CCS). To do so, the pym2mfj.py script can be used. 
usage: python pym2mfj.py InputFileName OutputFileName
Then we run the “score-connect.py” which is capable of comparing the topologies of the structural models generated with the topology of the reference structure by scoring: A) the Interacrtions and B) the non-interactions. This means that if any interaction that exists in the reference structure is not found in the model, we give a penalty of 2.0 to this model. If, on the other hand, a non-existing interaction in the reference structure is found in the model, then the model receives a penalty of 1.0.


Describe here the steps necessary to run the scripts.

## Info

_Author(s)_: Argyris Politis

_Version_: 1.0

_License_: [LGPL](http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html).
This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2 of the License, or (at your option) any later version.

_Last known good IMP version_: XXXX

_Testable_: Yes.

_Parallelizeable_: No

_Publications_:
 - Keren Lasker, Javier A. Velazquez-Muriel, Benjamin M. Webb, Zheng Yang, Thomas E. Ferrin, Andrej Sali, [Macromolecular assembly structures by comparative modeling and electron microscopy](http://salilab.org/pdf/Lasker_MethodsMolBiol_2011.pdf), Methods in Molecular Biology, 2011.
