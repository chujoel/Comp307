Python must be installed on the PC to run this!!!!!!!!!!!!
There are some libraries that may not be on the machine so it would be handy to have pip installed
to make it easy to install these libraries is needed.
Imports are listed below:

import os
import random
import sys
from statistics import mode
from numpy import *



Open this directory in terminal or cmd or any sort of command line

You should be at ......\SourceCode\part2>

From here, you can run the python file and give a training(first parameter) and test set(second parameter)

To call it should look something like this:
 py DecisionTree.py hepatitis-training hepatitis-test

 Doing this will run the DecisionTree.py file and give it a training and test file as parameters


To run the 10 fold, simply don't enter any training or test sets as arguments. Your input should looks something like this
py DecisionTree.py

It will look for hepatitis-training-run- and hepatitis-test-run- both followed by some number