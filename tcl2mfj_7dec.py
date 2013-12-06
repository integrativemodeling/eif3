# This code converts the pdb file (single file) into mfj file
# the total number of Atom lines is initially extracted 
# and then is written to a *.mfj file to be used for mobcal calculations
# C, H, 0,S and N are converted into 12,1,16,32 and 12, respectively
# This code is based on 3/12/08 code written by AKP
# Was modified for use of single files AKP
# It counts the number of atoms within the pdb file

from Numeric import *
import re
#import wx


Ns=raw_input("enter number of spheres: ")
Nsphs=str(Ns)
Nas = raw_input("enter number of first structure: ")
Nbs = raw_input("enter number of second structure: ")
Na = int(Nas)
Nb = int(Nbs)

# Wx Python module for choosing file to open
for i in range(Na, Nb):
	#fileName="c0"+str(i)+".tcl"

	#f = open(fileName,'r') # Open file to read//
	#lines = f.read().splitlines() # string of lines from pdb file//
	fileName="mod_trim."+str(i)+".tcl"
	InputFile = open(fileName,'r') # Open file to read
	lines = InputFile.read().splitlines() # string of lines from pdb file
	#print lines




# Function to convert pdb file into mfj type file
#def getMfj_file(Fname,strNA,lines):
	Fname = 'models_trim.'+str(i)+'.mfj'
        f1 = open(Fname, 'w')
        #f1 = open(Fname, 'w')
        f1.write(Fname+'\n')
        #f1.write(strNM+'\n')
        f1.write('1'+'\n')
        f1.write(Nsphs+'\n')
        f1.write('ang'+'\n')
        f1.write('none'+'\n')
        f1.write('1.0000'+'\n')
        for line in lines:
                if line[0:11]=='draw sphere':
                        l = re.findall ("(\S+)", line) 
                        #x = float(line[13:21]) # x-coordinates
                        #y = float(line[23:31]) # y-coordiantes
                        #z = float(line[32:39]) # z-coordinates
                        #r = float(line[48:52])
                        x = float(l[3])
                        y = float(l[4])
                        z = float(l[5])
                        r = float(l[8])
                        #strAt = str(line[13:14])
                        #strAt1 = strAt.replace('C', ' 12')
                        #strAt2 = strAt1.replace('H', '  1')
                        #strAt3 = strAt2.replace('N', ' 14')
                        #strAt4 = strAt3.replace('O', ' 16')
                       # strAt5 = strAt4.replace('S', ' 32')
                        #strSp1 = '  '
                        #strSp = '   '
                        #
                        #f1.write("%s %8.3f%8.3f%8.3f%s" % ('ATOM      1   B1 FUP     1     ',x,y,z,'  1.00  1.00         P')+'\n')
                        #f1.write('REMARK'+'\n')
                        f1.write("%s%8.3f%s%8.3f%s%8.3f%7.1f%s" % ('    ',x,'      ',y,'      ',z,r,'      .00000')+'\n')
        
                        #f1.write("%s %10.5f %s %10.5f %s %10.5f %s %s %s" % (strSp,x,strSp1,y,strSp1,z,strAt5,str('     '),str('.00000'))+'\n')
        #f1.write(' 3'+'\n')
        f1.close()

#f1.write('END'+'\n')
#Main
# Get Mfj file by assigning name
#for i in range(1000):
	#Fname = 'CONF.00'+str(i)+'.mfj'
	#get_Mfj = getMfj_file(Fname,strNA,lines)
