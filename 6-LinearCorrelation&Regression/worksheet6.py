import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
from scipy.stats import pearsonr

def main():
    data = pd.read_csv('Poverty.csv')
    
    plt.scatter(data['GNP'], data['LExpF'])
    plt.xlabel('GNP')
    plt.ylabel('Female Life Expectancy')
    plt.title('Female Life Expectancy vs GNP')
    plt.show()
    
    data['Avg_Life_Expectancy'] = (data['LExpM'] + data['LExpF']) / 2
    
    correlation, p_value = pearsonr(data['GNP'], data['LExpF'])
    significance_level = 0.05  # Set your desired significance level
    if p_value < significance_level:
        result = "rejected"
    else:
        result = "not rejected"
    print("We performed a Pearson’s R correlation for Female Life Expectancy against GNP.")
    print(f"We {result} the null hypothesis at the {significance_level*100}% significance level.")
    print(f"Correlation coefficient (R): {correlation:.2f}")
    print(f"P-value: {p_value:.3f}")
    
    plt.scatter(data['BirthRt'], data['InfMort'])
    plt.xlabel('Birth Rate')
    plt.ylabel('Infant Mortality')
    plt.title('Infant Mortality vs Birth Rate')
    plt.show()
    
main()