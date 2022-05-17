import sys
import os
import math 
from statistics import mode
KVALUE = 3
headers = []
trainingWineList = []
testWineList = []
distanceList = []
rangeList = []
accuracy = []

def findRange():
    for i in range (len(headers)-1):
        currList = []
        for wine in trainingWineList:
            currList.append(wine[i])
        rangeList.append(max(currList)-min(currList))
        

def findClosestK(testAnswer):
    newList = sorted(distanceList)
    kList = []
    for wine in newList[0:KVALUE]:
        kList.append(wine[1])
    print("Guess:",int(mode(kList)),"Answer:",int(testAnswer))
    if mode(kList)==testAnswer:
        accuracy.append(0)
    else: 
        accuracy.append(1)


def findDistance(testList, trainingList):
    distance=0
    for i in range (len(headers)-1):
        distance += pow(testList[i] - trainingList[i], 2)/pow(rangeList[i], 2)
    return math.sqrt(distance)


def loadSets(loadFile, selectedList):
    os.chdir("../../ass1_data/part1")
    with open(loadFile) as file:
        line = file.readline()
        if not len(headers):
            headers.extend(line.split(" "))
        while line:
            line = file.readline().replace("\n", "")
            if line=='':
                continue
            selectedList.append(list(map(float, line.split(" "))))


def search():
    findRange()
    for testWine in testWineList:
        distanceList.clear()
        for trainWine in trainingWineList:
            distanceList.append([findDistance(testWine, trainWine), trainWine[-1]])
        findClosestK(testWine[-1])
    print('Where k=',KVALUE)
    print('Accuracy: ',accuracy.count(0)/len(accuracy)*100,' == ',accuracy.count(0),'/',len(accuracy))


def main():
    loadSets(sys.argv[1], trainingWineList)
    loadSets(sys.argv[2], testWineList)
    search()
    print(rangeList)


if __name__ == "__main__":
    main()