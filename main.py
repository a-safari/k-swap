import scheduleStructure
import KSwap
import time
import os
import xlsxwriter
import math
import statistics
import Dynamic3DList

largeK = 9
mediumK = 6
smallK = 5
numOfTrials = 1 #For makespan in each itertion (2d list), num of trials should be always 1
ClassesList = [[2, 200, smallK, 1, 1000000000], 
                [2, 50, largeK, 1, 1000000000], 
                [2, 100, mediumK, 1, 1000000000], 
                [5, 200, smallK, 1, 1000000000], 
                [5, 50, largeK, 1, 1000000000],
                [5, 100, mediumK, 1, 1000000000],
                [10, 200, smallK, 1, 1000000000],
                [10, 50, largeK, 1, 1000000000],
                [10, 100, mediumK, 1, 1000000000]] #[machine, job, MaximumValueOfK, minProcesing, maxProcessing]


#ClassesList = [[5, 50, smallK, 1, 1000000000]] #[machine, job, MaximumValueOfK, minProcesing, maxProcessing]


classCounter = 1
TfileCounter = 0
Tst = time.process_time()

for MJItem in ClassesList:
    print("Class " + str(classCounter) + " started:")

    MaximumValueOfK = MJItem[2]
    className = "M" + str(MJItem[0]) + "_N" + str(MJItem[1]) + "_U" + str(MJItem[3]) + "_" + str(MJItem[4])
    directoryOfInputFiles = "ConvertedInstances/" + className #input directory
    outputExcel = "Computational Results/excel/" + className + ".xlsx" #output file of details
    
    outputDatRTime = "Computational Results/dat/" + className + "_R_Time.dat" #output file of diagrams for the Randomized operator Time
    outputDatNTime = "Computational Results/dat/" + className + "_N_Time.dat" #output file of diagrams for the Naive operator Time
    
    outputDatRMS = "Computational Results/dat/" + className + "_R_MS.dat" #output file of diagrams for the Randomized operator MakeSpan
    outputDatNMS = "Computational Results/dat/" + className + "_N_MS.dat" #output file of diagrams for the Naive operator MakeSpan
    
    outputDatRTotalTime = "Computational Results/dat/" + className + "_R_TotalTime.dat" #output file of diagrams for the Randomized Total Time
    outputDatNTotalTime = "Computational Results/dat/" + className + "_N_TotalTime.dat" #output file of diagrams for the Naive Total Time
    
    outputDatRNumIterations = "Computational Results/dat/" + className + "_R_NumIterations.dat" #output file of diagrams for the Randomized number of iterations
    outputDatNNumIterations = "Computational Results/dat/" + className + "_N_NumIterations.dat" #output file of diagrams for the Naive number of iterations

    outputDatRMSPerIteration = []
    outputDatNMSPerIteration = []
    for i in range(MaximumValueOfK):
        outputDatRMSPerIteration.append("Computational Results/dat/" + className + "_k" + str(i+1) + "_R_MSPerIteration.dat")
        outputDatNMSPerIteration.append("Computational Results/dat/" + className + "_k" + str(i+1) + "_N_MSPerIteration.dat")

    
    
    fileCounter = 0

    #open excel file
    workbook = xlsxwriter.Workbook(outputExcel) #output file
    worksheet = workbook.add_worksheet()
    row = 0
    floating_point = workbook.add_format({'num_format': '#,##0.00000000'})
    format_color = workbook.add_format()
    format_color.set_bg_color('#FF9900')

    #open other files
    datFileRTime = open(outputDatRTime, 'w')
    datFileNTime = open(outputDatNTime, 'w')
    datFileRMS = open(outputDatRMS, 'w')
    datFileNMS = open(outputDatNMS, 'w')
    datFileRTotalTime = open(outputDatRTotalTime, 'w')
    datFileNTotalTime = open(outputDatNTotalTime, 'w')
    datFileRNumIterations = open(outputDatRNumIterations, 'w')
    datFileNNumIterations = open(outputDatNNumIterations, 'w')

    datFileRMSPerIteration = []
    datFileNMSPerIteration = []
    for i in range(MaximumValueOfK):
        datFileRMSPerIteration.append(open(outputDatRMSPerIteration[i], 'w'))
        datFileNMSPerIteration.append(open(outputDatNMSPerIteration[i], 'w'))


    RSumTimeImproveNeighPerK = []
    NSumTimeImproveNeighPerK = []
    RSumMakeSpanImpPerK = []
    NSumMakeSpanImpPerK = []
    RSumTotalTimePerK = []
    NSumTotalTimePerK = []
    RSumNumOfIterationPerK = []
    NSumNumOfIterationPerK = []
    #we need the following 4 lists four computing standard deviation
    R2DListTimeImproveNeighPerK = []
    N2DListTimeImproveNeighPerK = []
    R2DMakeSpanImpPerK = []
    N2DMakeSpanImpPerK = []
    for i in range(MaximumValueOfK):
        RSumTimeImproveNeighPerK.append(0)
        NSumTimeImproveNeighPerK.append(0)
        RSumMakeSpanImpPerK.append(0)
        NSumMakeSpanImpPerK.append(0)
        R2DListTimeImproveNeighPerK.append([])
        N2DListTimeImproveNeighPerK.append([])
        R2DMakeSpanImpPerK.append([])
        N2DMakeSpanImpPerK.append([])

        RSumTotalTimePerK.append(0)
        NSumTotalTimePerK.append(0)
        RSumNumOfIterationPerK.append(0)
        NSumNumOfIterationPerK.append(0)

    #3D list for makespan in each iteration => Dimension 1: k, Dimension 2: iteration, Dimension 3:file
    RmakeSpanPerIteration3DList = Dynamic3DList.Dynamic3DList()
    NmakeSpanPerIteration3DList = Dynamic3DList.Dynamic3DList()


    for fileName in os.listdir(directoryOfInputFiles):
        fileCounter += 1
        TfileCounter += 1
        inputFile = os.path.join(directoryOfInputFiles, fileName)
        mySchedule = scheduleStructure.schedule(inputFile)
        initialMakeSpan = mySchedule.makespan

        worksheet.write(row, 0, "Name of the File")
        worksheet.write(row + 1, 0, fileName)
        worksheet.write(row, 1, "Initial MakeSpan")
        worksheet.write(row + 1, 1, initialMakeSpan, floating_point)
        worksheet.write(row, 2, "Number of Trials")
        worksheet.write(row + 1, 2, numOfTrials)
        worksheet.write(row, 3, "k")
        worksheet.write(row, 4, "R: (Average) Time of Finding a Local Optima")
        worksheet.write(row, 5, "N: (Average) Time of Finding a Local Optima")
        worksheet.write(row, 6, "R: (Average) Number of Iterations")
        worksheet.write(row, 7, "N: (Average) Number of Iterations")
        worksheet.write(row, 8, "R: Average Time in Finding an Improving Neighbourhood")
        worksheet.write(row, 9, "N: Average Time in Finding an Improving Neighbourhood")
        worksheet.write(row, 10, "R: (Average) MakeSpan")
        worksheet.write(row, 11, "N: (Average) MakeSpan")
        worksheet.write(row, 12, "R: (Average) MakeSpan Improvement")
        worksheet.write(row, 13, "N: (Average) MakeSpan Improvement")
        worksheet.write(row, 14, "R: (Average) MinLoad")
        worksheet.write(row, 15, "N: (Average) MinLoad")

        for k in range(1, MaximumValueOfK + 1):
            row += 1
            worksheet.write(row, 3, k)
            
            #Randomized Operator
            sumOfExecutionTimes = 0
            sumOfNumOfIterations = 0
            sumOfMakeSpans = 0
            sumOfMinLoads = 0

            for i in range(numOfTrials):
                print("Trial " + str(i+1) + " of randomized " + str(k) + "-swap for " + fileName + " file => file " + str(TfileCounter))
                mySchedule = scheduleStructure.schedule(inputFile)
                myKSwapNeighbourhood = KSwap.KSwapNeighbourhood(mySchedule, k)
                #print("MakeSpan: " + str(myKSwapNeighbourhood.mySchedule.makespan))
                numOfIterations = 0
                st = time.process_time()
                while True:
                    numOfIterations += 1
                    output = myKSwapNeighbourhood.randomizedOperator()
                    #print("MakeSpan: " + str(myKSwapNeighbourhood.mySchedule.makespan))
                    RmakeSpanPerIteration3DList[k, numOfIterations, fileCounter] = 1 - (myKSwapNeighbourhood.mySchedule.makespan/initialMakeSpan)
                    
                    if output==False:
                        p = 0
                        while(p < math.ceil(pow(2, k)/math.comb(k, math.floor(k/2)))):
                            p+=1
                            #numOfIterations += 1
                            output = myKSwapNeighbourhood.randomizedOperator()
                            RmakeSpanPerIteration3DList[k, numOfIterations, fileCounter] = 1 - (myKSwapNeighbourhood.mySchedule.makespan/initialMakeSpan)
                            #print("MakeSpan: " + str(myKSwapNeighbourhood.mySchedule.makespan))
                            #output = pool.map(myKSwapNeighbourhood.randomizedOperator, [0])
                            if output == "Global Optimal!":
                                break
                            if output==True:
                                p+=1
                                break
                        if p == math.ceil(pow(2, k)/math.comb(k, math.floor(k/2))):
                            break
                    if output == "Global Optimal!":
                        break
                et = time.process_time()
                sumOfExecutionTimes += (et - st)
                sumOfNumOfIterations += numOfIterations
                sumOfMakeSpans += myKSwapNeighbourhood.mySchedule.makespan
                sumOfMinLoads += myKSwapNeighbourhood.mySchedule.minLoad

            AverageCPUTimeOfTheProgram1 = sumOfExecutionTimes/numOfTrials
            AverageNumOfIterations1 = sumOfNumOfIterations/numOfTrials
            AverageAmountOfCPUTimePerItaration1 = AverageCPUTimeOfTheProgram1/AverageNumOfIterations1
            AverageMakeSpan1 = sumOfMakeSpans/numOfTrials
            AverageMinLoad1 = sumOfMinLoads/numOfTrials

            RSumTimeImproveNeighPerK[k - 1] += AverageAmountOfCPUTimePerItaration1
            makeSpanImprovement1 = 1 - (AverageMakeSpan1/initialMakeSpan)
            RSumMakeSpanImpPerK[k - 1] += makeSpanImprovement1
            RSumTotalTimePerK[k - 1] += AverageCPUTimeOfTheProgram1
            RSumNumOfIterationPerK[k - 1] += AverageNumOfIterations1

            #Naive Operator
            sumOfExecutionTimes = 0
            sumOfNumOfIterations = 0
            sumOfMakeSpans = 0
            sumOfMinLoads = 0

            for i in range(numOfTrials):
                print("Trial " + str(i+1) + " of naive " + str(k) + "-swap for " + fileName + " file => file " + str(TfileCounter))
                mySchedule = scheduleStructure.schedule(inputFile)
                myKSwapNeighbourhood = KSwap.KSwapNeighbourhood(mySchedule, k)
                #print("MakeSpan: " + str(myKSwapNeighbourhood.mySchedule.makespan))
                numOfIterations = 0
                st = time.process_time()
                while True:
                    numOfIterations += 1
                    output = myKSwapNeighbourhood.naiveOperator()
                    NmakeSpanPerIteration3DList[k, numOfIterations, fileCounter] = 1 - (myKSwapNeighbourhood.mySchedule.makespan/initialMakeSpan)
                    #print("MakeSpan: " + str(myKSwapNeighbourhood.mySchedule.makespan))
                    
                    if output==False or output == "Global Optimal!":
                        break
                et = time.process_time()
                sumOfExecutionTimes += (et - st)
                sumOfNumOfIterations += numOfIterations
                sumOfMakeSpans += myKSwapNeighbourhood.mySchedule.makespan
                sumOfMinLoads += myKSwapNeighbourhood.mySchedule.minLoad

            AverageCPUTimeOfTheProgram2 = sumOfExecutionTimes/numOfTrials
            AverageNumOfIterations2 = sumOfNumOfIterations/numOfTrials 
            AverageAmountOfCPUTimePerItaration2 = AverageCPUTimeOfTheProgram2/AverageNumOfIterations2
            AverageMakeSpan2 = sumOfMakeSpans/numOfTrials
            AverageMinLoad2 = sumOfMinLoads/numOfTrials

            NSumTimeImproveNeighPerK[k - 1] += AverageAmountOfCPUTimePerItaration2
            makeSpanImprovement2 = 1 - (AverageMakeSpan2/initialMakeSpan)
            NSumMakeSpanImpPerK[k - 1] += makeSpanImprovement2
            NSumTotalTimePerK[k - 1] += AverageCPUTimeOfTheProgram2
            NSumNumOfIterationPerK[k - 1] += AverageNumOfIterations2

            worksheet.write(row, 4, AverageCPUTimeOfTheProgram1, floating_point)
            worksheet.write(row, 6, AverageNumOfIterations1, floating_point)
            worksheet.write(row, 8, AverageAmountOfCPUTimePerItaration1, floating_point)
            R2DListTimeImproveNeighPerK[k - 1].append(AverageAmountOfCPUTimePerItaration1)
            worksheet.write(row, 10, AverageMakeSpan1, floating_point)
            worksheet.write(row, 12, makeSpanImprovement1, floating_point)
            R2DMakeSpanImpPerK[k - 1].append(makeSpanImprovement1)
            worksheet.write(row, 14, AverageMinLoad1, floating_point)

            worksheet.write(row, 5, AverageCPUTimeOfTheProgram2, floating_point)
            worksheet.write(row, 7, AverageNumOfIterations2, floating_point)
            worksheet.write(row, 9, AverageAmountOfCPUTimePerItaration2, floating_point)
            N2DListTimeImproveNeighPerK[k - 1].append(AverageAmountOfCPUTimePerItaration2)
            worksheet.write(row, 11, AverageMakeSpan2, floating_point)
            worksheet.write(row, 13, makeSpanImprovement2, floating_point)
            N2DMakeSpanImpPerK[k - 1].append(makeSpanImprovement2)
            worksheet.write(row, 15, AverageMinLoad2, floating_point)

            if AverageAmountOfCPUTimePerItaration2 > AverageAmountOfCPUTimePerItaration1:
                worksheet.write(row, 3, k, format_color)

        row += 3


    #Adding data to the dat file
    for i in range(MaximumValueOfK):
        RAVGT = RSumTimeImproveNeighPerK[i]/fileCounter
        #RSDT = statistics.stdev(R2DListTimeImproveNeighPerK[i])
        NAVGT = NSumTimeImproveNeighPerK[i]/fileCounter
        #NSDT = statistics.stdev(N2DListTimeImproveNeighPerK[i])
        #L1 = [str(i + 1), "\t", str(RAVGT), "\t", str(RSDT), "\n"]
        #L2  = [str(i + 1), "\t", str(NAVGT), "\t", str(NSDT), "\n"]
        L1 = [str(i + 1), "\t", str(RAVGT), "\n"]
        L2  = [str(i + 1), "\t", str(NAVGT), "\n"]
        datFileRTime.writelines(L1)
        datFileNTime.writelines(L2)

        RAVGMS = RSumMakeSpanImpPerK[i]/fileCounter
        #RSDMS = statistics.stdev(R2DMakeSpanImpPerK[i])
        NAVGMS = NSumMakeSpanImpPerK[i]/fileCounter
        #NSDMS = statistics.stdev(N2DMakeSpanImpPerK[i])
        #L3 = [str(i + 1), "\t", str(RAVGMS*100), "\t", str(RSDMS*100), "\n"]
        #L4  = [str(i + 1), "\t", str(NAVGMS*100), "\t", str(NSDMS*100), "\n"]
        L3 = [str(i + 1), "\t", str(RAVGMS*100), "\n"]
        L4  = [str(i + 1), "\t", str(NAVGMS*100), "\n"]
        datFileRMS.writelines(L3)
        datFileNMS.writelines(L4)

        RAVGTT = RSumTotalTimePerK[i]/fileCounter
        NAVGTT = NSumTotalTimePerK[i]/fileCounter
        L5 = [str(i + 1), "\t", str(RAVGTT), "\n"]
        L6  = [str(i + 1), "\t", str(NAVGTT), "\n"]
        datFileRTotalTime.writelines(L5)
        datFileNTotalTime.writelines(L6)

        RAVGNI = RSumNumOfIterationPerK[i]/fileCounter
        NAVGNI = NSumNumOfIterationPerK[i]/fileCounter
        L7 = [str(i + 1), "\t", str(RAVGNI), "\n"]
        L8  = [str(i + 1), "\t", str(NAVGNI), "\n"]
        datFileRNumIterations.writelines(L7)
        datFileNNumIterations.writelines(L8)

    
    RmakeSpanPerIteration3DList.pad_iterations_per_file()
    NmakeSpanPerIteration3DList.pad_iterations_per_file()

    RAverageOverFiles = RmakeSpanPerIteration3DList.average_over_files()
    NAverageOverFiles = NmakeSpanPerIteration3DList.average_over_files()
    for i in range(1, len(RAverageOverFiles)):
        for j in range(1, len(RAverageOverFiles[i])):
            L9 = [str(j), "\t", str(RAverageOverFiles[i][j]*100), "\n"]
            datFileRMSPerIteration[i-1].writelines(L9)
    for i in range(1, len(NAverageOverFiles)):
        for j in range(1, len(NAverageOverFiles[i])):
            L10 = [str(j), "\t", str(NAverageOverFiles[i][j]*100), "\n"]
            datFileNMSPerIteration[i-1].writelines(L10)
            
        
    #closing all the files
    workbook.close()
    datFileRTime.close()
    datFileNTime.close()
    datFileRMS.close()
    datFileNMS.close()
    datFileRTotalTime.close()
    datFileNTotalTime.close()
    datFileRNumIterations.close()
    datFileNNumIterations.close()

    for i in range(MaximumValueOfK):
        datFileRMSPerIteration[i].close()
        datFileNMSPerIteration[i].close()

    print("Class " + str(classCounter) + " Ended.")
    classCounter += 1

Tet = time.process_time()
print("Done!")
print("Total Execution Time: ", (Tet-Tst)//3600, "hours and ", ((Tet-Tst)%3600)//60, "minutes.")