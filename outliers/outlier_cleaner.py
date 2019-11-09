#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    import numpy as np
    
    n = len(predictions)
    
    # Error squared
    err_squared = (predictions-net_worths)**2
    
    # index sorted from smallest to largest error
    idx_dummy = np.argsort(err_squared.flatten())
    
    # Cut (take only 90%)
    idx_dummy = idx_dummy[:int(n*0.9)]
    cleaned_data = [(ages.flatten()[idx], net_worths.flatten()[idx], predictions.flatten()[idx]-net_worths.flatten()[idx]) for idx in idx_dummy] 
    
    return cleaned_data

