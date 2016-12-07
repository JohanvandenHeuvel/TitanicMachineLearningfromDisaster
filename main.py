# import libraries

import csv as csv
import numpy as np

# read file

train = csv.reader(open("Files/train.csv", 'r'))
trainHeader = train.__next__()
data = []
for row in train:
    data.append(row)
data = np.array(data)
print(data)

print ("test git")