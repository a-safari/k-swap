import math

#output file of the Improvement Time Table
outputText1 = open("Computational Results/Text/ImpTimeTable.dat", 'w')

#output file of the MS Improvement Table
outputText2 = open("Computational Results/Text/MakeSpanTable.dat", 'w')

#output file of the Total Time Table
outputText3 = open("Computational Results/Text/TotalTimeTable.dat", 'w')

#output file of the Number of Iterations Table
outputText4 = open("Computational Results/Text/NumOfItTable.dat", 'w')

MaximumValueOfK = 9
floatPrecisionTime = 1
floatPrecisionMS = 4

#Improvement Time Table
TC1R = open("Computational Results/dat/M2_N50_U1_1000000000_R_Time.dat", 'r')
TC1N = open("Computational Results/dat/M2_N50_U1_1000000000_N_Time.dat", 'r')
TC2R = open("Computational Results/dat/M2_N100_U1_1000000000_R_Time.dat", 'r')
TC2N = open("Computational Results/dat/M2_N100_U1_1000000000_N_Time.dat", 'r')
TC3R = open("Computational Results/dat/M2_N200_U1_1000000000_R_Time.dat", 'r')
TC3N = open("Computational Results/dat/M2_N200_U1_1000000000_N_Time.dat", 'r')
TC4R = open("Computational Results/dat/M5_N50_U1_1000000000_R_Time.dat", 'r')
TC4N = open("Computational Results/dat/M5_N50_U1_1000000000_N_Time.dat", 'r')
TC5R = open("Computational Results/dat/M5_N100_U1_1000000000_R_Time.dat", 'r')
TC5N = open("Computational Results/dat/M5_N100_U1_1000000000_N_Time.dat", 'r')
TC6R = open("Computational Results/dat/M5_N200_U1_1000000000_R_Time.dat", 'r')
TC6N = open("Computational Results/dat/M5_N200_U1_1000000000_N_Time.dat", 'r')
TC7R = open("Computational Results/dat/M10_N50_U1_1000000000_R_Time.dat", 'r')
TC7N = open("Computational Results/dat/M10_N50_U1_1000000000_N_Time.dat", 'r')
TC8R = open("Computational Results/dat/M10_N100_U1_1000000000_R_Time.dat", 'r')
TC8N = open("Computational Results/dat/M10_N100_U1_1000000000_N_Time.dat", 'r')
TC9R = open("Computational Results/dat/M10_N200_U1_1000000000_R_Time.dat", 'r')
TC9N = open("Computational Results/dat/M10_N200_U1_1000000000_N_Time.dat", 'r')

L1 = []
for i in range(1, MaximumValueOfK + 1):
    A1 = TC1R.readline()
    A2 = TC2R.readline()
    A3 = TC3R.readline()
    A4 = TC4R.readline()
    A5 = TC5R.readline()
    A6 = TC6R.readline()
    A7 = TC7R.readline()
    A8 = TC8R.readline()
    A9 = TC9R.readline()

    B1 = TC1N.readline()
    B2 = TC2N.readline()
    B3 = TC3N.readline()
    B4 = TC4N.readline()
    B5 = TC5N.readline()
    B6 = TC6N.readline()
    B7 = TC7N.readline()
    B8 = TC8N.readline()
    B9 = TC9N.readline()

    S1 = "\\textit{Randomized} & "+ str(i)+ " & "+ (str(round(float(A1.split("\t")[1]) * 1000, floatPrecisionTime)) if A1 != '' else "-")+ " & "+ (str(round(float(A2.split("\t")[1]) * 1000, floatPrecisionTime)) if A2 != '' else "-")+ " & "+ (str(round(float(A3.split("\t")[1]) * 1000, floatPrecisionTime)) if A3 != '' else "-")+ " & "+ (str(round(float(A4.split("\t")[1]) * 1000, floatPrecisionTime)) if A4 != '' else "-")+ " & "+ (str(round(float(A5.split("\t")[1]) * 1000, floatPrecisionTime)) if A5 != '' else "-")+ " & "+ (str(round(float(A6.split("\t")[1]) * 1000, floatPrecisionTime)) if A6 != '' else "-")+ " & "+ (str(round(float(A7.split("\t")[1]) * 1000, floatPrecisionTime)) if A7 != '' else "-")+ " & "+ (str(round(float(A8.split("\t")[1]) * 1000, floatPrecisionTime)) if A8 != '' else "-")+ " & "+ (str(round(float(A9.split("\t")[1]) * 1000, floatPrecisionTime)) if A9 != '' else "-")+ " \\\\ \n"
    S2 = "\\textit{Naive} & "+ str(i)+ " & "+ (str(round(float(B1.split("\t")[1]) * 1000, floatPrecisionTime)) if B1 != '' else "-")+ " & "+ (str(round(float(B2.split("\t")[1]) * 1000, floatPrecisionTime)) if B2 != '' else "-")+ " & "+ (str(round(float(B3.split("\t")[1]) * 1000, floatPrecisionTime)) if B3 != '' else "-")+ " & "+ (str(round(float(B4.split("\t")[1]) * 1000, floatPrecisionTime)) if B4 != '' else "-")+ " & "+ (str(round(float(B5.split("\t")[1]) * 1000, floatPrecisionTime))  if B5 != '' else "-")+ " & "+ (str(round(float(B6.split("\t")[1]) * 1000, floatPrecisionTime))  if B6 != '' else "-")+ " & "+ (str(round(float(B7.split("\t")[1]) * 1000, floatPrecisionTime))  if B7 != '' else "-")+ " & "+ (str(round(float(B8.split("\t")[1]) * 1000, floatPrecisionTime))  if B8 != '' else "-")+ " & "+ (str(round(float(B9.split("\t")[1]) * 1000, floatPrecisionTime))  if B9 != '' else "-")+ " \\\\ \n"
    L1.append(S1)
    L1.append(S2)

outputText1.writelines(L1)

TC1R.close()
TC1N.close()
TC2R.close()
TC2N.close()
TC3R.close()
TC3N.close()
TC4R.close()
TC4N.close()
TC5R.close()
TC5N.close()
TC6R.close()
TC6N.close()
TC7R.close()
TC7N.close()
TC8R.close()
TC8N.close()
TC9R.close()
TC9N.close()


#MakeSpanTable
TC1R = open("Computational Results/dat/M2_N50_U1_1000000000_R_MS.dat", 'r')
TC1N = open("Computational Results/dat/M2_N50_U1_1000000000_N_MS.dat", 'r')
TC2R = open("Computational Results/dat/M5_N50_U1_1000000000_R_MS.dat", 'r')
TC2N = open("Computational Results/dat/M5_N50_U1_1000000000_N_MS.dat", 'r')
TC3R = open("Computational Results/dat/M10_N50_U1_1000000000_R_MS.dat", 'r')
TC3N = open("Computational Results/dat/M10_N50_U1_1000000000_N_MS.dat", 'r')
TC4R = open("Computational Results/dat/M2_N100_U1_1000000000_R_MS.dat", 'r')
TC4N = open("Computational Results/dat/M2_N100_U1_1000000000_N_MS.dat", 'r')
TC5R = open("Computational Results/dat/M5_N100_U1_1000000000_R_MS.dat", 'r')
TC5N = open("Computational Results/dat/M5_N100_U1_1000000000_N_MS.dat", 'r')
TC6R = open("Computational Results/dat/M10_N100_U1_1000000000_R_MS.dat", 'r')
TC6N = open("Computational Results/dat/M10_N100_U1_1000000000_N_MS.dat", 'r')
TC7R = open("Computational Results/dat/M2_N200_U1_1000000000_R_MS.dat", 'r')
TC7N = open("Computational Results/dat/M2_N200_U1_1000000000_N_MS.dat", 'r')
TC8R = open("Computational Results/dat/M5_N200_U1_1000000000_R_MS.dat", 'r')
TC8N = open("Computational Results/dat/M5_N200_U1_1000000000_N_MS.dat", 'r')
TC9R = open("Computational Results/dat/M10_N200_U1_1000000000_R_MS.dat", 'r')
TC9N = open("Computational Results/dat/M10_N200_U1_1000000000_N_MS.dat", 'r')

L1 = []
for i in range(1, MaximumValueOfK + 1):
    A1 = TC1R.readline()
    A2 = TC2R.readline()
    A3 = TC3R.readline()
    A4 = TC4R.readline()
    A5 = TC5R.readline()
    A6 = TC6R.readline()
    A7 = TC7R.readline()
    A8 = TC8R.readline()
    A9 = TC9R.readline()

    B1 = TC1N.readline()
    B2 = TC2N.readline()
    B3 = TC3N.readline()
    B4 = TC4N.readline()
    B5 = TC5N.readline()
    B6 = TC6N.readline()
    B7 = TC7N.readline()
    B8 = TC8N.readline()
    B9 = TC9N.readline()

    S1 = "\\textit{Randomized} & "+ str(i)+ " & "+ (str(round(float(A1.split("\t")[1]), floatPrecisionMS)) if A1 != '' else "-")+ " & "+ (str(round(float(A2.split("\t")[1]), floatPrecisionMS)) if A2 != '' else "-")+ " & "+ (str(round(float(A3.split("\t")[1]), floatPrecisionMS)) if A3 != '' else "-")+ " & "+ (str(round(float(A4.split("\t")[1]), floatPrecisionMS)) if A4 != '' else "-")+ " & "+ (str(round(float(A5.split("\t")[1]), floatPrecisionMS)) if A5 != '' else "-")+ " & "+ (str(round(float(A6.split("\t")[1]), floatPrecisionMS)) if A6 != '' else "-")+ " & "+ (str(round(float(A7.split("\t")[1]), floatPrecisionMS)) if A7 != '' else "-")+ " & "+ (str(round(float(A8.split("\t")[1]), floatPrecisionMS)) if A8 != '' else "-")+ " & "+ (str(round(float(A9.split("\t")[1]), floatPrecisionMS)) if A9 != '' else "-")+ " \\\\ \n"
    #S2 = "\\textit{Naive} & "+ str(i)+ " & "+ (str(round(float(B1.split("\t")[1]), floatPrecisionMS)) if B1 != '' else "-")+ " & "+ (str(round(float(B2.split("\t")[1]), floatPrecisionMS)) if B2 != '' else "-")+ " & "+ (str(round(float(B3.split("\t")[1]), floatPrecisionMS)) if B3 != '' else "-")+ " & "+ (str(round(float(B4.split("\t")[1]), floatPrecisionMS)) if B4 != '' else "-")+ " & "+ (str(round(float(B5.split("\t")[1]), floatPrecisionMS))  if B5 != '' else "-")+ " & "+ (str(round(float(B6.split("\t")[1]), floatPrecisionMS))  if B6 != '' else "-")+ " & "+ (str(round(float(B7.split("\t")[1]), floatPrecisionMS))  if B7 != '' else "-")+ " & "+ (str(round(float(B8.split("\t")[1]), floatPrecisionMS))  if B8 != '' else "-")+ " & "+ (str(round(float(B9.split("\t")[1]), floatPrecisionMS))  if B9 != '' else "-")+ " \\\\ \n"
    L1.append(S1)
    #L1.append(S2)

outputText2.writelines(L1)

TC1R.close()
TC1N.close()
TC2R.close()
TC2N.close()
TC3R.close()
TC3N.close()
TC4R.close()
TC4N.close()
TC5R.close()
TC5N.close()
TC6R.close()
TC6N.close()
TC7R.close()
TC7N.close()
TC8R.close()
TC8N.close()
TC9R.close()
TC9N.close()


#Total Time Table
TC1R = open("Computational Results/dat/M2_N50_U1_1000000000_R_TotalTime.dat", 'r')
TC1N = open("Computational Results/dat/M2_N50_U1_1000000000_N_TotalTime.dat", 'r')
TC2R = open("Computational Results/dat/M2_N100_U1_1000000000_R_TotalTime.dat", 'r')
TC2N = open("Computational Results/dat/M2_N100_U1_1000000000_N_TotalTime.dat", 'r')
TC3R = open("Computational Results/dat/M2_N200_U1_1000000000_R_TotalTime.dat", 'r')
TC3N = open("Computational Results/dat/M2_N200_U1_1000000000_N_TotalTime.dat", 'r')
TC4R = open("Computational Results/dat/M5_N50_U1_1000000000_R_TotalTime.dat", 'r')
TC4N = open("Computational Results/dat/M5_N50_U1_1000000000_N_TotalTime.dat", 'r')
TC5R = open("Computational Results/dat/M5_N100_U1_1000000000_R_TotalTime.dat", 'r')
TC5N = open("Computational Results/dat/M5_N100_U1_1000000000_N_TotalTime.dat", 'r')
TC6R = open("Computational Results/dat/M5_N200_U1_1000000000_R_TotalTime.dat", 'r')
TC6N = open("Computational Results/dat/M5_N200_U1_1000000000_N_TotalTime.dat", 'r')
TC7R = open("Computational Results/dat/M10_N50_U1_1000000000_R_TotalTime.dat", 'r')
TC7N = open("Computational Results/dat/M10_N50_U1_1000000000_N_TotalTime.dat", 'r')
TC8R = open("Computational Results/dat/M10_N100_U1_1000000000_R_TotalTime.dat", 'r')
TC8N = open("Computational Results/dat/M10_N100_U1_1000000000_N_TotalTime.dat", 'r')
TC9R = open("Computational Results/dat/M10_N200_U1_1000000000_R_TotalTime.dat", 'r')
TC9N = open("Computational Results/dat/M10_N200_U1_1000000000_N_TotalTime.dat", 'r')

L1 = []
for i in range(1, MaximumValueOfK + 1):
    A1 = TC1R.readline()
    A2 = TC2R.readline()
    A3 = TC3R.readline()
    A4 = TC4R.readline()
    A5 = TC5R.readline()
    A6 = TC6R.readline()
    A7 = TC7R.readline()
    A8 = TC8R.readline()
    A9 = TC9R.readline()

    B1 = TC1N.readline()
    B2 = TC2N.readline()
    B3 = TC3N.readline()
    B4 = TC4N.readline()
    B5 = TC5N.readline()
    B6 = TC6N.readline()
    B7 = TC7N.readline()
    B8 = TC8N.readline()
    B9 = TC9N.readline()

    S1 = "\\textit{Randomized} & "+ str(i)+ " & "+ (str(round(float(A1.split("\t")[1]) * 1000, floatPrecisionTime)) if A1 != '' else "-")+ " & "+ (str(round(float(A2.split("\t")[1]) * 1000, floatPrecisionTime)) if A2 != '' else "-")+ " & "+ (str(round(float(A3.split("\t")[1]) * 1000, floatPrecisionTime)) if A3 != '' else "-")+ " & "+ (str(round(float(A4.split("\t")[1]) * 1000, floatPrecisionTime)) if A4 != '' else "-")+ " & "+ (str(round(float(A5.split("\t")[1]) * 1000, floatPrecisionTime)) if A5 != '' else "-")+ " & "+ (str(round(float(A6.split("\t")[1]) * 1000, floatPrecisionTime)) if A6 != '' else "-")+ " & "+ (str(round(float(A7.split("\t")[1]) * 1000, floatPrecisionTime)) if A7 != '' else "-")+ " & "+ (str(round(float(A8.split("\t")[1]) * 1000, floatPrecisionTime)) if A8 != '' else "-")+ " & "+ (str(round(float(A9.split("\t")[1]) * 1000, floatPrecisionTime)) if A9 != '' else "-")+ " \\\\ \n"
    S2 = "\\textit{Naive} & "+ str(i)+ " & "+ (str(round(float(B1.split("\t")[1]) * 1000, floatPrecisionTime)) if B1 != '' else "-")+ " & "+ (str(round(float(B2.split("\t")[1]) * 1000, floatPrecisionTime)) if B2 != '' else "-")+ " & "+ (str(round(float(B3.split("\t")[1]) * 1000, floatPrecisionTime)) if B3 != '' else "-")+ " & "+ (str(round(float(B4.split("\t")[1]) * 1000, floatPrecisionTime)) if B4 != '' else "-")+ " & "+ (str(round(float(B5.split("\t")[1]) * 1000, floatPrecisionTime))  if B5 != '' else "-")+ " & "+ (str(round(float(B6.split("\t")[1]) * 1000, floatPrecisionTime))  if B6 != '' else "-")+ " & "+ (str(round(float(B7.split("\t")[1]) * 1000, floatPrecisionTime))  if B7 != '' else "-")+ " & "+ (str(round(float(B8.split("\t")[1]) * 1000, floatPrecisionTime))  if B8 != '' else "-")+ " & "+ (str(round(float(B9.split("\t")[1]) * 1000, floatPrecisionTime))  if B9 != '' else "-")+ " \\\\ \n"
    L1.append(S1)
    L1.append(S2)

outputText3.writelines(L1)

TC1R.close()
TC1N.close()
TC2R.close()
TC2N.close()
TC3R.close()
TC3N.close()
TC4R.close()
TC4N.close()
TC5R.close()
TC5N.close()
TC6R.close()
TC6N.close()
TC7R.close()
TC7N.close()
TC8R.close()
TC8N.close()
TC9R.close()
TC9N.close()


#Number of Iterations Table
TC1R = open("Computational Results/dat/M2_N50_U1_1000000000_R_NumIterations.dat", 'r')
TC1N = open("Computational Results/dat/M2_N50_U1_1000000000_N_NumIterations.dat", 'r')
TC2R = open("Computational Results/dat/M2_N100_U1_1000000000_R_NumIterations.dat", 'r')
TC2N = open("Computational Results/dat/M2_N100_U1_1000000000_N_NumIterations.dat", 'r')
TC3R = open("Computational Results/dat/M2_N200_U1_1000000000_R_NumIterations.dat", 'r')
TC3N = open("Computational Results/dat/M2_N200_U1_1000000000_N_NumIterations.dat", 'r')
TC4R = open("Computational Results/dat/M5_N50_U1_1000000000_R_NumIterations.dat", 'r')
TC4N = open("Computational Results/dat/M5_N50_U1_1000000000_N_NumIterations.dat", 'r')
TC5R = open("Computational Results/dat/M5_N100_U1_1000000000_R_NumIterations.dat", 'r')
TC5N = open("Computational Results/dat/M5_N100_U1_1000000000_N_NumIterations.dat", 'r')
TC6R = open("Computational Results/dat/M5_N200_U1_1000000000_R_NumIterations.dat", 'r')
TC6N = open("Computational Results/dat/M5_N200_U1_1000000000_N_NumIterations.dat", 'r')
TC7R = open("Computational Results/dat/M10_N50_U1_1000000000_R_NumIterations.dat", 'r')
TC7N = open("Computational Results/dat/M10_N50_U1_1000000000_N_NumIterations.dat", 'r')
TC8R = open("Computational Results/dat/M10_N100_U1_1000000000_R_NumIterations.dat", 'r')
TC8N = open("Computational Results/dat/M10_N100_U1_1000000000_N_NumIterations.dat", 'r')
TC9R = open("Computational Results/dat/M10_N200_U1_1000000000_R_NumIterations.dat", 'r')
TC9N = open("Computational Results/dat/M10_N200_U1_1000000000_N_NumIterations.dat", 'r')

L1 = []
for i in range(1, MaximumValueOfK + 1):
    A1 = TC1R.readline()
    A2 = TC2R.readline()
    A3 = TC3R.readline()
    A4 = TC4R.readline()
    A5 = TC5R.readline()
    A6 = TC6R.readline()
    A7 = TC7R.readline()
    A8 = TC8R.readline()
    A9 = TC9R.readline()

    B1 = TC1N.readline()
    B2 = TC2N.readline()
    B3 = TC3N.readline()
    B4 = TC4N.readline()
    B5 = TC5N.readline()
    B6 = TC6N.readline()
    B7 = TC7N.readline()
    B8 = TC8N.readline()
    B9 = TC9N.readline()

    S1 = "\\textit{Randomized} & "+ str(i)+ " & "+ (str(round(float(A1.split("\t")[1]), floatPrecisionTime)) if A1 != '' else "-")+ " & "+ (str(round(float(A2.split("\t")[1]), floatPrecisionTime)) if A2 != '' else "-")+ " & "+ (str(round(float(A3.split("\t")[1]), floatPrecisionTime)) if A3 != '' else "-")+ " & "+ (str(round(float(A4.split("\t")[1]), floatPrecisionTime)) if A4 != '' else "-")+ " & "+ (str(round(float(A5.split("\t")[1]), floatPrecisionTime)) if A5 != '' else "-")+ " & "+ (str(round(float(A6.split("\t")[1]), floatPrecisionTime)) if A6 != '' else "-")+ " & "+ (str(round(float(A7.split("\t")[1]), floatPrecisionTime)) if A7 != '' else "-")+ " & "+ (str(round(float(A8.split("\t")[1]), floatPrecisionTime)) if A8 != '' else "-")+ " & "+ (str(round(float(A9.split("\t")[1]), floatPrecisionTime)) if A9 != '' else "-")+ " \\\\ \n"
    S2 = "\\textit{Naive} & "+ str(i)+ " & "+ (str(round(float(B1.split("\t")[1]), floatPrecisionTime)) if B1 != '' else "-")+ " & "+ (str(round(float(B2.split("\t")[1]), floatPrecisionTime)) if B2 != '' else "-")+ " & "+ (str(round(float(B3.split("\t")[1]), floatPrecisionTime)) if B3 != '' else "-")+ " & "+ (str(round(float(B4.split("\t")[1]), floatPrecisionTime)) if B4 != '' else "-")+ " & "+ (str(round(float(B5.split("\t")[1]), floatPrecisionTime))  if B5 != '' else "-")+ " & "+ (str(round(float(B6.split("\t")[1]), floatPrecisionTime))  if B6 != '' else "-")+ " & "+ (str(round(float(B7.split("\t")[1]), floatPrecisionTime))  if B7 != '' else "-")+ " & "+ (str(round(float(B8.split("\t")[1]), floatPrecisionTime))  if B8 != '' else "-")+ " & "+ (str(round(float(B9.split("\t")[1]), floatPrecisionTime))  if B9 != '' else "-")+ " \\\\ \n"
    L1.append(S1)
    L1.append(S2)

outputText4.writelines(L1)

TC1R.close()
TC1N.close()
TC2R.close()
TC2N.close()
TC3R.close()
TC3N.close()
TC4R.close()
TC4N.close()
TC5R.close()
TC5N.close()
TC6R.close()
TC6N.close()
TC7R.close()
TC7N.close()
TC8R.close()
TC8N.close()
TC9R.close()
TC9N.close()


#closing output files
outputText1.close()
outputText2.close()
outputText3.close()
outputText4.close()