trainingInstances = []
testInstances = []
# Class lable y
classLabels = ["no-recurrence-events", "recurrence-events"]
classLabelCountY = [0,0]
prob = [0,0]
allProb = {}
classProb = {}

# List of attribute name

attributes = ["age", "menopause", "tumor-size", "inv-nodes", "node-caps", "deg-malig", "breast", "breast-quad", "irradiat"]

allAtributes = {"age" :["10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80-89", "90-99"], "menopause": ["lt40", "ge40", "premeno"], "tumor-size":["0-4", "5-9", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59"], "inv-nodes" :["0-2", "3-5", "6-8","9-11", "12-14", "15-17", "18-20", "21-23", "24-26", "27-29", "30-32","33-35", "36-39"], "node-caps": ["yes", "no"], "deg-malig": ["1","2","3"], "breast": ["left","right"],"breast-quad" :[ "left_up", "left_low", "right_up", "right_low", "central"], "irradiat" :["yes", "no"]}

AllCounterDict = {}
AllProbDict = {}
attributeTotal = {}
numClassLabels = 0
numFeatures = 0
class_total=0

# Triple nested for loop to initialize everything


def initializeCounters():
    for i in range(len(classLabels)):
        classLabelCountY[i] = 1
        for attribute in attributes:
            for value in allAtributes.get(attribute):
                AllCounterDict[classLabels[i]+attribute+value] = 1

def loadSets(loadFile, selectedList):
    with open(loadFile) as file:
        line = file.readline()
        while line:
            line = file.readline().replace("\n", "")
            if line=='':
                continue
            thingList = list(line.split(","))
            thingList.pop(0)
            selectedList.append(thingList)
def train():
    for instance in trainingInstances:
        classLabelCountY[classLabels.index(instance[0])]+=1
        for i in range(len(attributes)):
            AllCounterDict[instance[0]+attributes[i]+instance[i+1]] = AllCounterDict[instance[0]+attributes[i]+instance[i+1]]+1
    class_total=0

    for i in range(len(classLabels)):
        class_total+=classLabelCountY[i]
        for j in range(len(attributes)):
            attributeTotal[classLabels[i]+attributes[j]]=0
            for thing in allAtributes[attributes[j]]:
                attributeTotal[classLabels[i]+attributes[j]] = attributeTotal[classLabels[i]+attributes[j]]+AllCounterDict[classLabels[i]+attributes[j]+thing]


    for i in range(len(classLabels)):
        prob[i] = classLabelCountY[i]/class_total
        for attribute in attributes:
            for thing in allAtributes[attribute]:
                allProb[classLabels[i]+attribute+thing] = AllCounterDict[classLabels[i]+attribute+thing] / attributeTotal[classLabels[i]+attribute]


def calculateScore(testInstance):
    score = prob[classLabels.index(testInstance[0])]
    for i in range(len(testInstance)):
        if i==0: continue
        score = score * allProb[testInstance[0]+attributes[i-1]+testInstance[i]]
    print(score)


def main():
    initializeCounters()
    loadSets("breast-cancer-training.csv", trainingInstances)
    train()
    loadSets("breast-cancer-test.csv", testInstances)
    calculateScore(testInstances[0])


if __name__ == "__main__":
    main()