from itertools import combinations
import random
import math
import scheduleStructure

class ABPrimeStructure(object):
    def __init__(self, setOfJobs, sumOfProcessingTimes):
        self.setOfJobs = setOfJobs  #jobNode2
        self.sumOfProcessingTimes = sumOfProcessingTimes

class KSwapNeighbourhood(object):
    def __init__(self, mySchedule, valueOfK):
        self.mySchedule = mySchedule
        self.valueOfK = valueOfK

    def searchRange(self, sortedList, startingPoint, endPoint):
        low = 0
        high = len(sortedList) - 1

        while low <= high:
            middle = low + (high - low) // 2
            if sortedList[middle].sumOfProcessingTimes > startingPoint and sortedList[middle].sumOfProcessingTimes < endPoint:
                return sortedList[middle]
            elif sortedList[middle].sumOfProcessingTimes <= startingPoint:
                low = middle + 1
            elif sortedList[middle].sumOfProcessingTimes >= endPoint:
                high = middle - 1

        return -1

    def ABCreator(self, maxMachineJobList, minMachineJobList, maxMachineIndex, minMachineIndex, typeOfAllocation):  #typeOfAllocation=0 => Randomly, typeOfAllocation=1 => Randomly and evenly
        A = []
        B = []
        sampleList = [0, 1]

        if typeOfAllocation == 0:
            for l in maxMachineJobList:
                x = random.choice(sampleList)
                if x == 0:
                    A.append(scheduleStructure.jobNode2(l, maxMachineIndex))
                else:
                    B.append(scheduleStructure.jobNode2(l, maxMachineIndex))
            for l in minMachineJobList:
                x = random.choice(sampleList)
                if x == 0:
                    A.append(scheduleStructure.jobNode2(l, minMachineIndex))
                else:
                    B.append(scheduleStructure.jobNode2(l, minMachineIndex))
        else:
            for l in range(0, len(maxMachineJobList), 2):
                x = random.choice(sampleList)
                if x == 0:
                    A.append(scheduleStructure.jobNode2(maxMachineJobList[l], maxMachineIndex))
                    if l+1 < len(maxMachineJobList):
                        B.append(scheduleStructure.jobNode2(maxMachineJobList[l+1], maxMachineIndex))
                else:
                    B.append(scheduleStructure.jobNode2(maxMachineJobList[l], maxMachineIndex))
                    if l+1 < len(maxMachineJobList):
                        A.append(scheduleStructure.jobNode2(maxMachineJobList[l+1], maxMachineIndex))
            for l in range(0, len(minMachineJobList), 2):
                x = random.choice(sampleList)
                if x == 0:
                    A.append(scheduleStructure.jobNode2(minMachineJobList[l], minMachineIndex))
                    if l+1 < len(minMachineJobList):
                        B.append(scheduleStructure.jobNode2(minMachineJobList[l+1], minMachineIndex))
                else:
                    B.append(scheduleStructure.jobNode2(minMachineJobList[l], minMachineIndex))
                    if l+1 < len(minMachineJobList):
                        A.append(scheduleStructure.jobNode2(minMachineJobList[l+1], minMachineIndex))


        return A, B
    
    def naiveOperator(self):
        for i in range(len(self.mySchedule.machineList)):
            for j in range(len(self.mySchedule.machineList)):
                if self.mySchedule.machineList[i].status == 1 and (self.mySchedule.machineList[j].status == 0 or self.mySchedule.machineList[j].status == -1):
                    for l in range(self.valueOfK):
                        kPrime = l + 1
                        if kPrime > len(self.mySchedule.machineList[i].jobsList):
                            break
                        for m in range(self.valueOfK - l):
                            kDoublePrime = m
                            if kDoublePrime > len(self.mySchedule.machineList[j].jobsList):
                                break

                            maxMachineCombinations = combinations(self.mySchedule.machineList[i].jobsList, kPrime)
                            minMachineCombinations = combinations(self.mySchedule.machineList[j].jobsList, kDoublePrime)
                            
                            for n in list(maxMachineCombinations):
                                sumOfProcessingTimesOfKPrimeJobs = 0
                                for nn in n:
                                    sumOfProcessingTimesOfKPrimeJobs += nn.processingTime

                                for o in minMachineCombinations:
                                    sumOfProcessingTimesOfKDoublePrimeJobs = 0
                                    for oo in o:
                                        sumOfProcessingTimesOfKDoublePrimeJobs += oo.processingTime

                                    if sumOfProcessingTimesOfKPrimeJobs - sumOfProcessingTimesOfKDoublePrimeJobs < self.mySchedule.makespan - self.mySchedule.machineList[j].machineLoad and sumOfProcessingTimesOfKPrimeJobs - sumOfProcessingTimesOfKDoublePrimeJobs > 0:
                                        updatedStatus = self.mySchedule.updateSchedule(n, o, i, j, sumOfProcessingTimesOfKPrimeJobs, sumOfProcessingTimesOfKDoublePrimeJobs)
                                        return updatedStatus #Mostly True

        return False

    def randomizedOperator(self):
        for i in range(len(self.mySchedule.machineList)):
            for j in range(len(self.mySchedule.machineList)):
                if self.mySchedule.machineList[i].status == 1 and (self.mySchedule.machineList[j].status == 0 or self.mySchedule.machineList[j].status == -1):
                    for k in range(self.valueOfK):
                        APrime = []
                        BPrime = []

                        #creaing the sets A and B
                        A, B = self.ABCreator(self.mySchedule.machineList[i].jobsList, self.mySchedule.machineList[j].jobsList, i, j, 1)

                        #Creating the sets A' and B'
                        S1 = combinations(A, math.ceil((k+1)/2))
                        S2 = combinations(B, math.floor((k+1)/2))

                        for m in list(S1):
                            valueOfSummation = 0
                            for n in m:
                                if n.machineNumber == i:
                                    valueOfSummation += n.jobObject.processingTime
                                elif n.machineNumber == j:
                                    valueOfSummation -= n.jobObject.processingTime
                            APrime.append(ABPrimeStructure(m, valueOfSummation))

                        for m in list(S2):
                            valueOfSummation = 0
                            for n in m:
                                if n.machineNumber == i:
                                    valueOfSummation += n.jobObject.processingTime
                                elif n.machineNumber == j:
                                    valueOfSummation -= n.jobObject.processingTime
                            BPrime.append(ABPrimeStructure(m, valueOfSummation))

                        #Sort B'
                        BPrime.sort(key=lambda x: x.sumOfProcessingTimes)

                        #Search
                        for m in APrime:
                            outputOfSearch = self.searchRange(BPrime, -(m.sumOfProcessingTimes), self.mySchedule.makespan - self.mySchedule.machineList[j].machineLoad - m.sumOfProcessingTimes)
                            if outputOfSearch != -1:
                                kPrimeList = []
                                kDoublePrimeList = []
                                for n in m.setOfJobs:
                                    if n.machineNumber == i:
                                        kPrimeList.append(n.jobObject)
                                    else:   #n.machineNumber == j
                                        kDoublePrimeList.append(n.jobObject)
                                for n in outputOfSearch.setOfJobs:
                                    if n.machineNumber == i:
                                        kPrimeList.append(n.jobObject)
                                    else:   #n.machineNumber == j
                                        kDoublePrimeList.append(n.jobObject)
                                
                                sumOfProcessingTimesOfKPrimeJobs = 0
                                sumOfProcessingTimesOfKDoublePrimeJobs = 0
                                for n in kPrimeList:
                                    sumOfProcessingTimesOfKPrimeJobs += n.processingTime
                                for n in kDoublePrimeList:
                                    sumOfProcessingTimesOfKDoublePrimeJobs += n.processingTime

                                updatedStatus = self.mySchedule.updateSchedule(kPrimeList, kDoublePrimeList, i, j, sumOfProcessingTimesOfKPrimeJobs, sumOfProcessingTimesOfKDoublePrimeJobs)
                                return updatedStatus #Mostly True

        return False






#mySchedule = scheduleStructure.schedule("instances/E3/M3_N17_U1_100_090.dat")
#myKSwapNeighbourhood = KSwapNeighbourhood(mySchedule, 4)

#output = myKSwapNeighbourhood.randomizedOperator()
#print("Done!")

#while True:
#    output = myKSwapNeighbourhood.randomizedOperator()
#    if output==False:
#        break 