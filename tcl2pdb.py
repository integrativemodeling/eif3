import os, sys, re
Ns=raw_input("enter numbe rof structures: ")
N = int(Ns)

# Wx Python module for choosing file to open
for i in range(N):
	counter = 1
	#lines = f.read().splitlines() # string of lines from pdb file//
	fileName="mod_trim."+str(i)+".tcl"
	#fileName="37_xlinks_nas6.tcl"
	InputFile = open(fileName,'r') # Open file to read
	lines = InputFile.read().splitlines() # string of lines from pdb file
	#print lines
# Function to convert pdb file into mfj type file
#def getMfj_file(Fname,strNA,lines):
	Fname = 'OutPdb.'+str(i)+'.pdb'
        f1 = open(Fname, 'w')
        #f1 = open(Fname, 'w')
        for line in lines:
                if line[0:11]=='draw sphere':
			str1=str("ATOM  ")
			str2=str("  CA  UNK A")
			str3=str("  1.00140.46           C")
			#counter = 1
                        l = re.findall ("(\S+)", line) 
                        x = float(l[3])
                        y = float(l[4])
                        z = float(l[5])
                        r = float(l[8])
                        #f1.write("%s %8.3f%8.3f%8.3f%s" % ('ATOM      1   B1 FUP     1     ',x,y,z,'  1.00  1.00         P')+'\n')
                        #f1.write('REMARK'+'\n')
                        #f1.write("%s%8.3f%s%8.3f%s%8.3f%7.1f%s" % ('    ',x,'      ',y,'      ',z,r,'      .00000')+'\n')
			#counter +=1
			f1.write("%s%5s%s%4s%s%8.3f%8.3f%8.3f%s" % (str1,counter,str2,counter,'    ',x,y,z,str3)+'\n')
			counter +=1
                        #f1.write("%s %10.5f %s %10.5f %s %10.5f %s %s %s" % (strSp,x,strSp1,y,strSp1,z,strAt5,str('     '),str('.00000'))+'\n')
        f1.write('END'+'\n')
        f1.close()

#def pdbAtomRenumber(pdb):
    #"""
    #Renumber all atoms in pdb file, starting from 1.
    #"""

    #out = []
    #counter = 1
    #for line in pdb:
        ## For and ATOM record, update residue number
        #if line[0:6] == "ATOM  " or line[0:6] == "TER   ":
            #out.append("%s%5s%s" % (line[0:6],counter,line[11:]))
            #counter += 1
        #else:
            #out.append(line)

    #return out

#pdb_file="CTDNA.pdb"
       ###InputFileName="rpn3_cgall.mfj"
       ##def ReadFile(InputFile):
              ##InputFile = open(InputFileName,'r') # Open file to read
              ##InputFileLines = InputFile.read().splitlines() # string of lines from pdb file
              ##InputFile.close()
              ##return InputFileLines
    
## Read in the pdb file
#f = open(pdb_file,'r')
#pdb = f.readlines()
#f.close()

#out = pdbAtomRenumber(pdb)

#out_file = "%s_renum.pdb" % pdb_file[:-4]
#g = open(out_file,'w')
#g.writelines(out)
#g.close()

