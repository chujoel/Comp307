import os
import random
import sys
from statistics import mode
from numpy import *

attributes = []
trainingInstances = []
testInstances = []
decisions = set()

def displayTree(node, indentation):
    if(node.left is not None):   # Check if have children
        print(indentation+node.attribute," = TRUE:")
        displayTree(node.left, indentation+"\t")
        print(indentation+node.attribute," = FALSE:")
        displayTree(node.right, indentation+"\t")
    else:
        if node.probability==0: print("Unknown, prob = 0")
        print(indentation+node.className, ", prob = ",node.probability)
    
    

def loadSets(loadFile, selectedInstance):
    # os.chdir("../../ass1_data/part2/golf")
    # print(os.listdir(os.curdir))
    with open(loadFile) as file:
        line = file.readline().replace("\n", "")
        if not len(attributes):
            attributes.extend(line.split(" "))
            attributes.pop(0)
        while line:
            line = file.readline().replace("\n", "")
            if line=='': continue
            instance = list(line.split(" "))
            temp = {}
            decisions.add(instance[0])
            for i in range(0, (len(instance))):
                if(i==0): temp["decision"] = instance[0]
                else: temp[attributes[i-1]] = instance[i]
            selectedInstance.append(temp)
            
    
class Node:
    def __init__(self):
        self.attribute = None
        self.left = None
        self.right = None
        self.probability = None
        self.className = None

    def setNode(self, attribute, left, right):
        self.attribute = attribute
        self.left = left
        self.right = right

    def setLeaf(self, className, probability):
        self.probability = probability
        self.className = className


def calculatePurity(branchList):
    if not len(branchList): return 0
    listCount = len(list(filter(lambda x: x["decision"]==next(iter(decisions)) , branchList)))
    return (listCount/len(branchList))*((len(branchList)-listCount)/len(branchList))


def findMostProbable(instances):
    classList = []
    for instance in instances: classList.append(instance["decision"])
    count = classList.count(mode(classList))
    if count == len(classList)/2: return [random.choice(classList), 0.5]

    return [mode(classList), count/len(classList)]


def getPurity(trueList, falseList):
    return (calculatePurity(trueList)*len(trueList)/len(trueList+falseList) + 
    calculatePurity(falseList)*len(falseList)/len(trueList+falseList))


def buildTree(instances, attributes):
    node = Node()
    temp = []
    if not len(instances): # Creating a leaf node to return
        temp = findMostProbable(trainingInstances)
        (node.setLeaf(temp[0], temp[1]))
        return node
        # Return leaf node containing name of class(yes or no) and prob(1)
    elif findMostProbable(instances)[1]==1 or not len(attributes):
        temp = findMostProbable(instances)
        (node.setLeaf(temp[0], temp[1]))
        return node
    else:
        bestPurity = 1
        bestAttr=""
        bestInstsFalse=[]
        bestInstsTrue = []
        for attribute in attributes:
            trueList = list(filter(lambda x: x[attribute]=="true" , instances))
            falseList = [x for x in instances if x not in trueList]
            currPurity = getPurity(trueList, falseList)
            if currPurity<bestPurity:
                bestPurity = currPurity
                bestInstsTrue = trueList
                bestInstsFalse = falseList
                bestAttr = attribute
        attrList = attributes
        attrList.remove(bestAttr)
        left = buildTree(bestInstsTrue, attrList)
        right = buildTree(bestInstsFalse, attrList)
        node.setNode(bestAttr, left, right)
        return node

def recursion(instance, node):
    if node.left==None: return node.className
    if instance[node.attribute] == "true": return recursion(instance, node.left) 
    if instance[node.attribute] == "false": return recursion(instance, node.right) 
    print("this should never happen")

def testTree(testInstances, root):
    accuracy = 0
    for instance in testInstances:
        if instance["decision"] == recursion(instance, root):
            accuracy+=1

    return(accuracy/len(testInstances))

def doTenFold():
    tenFoldList = []
    for i in range(10):
        attributes.clear()
        trainingInstances.clear()
        testInstances.clear()
        decisions.clear()
        loadSets("hepatitis-training-run-"+str(i), trainingInstances)
        loadSets("hepatitis-test-run-"+str(i), testInstances)
        root = buildTree(trainingInstances, attributes)
        tenFoldList.append(testTree(testInstances, root))
        print(str(i)+")"+str(testTree(testInstances, root)))
    print("Ten fold average = "+str(average(tenFoldList)))

def findBaseline():
    classes = []
    count=0
    for instance in trainingInstances:
        classes.append(instance["decision"])
    baseLine = mode(classes)
    
    for instance in testInstances:
        if(baseLine==instance["decision"]):
            count+=1
    return count/len(testInstances)


def main():
    os.chdir("../../ass1_data/part2")
    if(len(sys.argv)==1):
        doTenFold()
    else:
        loadSets(sys.argv[1], trainingInstances)
        loadSets(sys.argv[2], testInstances)
        root = buildTree(trainingInstances, attributes)
        displayTree(root, "")
        print("Baseline: "+str(findMostProbable(trainingInstances)))
        print("Test accuracy: "+str(testTree(testInstances, root)))


if __name__ == "__main__":
    main()