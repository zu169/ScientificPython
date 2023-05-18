import pandas as pd
import scipy.stats as stats

def femaleHeight(female_height):
    population_mean_female_height = 162.9

    t_stat, p_value = stats.ttest_1samp(female_height, population_mean_female_height)
    alpha = 0.05

    print("Null hypothesis: The average female student's height is the same as the average female American height.")
    if p_value < alpha:
        print("Null hypothesis rejected. The average female student's height differs from the average female American height.")
    else:
        print("Null hypothesis not rejected. The average female student's height is the same as the average female American height.")
        
    confidence_interval = stats.t.interval(0.95, len(female_height)-1, loc=female_height.mean(), scale=stats.sem(female_height))
    print("Confidence Interval:", confidence_interval,"\n")
    
def maleHeight(male_height):
    
    population_mean_male_height = 176.4

    t_stat, p_value = stats.ttest_1samp(male_height, population_mean_male_height)
    alpha = 0.05
    
    print("Null hypothesis: The average male student's height is the same as the average male American height.")
    if p_value < alpha:
        print("Null hypothesis rejected. The average male student's height differs from the average male American height.")
    else:
        print("Null hypothesis not rejected. The average male student's height is the same as the average male American height.")
        
    confidence_interval = stats.t.interval(0.95, len(male_height)-1, loc=male_height.mean(), scale=stats.sem(male_height))
    print("Confidence Interval:", confidence_interval,"\n")


df = pd.read_csv("brain.csv")

female_height = df[df['Gender'] == 'Female']['Height']
print(female_height.describe(),"\n")
femaleHeight(female_height)

male_height = df[df['Gender'] == 'Male']['Height']
print(male_height.describe(),"\n")
male_height = male_height.dropna()
male_height.dropna(inplace=True)
maleHeight(male_height)

#test for two independent samples
t_stat, p_value = stats.ttest_ind(female_height, male_height)
alpha = 0.05

print("Null hypothesis: The average female student's height is the same as the average male student's height.")
if p_value < alpha:
    print("Null hypothesis rejected. The average female student's height differs from the average male student's height.")
else:
    print("Null hypothesis not rejected. The average female student's height is the same as the average male student's height.")





