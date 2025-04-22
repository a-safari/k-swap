import math
import random

startingRangeOfProcessingTimes = 1
endingRangeOfProcessingTimes = 1000000000

numberOfJobs = 200
numberOfMachines = 10

numberOfInstances = 50

for i in range(numberOfInstances):
    fileName = "M" + str(numberOfMachines) + "_N" + str(numberOfJobs) + "_U" + str(startingRangeOfProcessingTimes) + "_" + str(endingRangeOfProcessingTimes) + "_" + str(i+1) + ".dat"
    f = open("Instances/" + "M" + str(numberOfMachines) + "_N" + str(numberOfJobs) + "_U" + str(startingRangeOfProcessingTimes) + "_" + str(endingRangeOfProcessingTimes) + "/" + fileName, "w")

    f.write(str(numberOfMachines) + "\n")
    f.write(str(numberOfJobs) + "\n")

    for j in range(numberOfJobs):
        randomNumber = math.floor(random.uniform(startingRangeOfProcessingTimes, endingRangeOfProcessingTimes))
        f.write(str(randomNumber) + "\n")
