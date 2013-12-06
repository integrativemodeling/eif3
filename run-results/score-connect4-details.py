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


list10 = []
list11 = []
list12 = []
list13 = []
list14 = []
list15 = []
list16 = []
list17 = []
list18 = []
list19 = []


listNames=[]
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
              Diff1 = (sqrt(pow(b[0][linkA]-b[0][linkB], 2) + pow(b[1][linkA]-b[1][linkB], 2) + pow(b[2][linkA]-b[2][linkB], 2)))-(b[3][RA]+b[3][RB])*1.25
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
              if cLink<0:
                     score1=1.0
              else:
                     score1=0.0
              Score_Inter= score1
              return Score_Inter       
 
      # def getScoreInteractions(lines1, cLink):
       #       if cLink<0:
       #              score1=0.0
       #       Score_Inter= score1 
       #       return Score_Inter
       
       

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

				
       #listOv = []
       list1 = [0]
       ScoreIA = []
       for i in list1:
              SA= getScoreInteractions(list1, outDiff[i])
	      ScoreIA.append(SA)
              SAB = sum(ScoreIA)
       print SAB	      

       list2 = [1]
       ScoreIB = []
       for i in list2:
              SB= getScoreInteractions(list2, outDiff[i])
              ScoreIB.append(SB)
              SAC = sum(ScoreIB)
       print SAC


       list3 = [2]
       ScoreIC = []
       for i in list3:
              SC= getScoreInteractions(list3, outDiff[i])
              ScoreIC.append(SC)
              SAI = sum(ScoreIC)
       print SAI

       list4 = [3]
       ScoreID = []
       for i in list4:
              SD= getScoreInteractions(list4, outDiff[i])
              ScoreID.append(SD)
              SAG = sum(ScoreID)
       print SAG



       list5 = [4]
       ScoreIE = []
       for i in list5:
              SE= getScoreInteractions(list5, outDiff[i])
              ScoreIE.append(SE)
              SBC = sum(ScoreIE)
       print SBC

       list6 = [5]
       ScoreIF = []
       for i in list6:
              SF= getScoreInteractions(list6, outDiff[i])
              ScoreIF.append(SF)
              SBI = sum(ScoreIF)
       print SBI


       list7 = [6]
       ScoreIG = []
       for i in list3:
              SG= getScoreInteractions(list7, outDiff[i])
              ScoreIG.append(SG)
              SBG = sum(ScoreIG)
       print SBG

       list8 = [7]
       ScoreIH = []
       for i in list8:
              SH= getScoreInteractions(list8, outDiff[i])
              ScoreIH.append(SH)
              SCI = sum(ScoreIH)
       print SCI



       list9 = [8]
       ScoreII = []
       for i in list9:
              SI= getScoreInteractions(list9, outDiff[i])
              ScoreII.append(SI)
              SCG = sum(ScoreII)
       print SCG

       list10 = [9]
       ScoreIJ = []
       for i in list10:
              SJ= getScoreInteractions(list10, outDiff[i])
              ScoreIJ.append(SJ)
              SIG = sum(ScoreIJ)
       print SIG



  #STot=SCI#+SCNI
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
       eSAB = str(SAB)
       eSAC = str(SAC)




       eSAI = str(SAI)
       eSAG = str(SAG)

       eSBC = str(SBC)
       eSBI = str(SBI)

       eSBG = str(SBG)
       eSCI = str(SCI)

       eSCG = str(SCG)
       eSIG = str(SIG)
#       list0.append(eS)
#       list1.append(ecA)
#       list2.append(eDiff)
       #list3.append(eSC)
       #list4.append(eSD)
       #list5.append(eSE)
       #list6.append(eSF)
       #list7.append(eSG)
       list10.append(eSAB)
       list11.append(eSAC)
       list12.append(eSAI)
       list13.append(eSAG)
       list14.append(eSBC)
       list15.append(eSBI)
       list16.append(eSBG)
       list17.append(eSCI)
       list18.append(eSCG)
       list19.append(eSIG)



       SummaryFileName = 'details-interFreq-upd.csv'

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
       SummaryFile.write(str(list10) +'\n')
       SummaryFile.write(str(list11) +'\n')
       SummaryFile.write(str(list12) +'\n')
       SummaryFile.write(str(list13) +'\n')
       SummaryFile.write(str(list14) +'\n')
       SummaryFile.write(str(list15) +'\n')
       SummaryFile.write(str(list16) +'\n')
       SummaryFile.write(str(list17) +'\n')
       SummaryFile.write(str(list18) +'\n')
       SummaryFile.write(str(list19) +'\n')



       #SummaryFile.write(str(listOv5) +'\n')
       #SummaryFile.write(str(listOv6) +'\n')
       

SummaryFile.flush()
SummaryFile.close()



        
        

