import pandas as pd
from scipy.stats import chi2_contingency

# Load the CSV file into a pandas DataFrame
data = pd.read_csv('HairEyeColour.csv')

# Display the DataFrame
print("Dataframe:", data)

# Question 2 and 3

# Create a contingency table using pandas crosstab function
contingency_table = pd.crosstab(data["Hair Colour"], data["Eye Colour"])

# Calculate the row and column totals
row_totals = contingency_table.sum(axis=1)

# Display the contingency table
column_totals = contingency_table.sum()
print("Contingency Table:", contingency_table)

# Calculate the total number of subjects
total_subjects = contingency_table.values.sum()

# Calculate the expected number of subjects in each cell assuming independence
expected_table = pd.DataFrame(
    index=contingency_table.index, columns=contingency_table.columns
)

for hair_color in contingency_table.index:
    for eye_color in contingency_table.columns:
        expected_freq = (
            row_totals[hair_color] * column_totals[eye_color]
        ) / total_subjects
        expected_table.loc[hair_color, eye_color] = expected_freq

# Display the expected table
print("\nExpected Table (assuming independence):")
print(expected_table)

# Question 4 is the same as 5 but in the lectures they must show you another way to do it

# Question 5

# Calculate the chi-squared statistic, p-value, degrees of freedom, and expected frequencies
chi2, p_value, dof, expected_freq = chi2_contingency(contingency_table)

# Display the chi-squared statistic, p-value, degrees of freedom, and expected frequencies
print("Chi-squared statistic:", chi2)
print("p-value:", p_value)
print("Degrees of freedom:", dof)
print("Expected frequencies:")
print(
    pd.DataFrame(
        expected_freq, index=contingency_table.index, columns=contingency_table.columns
    )
)

""" Question 6
Hypothesis (alternative hypothesis):
There is an association between hair color and eye color.

Null Hypothesis:
There is no association between hair color and eye color.

In statistical terms, the null hypothesis assumes that the variables (hair color and eye color) are independent, meaning that
the distribution of one variable is not affected by the other variable. The alternative hypothesis suggests that there is a
relationship or association between the variables, indicating that the distribution of one variable is dependent on the other variable.
The chi-squared test is used to assess the evidence against the null hypothesis and determine whether the observed association
between hair color and eye color is statistically significant. 
"""

# Question 7

# Set the significance level (alpha)
alpha = 0.05

# Check if the p-value is less than the significance level
if p_value < alpha:
    print(
        "Eye Colour is significantly related to Hair Colour (reject the null hypothesis)."
    )
else:
    print(
        "Eye Colour is not significantly related to Hair Colour (fail to reject the null hypothesis)."
    )

# Display the p-value
print("p-value:", p_value)
