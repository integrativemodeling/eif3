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
list8 = []
list9 = []



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

listBest = [3773, 992, 2622, 342, 1409, 2697, 4051, 1722, 3633, 1434, 3969, 2440, 2989, 4856, 1782, 3576, 1635, 2519, 2492, 4751, 2948, 3556, 3551, 4440, 1263, 3174, 3880, 461, 1853, 2291, 1832, 379, 3159, 891, 4353, 4966, 1181, 1527, 1143, 1796, 8, 3973, 3827, 1011, 4622, 3092, 4926, 1799, 1926, 4967, 3261, 3116, 4576, 696, 3675, 4596, 1179, 3924, 2504, 3929, 3674, 3488, 2703, 1489, 2368, 2482, 4780, 2500, 1, 4004, 4606, 3369, 265, 793, 792, 3306, 4539, 4538, 28, 1734, 824, 4357, 3282, 3989, 1288, 1787, 2450, 3581, 2713, 2724, 1759, 3110, 652, 3678, 2439, 439, 1877, 1163, 1207, 2237, 1767, 3317, 1134, 2387, 3612, 2671, 2170, 1390, 570, 4549, 2806, 4055, 2384, 4624, 2253, 1811, 4000, 1380, 101, 39, 1772, 4730, 4086, 149, 1219, 2000, 1154, 3033, 833, 4221, 4865, 2952, 4521, 4836, 2946, 1460, 41, 2950, 2647, 4033, 2749, 956, 4675, 3537, 1668, 3690, 3830, 3254, 1184, 2984, 3666, 1167, 3733, 3850, 1361, 4541, 2212, 1650, 651, 3437, 3728, 840, 1587, 4543, 3750, 2265, 4574, 4260, 646, 1584, 1013, 2187, 3161, 961, 2469, 2836, 1567, 2061, 18, 4099, 2928, 3985, 2825, 349, 4938, 2615, 3749, 4458, 3871, 2533, 2630, 721, 3401, 2034, 2385, 1613, 4120, 2258, 1932, 3814, 1915, 1829, 4878, 4153, 1975, 115, 3374, 3652, 1973, 2272, 1404, 4190, 2098, 278, 1482, 3131, 575, 983, 3065, 4816, 4108, 4533, 2372, 2999, 4032, 1933, 3870, 2539, 1904, 4267, 796, 2299, 2338, 2626, 617, 789, 4773, 1699, 3168, 4582, 4392, 1779, 3368, 1175, 4861, 240, 4637, 2063, 2035, 4297, 1140, 1325, 4364, 4219, 1605, 2161, 2424, 3971, 2066, 3968, 4072, 1141, 3327, 1178, 1741, 3053, 3759, 4643, 542, 941, 4588, 591, 1828, 4490, 2260, 1647, 2464, 962, 4184, 4677, 769, 4896, 3591, 921, 586, 3243, 1573, 71, 3812, 2714, 1712, 4690, 334, 530, 4929, 578, 3663, 2563, 141, 1858, 318, 222, 947, 233, 4921, 4770, 3999, 2768, 1429, 687, 2796, 544, 3405, 2680, 3435, 564, 3790, 2691, 3679, 441, 2974, 2093, 3114, 4681, 4470, 1648, 698, 3434, 3166, 3860, 4423, 1307, 1524, 3173, 1098, 299, 948, 920, 2674, 4903, 47, 3069, 4303, 4558, 883, 3088, 140, 1512, 4728, 4431, 2911, 2707, 3966, 4003, 1457, 1137, 809, 2617, 4058, 4839, 3215, 1987, 4902, 4529, 2660, 2315, 3443, 3129, 2885, 2039, 4377, 3895, 2438, 4485, 440, 4457, 1087, 3481, 1632, 690, 1859, 1674, 1385, 3225, 395, 2444, 2051, 1056, 4608, 3535, 4590, 2263, 624, 3917, 1625, 2971, 777, 2101, 2097, 2955, 1789, 3363, 3496, 393, 4536, 2283, 59, 4334, 106, 1298, 3235, 2362, 2330, 1376, 3042, 2899, 1597, 2047, 1200, 2056, 2687, 2427, 773, 4755, 2409, 4880, 2793, 4864, 2944, 885, 339, 2119, 3932, 4838, 2337, 3117, 3385, 4723, 3912, 142, 1034, 1035, 1950, 545, 389, 2531, 689, 1138, 558, 260, 1730, 4387, 3194, 2455, 2990, 280, 4251, 1738, 137, 2915, 1323, 1360, 3746, 3570, 899, 2851, 4080, 173, 3854, 2902, 277, 3289, 896, 4044, 4585, 3662, 4256, 1378, 2739, 3244, 2756, 4351, 4815, 3762, 3818, 3250, 4525, 3502, 2560, 1909, 2809, 3543, 3714, 469, 2574, 3198, 4079, 2489, 2886, 321]



listNames=[]
##Read input file
#for i in range(NA, NB):
for i in listBest:
       #InputFileName="module1_20k_15Dec."+str(i)+".mfj"
       InputFileName="models_eif3-upd."+str(i)+".mfj"
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
       for i in range(0, 14):
              for j in range(0, 14):
                     if i < j:
		            cA = getDistancesAs(ReadFile(InputFileName), i, j)
		            outCA.append(cA)                     
       print outCA 


       outDiff = []
       for i in range(0, 14):
              for j in range(0, 14):
                     if i < j:
                            Diff = getDiffs(ReadFile(InputFileName), i, j, i, j)
                            outDiff.append(Diff)
       print outDiff

				
       #listOv = []
       listX1 = [36]
       ScoreIA1 = []
       for i in listX1:
              SA1= getScoreInteractions(listX1, outDiff[i])
	      ScoreIA1.append(SA1)
              S0 = sum(ScoreIA1)
       print S0	      

       listX2 = [37]
       ScoreIB1 = []
       for i in listX2:
              SB1= getScoreInteractions(listX2, outDiff[i])
              ScoreIB1.append(SB1)
              S1 = sum(ScoreIB1)
       print S1


       listX3 = [38]
       ScoreIC1 = []
       for i in listX3:
              SC1= getScoreInteractions(listX3, outDiff[i])
              ScoreIC1.append(SC1)
              S2 = sum(ScoreIC1)
       print S2

       listX4 = [39]
       ScoreID1 = []
       for i in listX4:
              SD1= getScoreInteractions(listX4, outDiff[i])
              ScoreID1.append(SD1)
              S3 = sum(ScoreID1)
       print S3



       listX5 = [40]
       ScoreIE1 = []
       for i in listX5:
              SE1= getScoreInteractions(listX5, outDiff[i])
              ScoreIE1.append(SE1)
              S4 = sum(ScoreIE1)
       print S4

       listX6 = [41]
       ScoreIF1 = []
       for i in listX6:
              SF1= getScoreInteractions(listX6, outDiff[i])
              ScoreIF1.append(SF1)
              S5 = sum(ScoreIF1)
       print S5


       listX7 = [42]
       ScoreIG1 = []
       for i in listX7:
              SG1= getScoreInteractions(listX7, outDiff[i])
              ScoreIG1.append(SG1)
              S6 = sum(ScoreIG1)
       print S6

       listX8 = [43]
       ScoreIH1 = []
       for i in listX8:
              SH1= getScoreInteractions(listX8, outDiff[i])
              ScoreIH1.append(SH1)
              S7 = sum(ScoreIH1)
       print S7



       listX9 = [44]
       ScoreII1 = []
       for i in listX9:
              SI1= getScoreInteractions(listX9, outDiff[i])
              ScoreII1.append(SI1)
              S8 = sum(ScoreII1)
       print S8

       listX10 = [45]
       ScoreIJ1 = []
       for i in listX10:
              SJ1= getScoreInteractions(listX10, outDiff[i])
              ScoreIJ1.append(SJ1)
              S9 = sum(ScoreIJ1)
       print S9



#       listX12 = [44]
#       ScoreIB2 = []
#       for i in listX12:
#              SB2= getScoreInteractions(listX12, outDiff[i])
#              ScoreIB2.append(SB2)
#              S11 = sum(ScoreIB2)
#       print S11


#       listX13 = [45]
#       ScoreIC2 = []
#       for i in listX13:
#              SC2= getScoreInteractions(listX13, outDiff[i])
#              ScoreIC2.append(SC2)
#              S12 = sum(ScoreIC2)
#       print S12

#       listX14 = [46]
#       ScoreID2 = []
#       for i in listX14:
#              SD2= getScoreInteractions(listX14, outDiff[i])
#              ScoreID2.append(SD2)
#              S13 = sum(ScoreID2)
#       print S13



#       listX15 = [47]
#       ScoreIE2 = []
#       for i in listX15:
#              SE2= getScoreInteractions(listX15, outDiff[i])
#              ScoreIE2.append(SE2)
#              S14 = sum(ScoreIE2)
#       print S14






  #STot=SCI#+SCNI
#+SD+SE+SF
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
       eS0 = str(S0)
       eS1 = str(S1)
       eS2 = str(S2)
       eS3 = str(S3)
       eS4 = str(S4)
       eS5 = str(S5)
       eS6 = str(S6)
       eS7 = str(S7)
       eS8 = str(S8)
       eS9 = str(S9)
#       eS10 = str(S10)
#       eS11 = str(S11)
#       eS12 = str(S12)
#       eS13 = str(S13)
#       eS14 = str(S14)

       list0.append(eS0)
       list1.append(eS1)
       list2.append(eS2)
       list3.append(eS3)
       list4.append(eS4)
       list5.append(eS5)
       list6.append(eS6)
       list7.append(eS7)
       list8.append(eS8)
       list9.append(eS9)
#       list10.append(eS10)
#       list11.append(eS11)
#       list12.append(eS12)
#       list13.append(eS13)
#       list14.append(eS14)


       SummaryFileName = 'details-eif3B1.csv'

       SummaryFile = open(SummaryFileName, 'w')
       SummaryFile.write(str(listNames) +'\n')
       SummaryFile.write(str(list0) +'\n')
       SummaryFile.write(str(list1) +'\n') 
       SummaryFile.write(str(list2) +'\n')
       SummaryFile.write(str(list3) +'\n')
       SummaryFile.write(str(list4) +'\n')
       SummaryFile.write(str(list5) +'\n')
       SummaryFile.write(str(list6) +'\n')
       SummaryFile.write(str(list7) +'\n')
       SummaryFile.write(str(list8) +'\n')
       SummaryFile.write(str(list9) +'\n')
#       SummaryFile.write(str(list10) +'\n')
#       SummaryFile.write(str(list11) +'\n')
#       SummaryFile.write(str(list12) +'\n')
#       SummaryFile.write(str(list13) +'\n')
#       SummaryFile.write(str(list14) +'\n')
       #SummaryFile.write(str(list19) +'\n')



       #SummaryFile.write(str(listOv5) +'\n')
       #SummaryFile.write(str(listOv6) +'\n')
       

SummaryFile.flush()
SummaryFile.close()



        
        

