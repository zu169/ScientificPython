import numpy as np
import pandas as pd
import scipy as sp 
from scipy import stats
import matplotlib.pyplot as plt


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
    #Skewness - measure of symmetry 
    #Kurtosis - measure of the tailedness of a distribution (how often outliers occur)
    print("\nSkewness: ", skewness, "\nKurtosis: ", kurtosis)
    
def question2():
    print("\nQuestion 2: ")
    normal_array  = np.random.normal(loc=50, scale=10, size=100) 
    print("\nNormally-Distributed Array:", normal_array)
    
    mean = np.mean(normal_array)
    median = np.median(normal_array)
    variance = np.var(normal_array)
    std_dev = np.std(normal_array)
    print("\nMean: ", mean, "\nMedian: ", median, "\nVariance: ", variance, "\nStandard Deviation: ", std_dev)
    
    skewness = stats.skew(normal_array)
    kurtosis = stats.kurtosis(normal_array)
    print("\nSkewness: ", skewness, "\nKurtosis: ", kurtosis)
    
def question3():
    print("\nQuestion 3:")
    df = pd.read_csv('camden_trees.csv')
    #describe function prints count,mean,std(min,25%,50%,75,max) for each column in dataframe
    summary_stats = df.describe()
    print("\nSummary Statistics for Camden Trees: \n", summary_stats)
    
    #plot Height column as a histogram
    df['Height'].hist()
    plt.xlabel('Height (m)')
    plt.ylabel('Frequency')
    plt.title('Height Distribution of Camden Trees')
    plt.show()
    
    plt.savefig('height_histogram.png')
    plt.clf()
    
    #plot Spread column as a historgram
    df['Spread'].hist()
    plt.title('Spread Distribution of Camden Trees')
    plt.xlabel('Spread (m)')
    plt.ylabel('Frequency')
    plt.show()
    
    plt.savefig('spread_histogram.png')

    #Group the data by tree maturity
    grouped_data = df.groupby('Maturity')
    
    #Plot the grouped Height column as histograms
    histograms = []
    for name,group in grouped_data:
        histogram = group['Height'].hist(alpha=0.5, label=name)
        histograms.append(histogram)
        
    plt.title('Height Distribution of Camden Trees by Maturity')
    plt.xlabel('Height (m)')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()
    
    plt.savefig('height_maturity_histogram.png')
    
    
    #Plot max Spread columns
    max_spread = grouped_data['Spread'].max()
    ax = max_spread.plot.bar()
    ax.set_title('Maximum Spread for each age of tree')
    ax.set_xlabel('Maturity')
    ax.set_ylabel('Maximum Spread (m)')
    plt.tight_layout()
    plt.show()
    
    plt.savefig('max_spread_maturity_histogram')
    
question1()
question2()
question3()