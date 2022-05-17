instances = []
# Class lable y
classLabels = ["no-recurrence-events", "recurrence-events"]
classLabelCountY = [0,0]

# List of attribute name

attributes = ["age", "menopause", "tumor-size", "inv-nodes", "node-caps", "deg-malig", "breast", "breast-quad", "irradiat"]

allAtributes = {"age" :["10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80-89", "90-99"], "menopause": ["lt40", "ge40", "premeno"], "tumor-size":["0-4", "5-9", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59"], "inv-nodes" :["0-2", "3-5", "6-8","9-11", "12-14", "15-17", "18-20", "21-23", "24-26", "27-29", "30-32","33-35", "36-39"], "node-caps": ["yes", "no"], "deg-malig": ["1","2","3"], "breast": ["left","right"],"breast-quad" :[ "left up", "left low", "right up", "right low", "central"], "irradiat" :["yes", "no"]}

AllCounterDict = {}
AllProbDict = {}
numClassLabels = 0
numFeatures = 0

# Triple nested for loop to initialize everything


def initializeCounters():
    for i in range(len(classLabels)):
        classLabelCountY[i] = 1
        for attribute in attributes:
            for value in allAtributes.get(attribute):
                AllCounterDict[classLabels[i]+attribute+value] = 1

def loadSets():
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

def main():
    initializeCounters()
    print(AllCounterDict)
    readfiles()


if __name__ == "__main__":
    main()