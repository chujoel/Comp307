Python must be installed on the PC to run this!!!!!!!!!!!!
There are some libraries that may not be on the machine so it would be handy to have pip installed
to make it easy to install these libraries is needed.
Imports are listed below:

import sys
import os

Open this directory in terminal or cmd or any sort of command line

You should be at ......\SourceCode\part3>

From here, you can run the python file and give an input file. To run the regular Perptron with the ionosphere.data,
the input should look something like this:

py Perceptron.py ionosphere.data 

The ionosphere.data will be used as a training set and Perceptron.py will training until it hits the highest accuract which is 
when there are 315 correct guesses


To run the Perceptron with a split dataset, it will look similar to the call from above:

py PerceptronSplitSets.py ionosphere.data 

It will split the sets up into a training and test dataset. Will run until it reaches the maximum expected accuracy which will be 
when there are 187 correct guesses in the test set.