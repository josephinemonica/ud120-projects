#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

# How many folks in this dataset have a quantified salary? What about a known email address?
n_email_address = 0
n_salary = 0

# How many folks in this datasetwith NaN in total payments
nan_total_payments = 0

# how many POIs have NaN total payments
# What percentage of POI as a whole is this
n_POI = 0
nan_total_payments_POI = 0

for key in enron_data.keys():
    if(enron_data[key]['email_address'] != 'NaN'):
        n_email_address = n_email_address+1
    if(enron_data[key]['salary'] != 'NaN'):
        n_salary = n_salary+1
    if(enron_data[key]['total_payments']=='NaN'):
        nan_total_payments += 1
    if(enron_data[key]['poi']):
        n_POI += 1
        if(enron_data[key]['total_payments']=='NaN'):
            nan_total_payments_POI += 1
            
print("No of people w quantified email is {}".format(n_email_address))
print("No of people w quantified salary is {}".format(n_salary))
print("{} out of {} people in this dataset have NaN total payments".\
      format(nan_total_payments, len(enron_data.keys())))
print("{} out of {} POI have NaN total payments".\
      format(nan_total_payments_POI, n_POI))