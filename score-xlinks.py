# code to implement the xlinking scoring for the proteasome module 1 (Rpn3/Rpn7/SEM1)
#import wx

import re
#import os, numarray
import operator
from operator import itemgetter
#from numpy  import *
#from Numeric import *
from math import *
from Numeric import * # imports numerical python
import csv

NAstrs=raw_input("enter the first number of structures: ")
NBstrs=raw_input("enter the last number of structures: ")
NA=int(NAstrs)
NB=int(NBstrs)


LinkA1 = raw_input("enter position of A1 Lys: ")
LinkA2 = raw_input("enter position of A2 Lys: ")
LinkB1 = raw_input("enter position of B1 Lys: ")
LinkB2 = raw_input("enter position of B2 Lys: ")
LinkC1 = raw_input("enter position of C1 Lys: ")
LinkC2 = raw_input("enter position of C2 Lys: ")
LinkD1 = raw_input("enter position of D1 Lys: ")
LinkD2 = raw_input("enter position of D2 Lys: ")
LinkE1 = raw_input("enter position of E1 Lys: ")
LinkE2 = raw_input("enter position of E2 Lys: ")
LinkF1 = raw_input("enter position of F1 Lys: ")
LinkF2 = raw_input("enter position of F2 Lys: ")
LinkG1 = raw_input("enter position of G1 Lys: ")
LinkG2 = raw_input("enter position of G2 Lys: ")
#LinkH1 = raw_input("enter position of H1 Lys: ")
#LinkH2 = raw_input("enter position of H2 Lys: ")
#LinkI1 = raw_input("enter position of I1 Lys: ")
#LinkI2 = raw_input("enter position of I2 Lys: ")

#LinkK1 = raw_input("enter position of K1 Lys: ")
#LinkK2 = raw_input("enter position of K2 Lys: ")
#LinkL1 = raw_input("enter position of L1 Lys: ")
#LinkL2 = raw_input("enter position of L2 Lys: ")




weighA = raw_input("enter weighing factor for 1st Xlink: ")
weighB = raw_input("enter weighing factor for 2nd Xlink: ")
weighC = raw_input("enter weighing factor for 3rd Xlink: ")
weighD = raw_input("enter weighing factor for 4 Xlink: ")
weighE = raw_input("enter weighing factor for 5 Xlink: ")
weighF = raw_input("enter weighing factor for 6 Xlink: ")
weighG = raw_input("enter weighing factor for 7 Xlink: ")
#weighH = raw_input("enter weighing factor for 8 Xlink: ")
#weighI = raw_input("enter weighing factor for 9 Xlink: ")

#weighK = raw_input("enter weighing factor for 10 Xlink: ")
#weighL = raw_input("enter weighing factor for 11 Xlink: ")
#      wC = raw_input("enter weighing factor for 3rd Xlink: ")


posA1 = int(LinkA1)-1
posA2 = int(LinkA2)-1
posB1 = int(LinkB1)-1
posB2 = int(LinkB2)-1
posC1 = int(LinkC1)-1
posC2 = int(LinkC2)-1
posD1 = int(LinkD1)-1
posD2 = int(LinkD2)-1
posE1 = int(LinkE1)-1
posE2 = int(LinkE2)-1
posF1 = int(LinkF1)-1
posF2 = int(LinkF2)-1
posG1 = int(LinkG1)-1
posG2 = int(LinkG2)-1
#posH1 = int(LinkH1)
#posH2 = int(LinkH2)
#posI1 = int(LinkI1)
#posI2 = int(LinkI2)

#posK1 = int(LinkK1)
#posK2 = int(LinkK2)


wA = float(weighA)
wB = float(weighB)
wC = float(weighC)
wD = float(weighD)
wE = float(weighE)
wF = float(weighF)
wG = float(weighG)
#wH = float(weighH)
#wI = float(weighI)

#wK = float(weighK)
#wL = float(weighL)


list0 = []
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
listNames=[]
##Read input file
for i in range(NA, NB):
       InputFileName="conf_eif3."+str(i)+".mfj"
       def ReadFile(InputFile):
              InputFile = open(InputFileName,'r') # Open file to read
              InputFileLines = InputFile.read().splitlines() # string of lines from pdb file
              InputFile.close()
              return InputFileLines

       def coordinates(lines):
              outX=[]
              outY=[]
              outZ=[]
              outR=[]
              for i in lines[6:]:
                     l = re.findall ("(\S+)", i) 
                     X0 = float(l[0])
                     Y0 = float(l[1])
                     Z0 = float(l[2])
                     R0 = float(l[3])
                     outX.append(X0)
                     outY.append(Y0)
                     outZ.append(Z0)
                     outR.append(R0)
                     #print Scr2
              return outX, outY, outZ, outR
       b= coordinates(ReadFile(InputFileName))
       #print b[0][0]
       #coordinates(ReadFile(InputFileName))
       # we dont care for the internal connections as those are fixed through distance restraints
       # As are Rpn3, Bs Rpn7 and Cs Sem1
       # distances between the cross linked residues nas6 (210) and rpt1 (220) - in models from IMP where structures
       # are coarse grained to residue level are identified as 208 and 493 (in python: 207 and 492 tespectuively)
       def getDistancesAs(lines, linkA, linkB):
              DA1 = sqrt(pow(b[0][linkA]-b[0][linkB], 2) + pow(b[1][linkA]-b[1][linkB], 2) + pow(b[2][linkA]-b[2][linkB], 2))
              return DA1 

       
       # X-link interactions observed in experiments
       # module 1: -A2B3 -A3B3 -B3C2 -A1C2
       # SIDs: 
       # 11-5 / E1-A3 >100 then penalty score=0.0 
       # 11-8 / E1-C1 (>100) and E2-C2 (<50, >20)
       # 6-8 / B1 - C2 (>100)
       # 5 - 8 / (A3-C2) (20<x<50)
       # 5- 9 / A2-D1 (>100)
       # 9-8 / D1-C1 (>100)
       
       def getScoreXlinks(lines, cLink, weighing):
              if cLink<30:
                     score1=0.0
              else:
                     score1=1.0*weighing
              Score_Xlinks= score1 
              return Score_Xlinks
              
       

       listNames.append(InputFileName)
       #LinkA1 = raw_input("enter position of A1 Lys: ")
       #LinkA2 = raw_input("enter position of A2 Lys: ")
       #LinkB1 = raw_input("enter position of B1 Lys: ")
       #LinkB2 = raw_input("enter position of B2 Lys: ")
#      # LinkC1 = raw_input("enter position of C1 Lys: ")
#      # LinkC2 = raw_input("enter position of C2 Lys: ")
       #weighA = raw_input("enter weighing factor for 1st Xlink: ")
       #weighB = raw_input("enter weighing factor for 2nd Xlink: ")
#      # wC = raw_input("enter weighing factor for 3rd Xlink: ")


       #posA1 = int(LinkA1)
       #posA2 = int(LinkA2)
       #posB1 = int(LinkB1)
       #posB2 = int(LinkB2)
#      # posC1 = str(LinkC1)
#      # posC2 = str(LinkC2)
       #wA = float(weighA)
       #wB = float(weighB)


       cA = getDistancesAs(ReadFile(InputFileName), posA1, posA2)
       cB = getDistancesAs(ReadFile(InputFileName), posB1, posB2)
       cC = getDistancesAs(ReadFile(InputFileName), posC1, posC2)
       cD = getDistancesAs(ReadFile(InputFileName), posD1, posD2)
       cE = getDistancesAs(ReadFile(InputFileName), posE1, posE2)
       cF = getDistancesAs(ReadFile(InputFileName), posF1, posF2)
       cG = getDistancesAs(ReadFile(InputFileName), posG1, posG2)
#       cH = getDistancesAs(ReadFile(InputFileName), posH1, posH2)
#       cI = getDistancesAs(ReadFile(InputFileName), posI1, posI2)

#       cK = getDistancesAs(ReadFile(InputFileName), posK1, posK2)
#       cL = getDistancesAs(ReadFile(InputFileName), posL1, posL2)

       print cA, cB#, cC

       
	#print c
       #listOv = []
       SA= getScoreXlinks(ReadFile(InputFileName), cA, wA)
       SB= getScoreXlinks(ReadFile(InputFileName), cB, wB)
       SC= getScoreXlinks(ReadFile(InputFileName), cC, wC)
       SD= getScoreXlinks(ReadFile(InputFileName), cD, wD)
       SE= getScoreXlinks(ReadFile(InputFileName), cE, wE)
       SF= getScoreXlinks(ReadFile(InputFileName), cF, wF)
       SG= getScoreXlinks(ReadFile(InputFileName), cG, wG)
#       SH= getScoreXlinks(ReadFile(InputFileName), cH, wH)
#       SI= getScoreXlinks(ReadFile(InputFileName), cI, wI)

#       SK= getScoreXlinks(ReadFile(InputFileName), cK, wK)
#       SL= getScoreXlinks(ReadFile(InputFileName), cL, wL)


       STot=SA+SB+SC+SD+SE+SF+SG
#+SD+SE+SF
#+SG+SH+SI+SK+SL
       #print SF
       print STot
       #print SO
                                                                    
       eSA = str(SA)
       eSB = str(SB)
       eSC = str(SC)
       eSD = str(SD)
       eSE = str(SE)
       eSF= str(SF)
       eSG = str(SG)
       #ecA = str(cA)
       eST=str(STot)
#       list0.append(eS)
       list1.append(eSA)
       list2.append(eSB)
       list3.append(eSC)
       list4.append(eSD)
       list5.append(eSE)
       list6.append(eSF)
       list7.append(eSG)
       list0.append(eST)

       SummaryFileName = 'out_rt4-5-3.csv'
       SummaryFile = open(SummaryFileName, 'w')
       SummaryFile.write(str(listNames) +'\n')
#       SummaryFile.write(str(list0) +'\n')
       SummaryFile.write(str(list1) +'\n') 
       SummaryFile.write(str(list2) +'\n')
       SummaryFile.write(str(list3) +'\n')
       SummaryFile.write(str(list4) +'\n')
       SummaryFile.write(str(list5) +'\n')
       SummaryFile.write(str(list6) +'\n')
       SummaryFile.write(str(list7) +'\n')
       SummaryFile.write(str(list0) +'\n')


       #SummaryFile.write(str(listOv4) +'\n')
       #SummaryFile.write(str(listOv5) +'\n')
       #SummaryFile.write(str(listOv6) +'\n')
       

SummaryFile.flush()
SummaryFile.close()



        
        

