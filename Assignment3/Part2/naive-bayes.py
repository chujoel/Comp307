# Class lable y
classLabels = ["no-recurrence-events", "recurrence-events"]
classLabelCountY = [0,0]

# List of attribute name

attributes = ["age", "menopause", "tumor-size", "inv-nodes", "node-caps", "deg-malig", "breast", "breast-quad", "irradiat"]

ages = ["10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80-89", "90-99"]
menopause = ["lt40", "ge40", "premeno"]
tumorSize = ["0-4", "5-9", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59"]
invNodes =["0-2", "3-5", "6-8","9-11", "12-14", "15-17", "18-20", "21-23", "24-26", "27-29", "30-32","33-35", "36-39"]
nodeCaps = ["yes", "no"]
degMalig = ["1","2","3"]
breast = ["left","right"]
breastQuad = [ "left up", "left low", "right up", "right low", "central"]
irradiat = ["yes", "no"]


numClassLabels = 0
numFeatures = 0

# Triple nested for loop to initialize everything