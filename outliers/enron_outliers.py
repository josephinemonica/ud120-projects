#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]

# Remove the outlier "TOTAL" that is a spreadsheet quirk
data_dict.pop("TOTAL",0)

data = featureFormat(data_dict, features)


### your code below
# Visualize
matplotlib.pyplot.scatter(data[:,0],data[:,1])
matplotlib.pyplot.xlabel("Salary")
matplotlib.pyplot.ylabel("Bonus")
matplotlib.pyplot.show()

# Looking for the one outlier that stands out
# By printing ad looking at data outlier is 2.6704229e+07, 9.7343619e+07
# It's "TOTAL"
for key in data_dict.keys():
    if(data_dict[key]['salary'] != 'NaN' and data_dict[key]['salary']>25000000):
        print(key)
    

#We would argue that theres 4 more outliers to investigate; let's look at a couple of them
#Two people made bonuses of at least 5 million dollars
# and a salary of over 1 million dollars; in other words, they made out like bandits
for key in data_dict.keys():
    if(data_dict[key]['salary'] != 'NaN' and data_dict[key]['salary']>1000000 \
       and data_dict[key]['bonus']!='NaN' and data_dict[key]['bonus']>5000000):
        print(key)