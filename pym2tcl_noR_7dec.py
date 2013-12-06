#import wx
import re
#Select input file.
#InputFileName = raw_input('choose pym file to open: ')

Nst=raw_input('enter number of structures: ')
Nstrs=int(Nst)

for i in range(Nstrs):
        #InputFileName='cC.pym'
        InputFileName="conf_eif3."+str(i)+".pym"
	InputFile = open(InputFileName,'r') # Open file to read
	InputFileLines = InputFile.read().splitlines() # string of lines from pdb file
	#InputFile.close()

	
#for i in range(1000):
	Fname = 'mod_eif3-upd.'+str(i)+'.tcl'
	#Fname = 'cC.tcl'
        f1=open(Fname, 'w')
	f1.write('draw color blue'+'\n')
	for line in InputFileLines:
		if line.find('SPHERE')>=0:
			seq = line[:]
			
			Newseq = seq.replace(",", " ")
#			Newseq1 = Newseq.replace("17.3775", "18.0")
#			Newseq2 = Newseq1.replace("21.1383", "21.5")
#                        Newseq3 = Newseq2.replace("17.4926", "18.2")
#                        Newseq4 = Newseq3.replace("10.6476", "10.8")
#          		Newseq5 = Newseq4.replace("24.7802", "25.5")
#  			Newseq6 = Newseq5.replace("21.4088", "22.1")
#			#Newseq7 = Newseq6.replace("6.40257", "6.20")
#			Newseq7 = Newseq6.replace("18.6188", "19.5")
#			#Newseq9 = Newseq8.replace("5.94366", "6.0")
			#l = re.findall ("(\S+)", line)
			l = re.findall ("(\S+)", Newseq)
			#seqCoords = line[7:43]
			#seqX = line[7:15]
			seqX = str(float(l[1]))
			#seqY = line[16:24]
			seqY = str(float(l[2]))
			#seqZ = line[25:32]
			seqZ = str(float(l[3]))
			#seqRad = line[33:41]
			seqRad = str(float(l[4]))
			#f1.write('draw color red'+'\n')
			f1.write('draw sphere { ' + seqX + ' ' + seqY + ' ' + seqZ + ' ' + '} radius '+ seqRad + ' resolution 300'+'\n')
			#f1.write('draw color')
			#f1.write('draw color red')
	f1.close()
