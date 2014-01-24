#!/usr/bin/python

import re
# Select input file.
#InputFileName = raw_input('choose pym file to open: ')

#Nst = raw_input('enter number of structures: ')
#Nstrs = int(Nst)
Nstrs = 10000

for i in range(Nstrs):
    InputFileName = "conf_eif3." + str(i) + ".pym"
    if not os.path.exists(InputFileName):
        continue
    InputFile = open(InputFileName, 'r')  # Open file to read
    # string of lines from pdb file
    InputFileLines = InputFile.read().splitlines()
    # InputFile.close()

    Fname = 'conf_eif3.' + str(i) + '.tcl'
    f1 = open(Fname, 'w')
    f1.write('draw color blue' + '\n')
    for line in InputFileLines:
        if line.find('SPHERE') >= 0:
            seq = line[:]

            Newseq = seq.replace(",", " ")
            l = re.findall("(\S+)", Newseq)
            seqX = str(float(l[1]))
            seqY = str(float(l[2]))
            seqZ = str(float(l[3]))
            seqRad = str(float(l[4]))
            f1.write(
                'draw sphere { ' + seqX + ' ' + seqY + ' ' + seqZ + ' ' +
                '} radius ' + seqRad + ' resolution 300' + '\n')
