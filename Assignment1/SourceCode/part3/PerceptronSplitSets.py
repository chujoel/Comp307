import sys
import os

inputSignals=[]
testSignals = []
anserDict = {0:'b', 1:'g', 'b':0, 'g':1}
LEARNINGRATE = 1


def loadSets(loadFile):
    os.chdir("../../ass1_data/part3/")
    with open(loadFile) as file:
        line = file.readline().replace("\n", "")
        while line:
            line = file.readline().replace("\n", "")
            thing = line.split(" ")
            temp = []
            for i in range (len(thing)-1):
                temp.append(float(thing[i]))
            temp.append(thing[len(thing)-1])
            inputSignals.append(temp)
    inputSignals.pop(len(inputSignals)-1)
    for i in range (int((len(inputSignals)*0.4))):
        testSignals.append(inputSignals.pop())


def activate(number):
    if number > 0 : return 1
    return 0

def calculate(input, weights, bias):
    total=bias
    for i in range(len(input)-1): 
        total+=input[i]*weights[i]
    return total

def adjustWeights(weights, answer, input): # Figure out how much to change weights by
    if(anserDict[answer] == input[-1]):
        return weights
    for i in range(len(weights)):
        weights[i] += LEARNINGRATE* (anserDict[input[-1]] - answer) * input[i]
    return weights


def train():
    bias = -10
    weight = -28
    weights = [weight]*(len(inputSignals[0])-1)
    for i in range(500):
        correct=0
        for input in range(len(inputSignals)):
            # print(correct)
            answer = activate(calculate(inputSignals[input], weights, bias))
            if(answer == anserDict[inputSignals[input][-1]]): correct+=1
            weights = adjustWeights(weights, answer, inputSignals[input])
        if correct>=187:
            # If accurate enough, use the test data at that point and check accuracy
            print("Using weight: ",weight," And Bias: ",bias," This was the highest accuracy that I could find")
            print("it has been ",i,"Iterations. The results are above")
            print("Accuracy = ",correct,"/",len(inputSignals),"   ",correct/len(inputSignals)*100)

            print("\nUsing test data which has length of: ",len(testSignals))
            testCorrect=0
            for testInput in range(len(testSignals)):
                answer = activate(calculate(testSignals[testInput], weights, bias))
                if(answer == anserDict[testSignals[testInput][-1]]): testCorrect+=1
            print("Accuracy = ",testCorrect,"/",len(testSignals),"   ",testCorrect/len(testSignals)*100)
        # else:


def main():
    loadSets(sys.argv[1])
    train()

if __name__ == "__main__":
    main()