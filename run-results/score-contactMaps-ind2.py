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


list0 = []
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
listNames=[]
hits = 0
##Read input file
for i in range(NA, NB):
       #InputFileName="module1_20k_15Dec."+str(i)+".mfj"
       InputFileName="mod-abcgi2."+str(i)+".mfj"
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

       def getDiffs(lines, linkA, linkB, RA, RB):
              Diff1 = (sqrt(pow(b[0][linkA]-b[0][linkB], 2) + pow(b[1][linkA]-b[1][linkB], 2) + pow(b[2][linkA]-b[2][linkB], 2)))-(b[3][RA]+b[3][RB])*1.10
              return Diff1

       # X-link interactions observed in experiments
       # module 1: -A2B3 -A3B3 -B3C2 -A1C2
       # SIDs: 
       # 11-5 / E1-A3 >100 then penalty score=0.0 
       # 11-8 / E1-C1 (>100) and E2-C2 (<50, >20)
       # 6-8 / B1 - C2 (>100)
       # 5 - 8 / (A3-C2) (20<x<50)
       # 5- 9 / A2-D1 (>100)
       # 9-8 / D1-C1 (>100)
       
       def getScoreInteractions(lines1, cLink):
              hits = 0
	      if cLink<0:
		     hits = hits+1.0
              #Score_Inter= score1 
	      return hits
              #return Score_Inter
       

       listNames.append(InputFileName)
       #LinkA1 = raw_input("enter position of A1 Lys: ")
       #LinkA2 = raw_input("enter position of A2 Lys: ")
       #LinkB2 = raw_input("enter position of B2 Lys: ")
       outCA = []
       for i in range(0, 5):
              for j in range(0, 5):
                     if i < j:
		            cA = getDistancesAs(ReadFile(InputFileName), i, j)
		            outCA.append(cA)                     
       print outCA 


       outDiff = []
       for i in range(0, 5):
              for j in range(0, 5):
                     if i < j:
                            Diff = getDiffs(ReadFile(InputFileName), i, j, i, j)
                            outDiff.append(Diff)
       print outDiff

				
#       cA = getDistancesAs(ReadFile(InputFileName), posA1, posA2)
#       cB = getDistancesAs(ReadFile(InputFileName), posB1, posB2)
#       cC = getDistancesAs(ReadFile(InputFileName), posC1, posC2)
#       cD = getDistancesAs(ReadFile(InputFileName), posD1, posD2)
#       cE = getDistancesAs(ReadFile(InputFileName), posE1, posE2)
#       cF = getDistancesAs(ReadFile(InputFileName), posF1, posF2)
#       cG = getDistancesAs(ReadFile(InputFileName), posG1, posG2)
#       cH = getDistancesAs(ReadFile(InputFileName), posH1, posH2)
#       cI = getDistancesAs(ReadFile(InputFileName), posI1, posI2)

#       cK = getDistancesAs(ReadFile(InputFileName), posK1, posK2)
#       cL = getDistancesAs(ReadFile(InputFileName), posL1, posL2)

      # print cA#, cB#, cC

       
	#print c
       #listOv = []
       list1 = [0]
       ScoreI = []
       for i in list1:
              SA= getScoreInteractions(list1, outDiff[i])
	      ScoreI.append(SA)
              SCI = sum(ScoreI)
              #SumHits = sum(hits)
       print SCI	      



       STot=SCI#+SCNI
#+SD+SE+SF
#+SG+SH+SI+SK+SL
       #print SF
#       print STot
       #print SO
                                                                    
#       eSA = str(SA)
#       eSB = str(SB)
#       eSC = str(SC)
#       eSD = str(SD)
#       eSE = str(SE)
#       eSF= str(SF)
#       eSG = str(SG)
       ecA = str(outCA)
       eDiff=str(outDiff)
       eSTot = str(STot)
#       list0.append(eS)
#       list1.append(ecA)
#       list2.append(eDiff)
       #list3.append(eSC)
       #list4.append(eSD)
       #list5.append(eSE)
       #list6.append(eSF)
       #list7.append(eSG)
       list0.append(eSTot)

       SummaryFileName = 'Scores-ABitest.csv'

       SummaryFile = open(SummaryFileName, 'w')
       SummaryFile.write(str(listNames) +'\n')
#       SummaryFile.write(str(list0) +'\n')
#       SummaryFile.write(str(list1) +'\n') 
#       SummaryFile.write(str(list2) +'\n')
       #SummaryFile.write(str(list3) +'\n')
       #SummaryFile.write(str(list4) +'\n')
       #SummaryFile.write(str(list5) +'\n')
       #SummaryFile.write(str(list6) +'\n')
       #SummaryFile.write(str(list7) +'\n')
       SummaryFile.write(str(list0) +'\n')
#Shits=sum(list0)
#print Shits
       #SummaryFile.write(str(listOv4) +'\n')
       #SummaryFile.write(str(listOv5) +'\n')
       #SummaryFile.write(str(listOv6) +'\n')
       
       print hits 
SG =sum(SCI)
print SG
SummaryFile.flush()
SummaryFile.close()
#print hits
