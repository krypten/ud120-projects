#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    error = [(net_worth - prediction)**2  for net_worth, prediction in zip(net_worths, predictions)]
    cleaned_data = zip(ages, net_worths, error)

    ### your code goes here
    cleaned_data = sorted(cleaned_data, key=lambda x: x[2])
    cleaned_data = cleaned_data[:int(0.9 * len(cleaned_data))]
    return cleaned_data
