import numpy as np
from scipy import stats

def population_mean_test(population, population_mean):
    #sample 100 individuals randomly
    sample = np.random.choice(population, size=100, replace=False)
    #calculate mean and standard deviation
    sample_mean = np.mean(sample)
    sample_std = np.std(sample, ddof=1)
    
    #print("Sample mean: ", sample_mean)
    #print("Sample standard deviation: ", sample_std)
    
    #calculate an estimate of the standard error of the mean by 
    #dividing the sample standard deviation by square root of sample size
    
    #Standard error of the mean (SEM) - measures the variability of sample means
    sem = sample_std / np.sqrt(len(sample))
    
    #print("Standard error of the mean: ", sem)
    
    #calculate the confidence interval for confidence level of 95%
    confidence_level = 0.95
    df = len(sample) - 1
    
    confidence_interval = stats.t.interval(confidence_level, df, loc=sample_mean, scale=sem)
    #print("Confidence interval: ", confidence_interval)
    
    #test whether the population mean is captured by the confidence interval
    
    if confidence_interval[0] <= population_mean <= confidence_interval[1]:
        return 1
    return 0
    
def question1():
    print("Question 1: \n")

    #generate population of 10,000 random numbers from a normal distribution (mean -> 0 std -> 1)
    population = np.random.normal(loc=0, scale=1, size=10000)
    #calculate the population mean
    population_mean = np.mean(population)
    
    print("Population mean: ", population_mean)
    
    #repeat the process 100 times to test how it relates to the confidence level required
    num_captures = 0
    for _ in range(0,100):
        num_captures += population_mean_test(population, population_mean)
    
    print("The confidence interval captures the population mean ", num_captures, "/100 times.\n")
    
    #How does your result relate to the confidence level you asked for? (refer to txt file)
    
def simulate_dice_throw():
    dice = np.random.randint(1, 7, size=6)
    num_sixes = np.count_nonzero(dice == 6)
    
    return num_sixes

def question2():
    print("Question 2: \n")
    num_experiments = 1000
    count = 0
    
    for _ in range(num_experiments):
        num_sizes = simulate_dice_throw()
        if num_sizes >= 3:
            count += 1
            
    percentage = count / num_experiments * 100
    probability = count / num_experiments
    print("Chances of rolling 3 or more sizes:")
    print("Percentage: ", percentage)
    print("Probabilty: ", probability)
    
    ideal_probability = 1 - stats.binom.cdf(2,6,1/6)
    print("Ideal probability: ", ideal_probability)
    
question1()
question2()