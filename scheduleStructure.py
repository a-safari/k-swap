import math

class jobNode(object):
    def __init__(self, processingTime, jobIndex):
        self.processingTime = processingTime
        self.jobIndex = jobIndex

class jobNode2(object):
    def __init__(self, jobObject, machineNumber):
        self.jobObject = jobObject     #jobNode
        self.machineNumber = machineNumber

class machineStructure(object):
    def __init__(self):
        self.machineLoad = 0
        self.status = 0     # -1 => min,    1 => max,   0 => min < load < max
        self.jobsList = []

class schedule(object):
    def __init__(self, inputFile):
        self.machineList = []
        self.makespan = 0
        self.minLoad = 0
        
        #Assignning the jobs to the machine and creating the initial schedule
        #self.balancedInititalSchedule(inputFile)
        self.LPTInitialSchedule(inputFile)
        

    def balancedInititalSchedule(self, inputFile): #creating the initial schedule in a balanced way
        f = open(inputFile, "r")
        numberOfMachines = int(f.readline().replace('\n',''))
        numberOfJobs = int(f.readline().replace('\n',''))
        jobsDividedByMachines = math.floor(numberOfJobs/numberOfMachines)
        jobIndex = 0

        for i in range(numberOfMachines):
            self.machineList.append(machineStructure())
            for j in range(jobsDividedByMachines):
                processingTime = float(f.readline().replace('\n',''))
                self.machineList[i].jobsList.append(jobNode(processingTime, jobIndex))
                self.machineList[i].machineLoad += processingTime
                jobIndex += 1

        while jobIndex < numberOfJobs: #Assigning the remaining jobs to the last machine
            processingTime = float(f.readline().replace('\n',''))
            self.machineList[len(self.machineList)-1].jobsList.append(jobNode(processingTime, jobIndex))
            self.machineList[len(self.machineList)-1].machineLoad += processingTime
            jobIndex += 1

        self.updateStatus()

    def LPTInitialSchedule(self, inputFile):
        f = open(inputFile, "r")
        numberOfMachines = int(f.readline().replace('\n',''))
        numberOfJobs = int(f.readline().replace('\n',''))

        ListOfProcessingTimes = []
        for i in range(numberOfJobs):
            ListOfProcessingTimes.append(float(f.readline().replace('\n',''))) 
        ListOfProcessingTimes.sort(reverse=True)

        for i in range(numberOfMachines):
            self.machineList.append(machineStructure())
        
        jobIndex = 0
        for pt in ListOfProcessingTimes:
            minIndex = self.getMinLoadMachineIndex()
            self.machineList[minIndex].jobsList.append(jobNode(pt, jobIndex))
            self.machineList[minIndex].machineLoad += pt
            jobIndex += 1

        self.updateStatus()

    
    def getMinLoadMachineIndex (self):
        minLoad = self.machineList[0].machineLoad
        minLoadIndex = 0
        for i in range(len(self.machineList)):
            if self.machineList[i].machineLoad < minLoad:
                minLoad = self.machineList[i].machineLoad
                minLoadIndex = i

        return minLoadIndex

    def updateStatus(self): #Determining the machines with max and min load
        minLoad = maxLoad = self.machineList[0].machineLoad

        for i in range(len(self.machineList)):     #Determining the max and min loads
            if self.machineList[i].machineLoad <= minLoad:
                minLoad = self.machineList[i].machineLoad
            elif self.machineList[i].machineLoad >= maxLoad:
                maxLoad = self.machineList[i].machineLoad

        self.makespan = maxLoad
        self.minLoad = minLoad

        if maxLoad == minLoad:
            #print("The max load is equal to the min load. So, the initial scheduler is optimal!")
            return "Global Optimal!"
            #return False
        else:
            for i in range(len(self.machineList)):
                if self.machineList[i].machineLoad == minLoad:
                    self.machineList[i].status = -1
                elif self.machineList[i].machineLoad == maxLoad:
                    self.machineList[i].status = 1
                else:
                    self.machineList[i].status = 0

        return True

    def updateSchedule(self, kPrimeList, kDoublePrimeList, maxMachineIndex, minMachineIndex, sumOfProcessingTimesOfKPrimeJobs, sumOfProcessingTimesOfKDoublePrimeJobs):     #swapping k' and k'' jobs between a critical and min-load machine 
        for i in kPrimeList:
            self.machineList[maxMachineIndex].jobsList.remove(i)
        for i in kDoublePrimeList:
            self.machineList[minMachineIndex].jobsList.remove(i)
        for i in kPrimeList:
            self.machineList[minMachineIndex].jobsList.append(i)
        for i in kDoublePrimeList:
            self.machineList[maxMachineIndex].jobsList.append(i)

        self.machineList[maxMachineIndex].machineLoad -= sumOfProcessingTimesOfKPrimeJobs
        self.machineList[maxMachineIndex].machineLoad += sumOfProcessingTimesOfKDoublePrimeJobs
        self.machineList[minMachineIndex].machineLoad -= sumOfProcessingTimesOfKDoublePrimeJobs
        self.machineList[minMachineIndex].machineLoad += sumOfProcessingTimesOfKPrimeJobs
        updatedStatus = self.updateStatus()
        return updatedStatus
            


#mySchedule = schedule("instances/E3/M3_N10_U1_100_003.dat")
#print("Done!")