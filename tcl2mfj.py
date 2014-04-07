#!/usr/bin/python

# This code converts the pdb file (single file) into mfj file
# the total number of Atom lines is initially extracted
# and then is written to a *.mfj file to be used for mobcal calculations
# C, H, 0,S and N are converted into 12,1,16,32 and 12, respectively
# This code is based on 3/12/08 code written by AKP
# Was modified for use of single files AKP
# It counts the number of atoms within the pdb file

import re
import os

#Ns = raw_input("enter number of spheres: ")
#Nsphs = str(Ns)
#Nas = raw_input("enter number of first structure: ")
#Nbs = raw_input("enter number of second structure: ")
#Na = int(Nas)
#Nb = int(Nbs)
Na = 0
Nb = 10000
Nsphs = "14"

for i in range(Na, Nb):
    fileName = "conf_eif3." + str(i) + ".tcl"
    if not os.path.exists(fileName):
        continue
    InputFile = open(fileName, 'r')  # Open file to read
    lines = InputFile.read().splitlines()  # string of lines from pdb file

    Fname = 'conf_eif3.' + str(i) + '.mfj'
    f1 = open(Fname, 'w')
    f1.write(Fname + '\n')
    f1.write('1' + '\n')
    f1.write(Nsphs + '\n')
    f1.write('ang' + '\n')
    f1.write('none' + '\n')
    f1.write('1.0000' + '\n')
    for line in lines:
        if line[0:11] == 'draw sphere':
            l = re.findall("(\S+)", line)
            x = float(l[3])
            y = float(l[4])
            z = float(l[5])
            r = float(l[8])
            f1.write(
                "%s%8.3f%s%8.3f%s%8.3f%7.1f%s" %
                ('    ', x, '      ', y, '      ', z, r, '      .00000') + '\n')
