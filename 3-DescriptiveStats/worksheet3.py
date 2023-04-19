import numpy as np
import scipy as sp
from scipy import stats

def question1():
    print("Question 1: \n")
    uniform_array = np.random.uniform(low=0, high=100, size=100)
    print("Uniform Array: \n", uniform_array)
    
    mean = np.mean(uniform_array)
    median = np.median(uniform_array)
    variance = np.var(uniform_array)
    std_dev = np.std(uniform_array)
    print("\nMean: ", mean, "\nMedian: ", median, "\nVariance: ", variance, "\nStandard Deviation: ", std_dev)
    
    skewness = stats.skew(uniform_array)
    kurtosis = stats.kurtosis(uniform_array)
    print("\n\nSkewness: ", skewness, "\nKurtosis: ", kurtosis)
    

    
question1()