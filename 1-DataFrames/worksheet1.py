import pandas as pd
import matplotlib.pyplot as plt

def fb_csv():
    df = pd.read_csv('GOOGL_2021-22.csv', index_col='date', parse_dates=True)
    fb_df = pd.read_csv('FB_2021-22.csv', index_col='date', parse_dates=True)
    
    #new dataframe with only close for both companies
    close_df = pd.concat({'Alphabet Inc.' : df['close'], 'Facebook' : fb_df['close']}, axis=1)
    
    #plot on one graph
    close_df.plot()
    #label the graph
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.title('Closing Price of Alphabet Inc. and Facebook')
    plt.legend(loc='upper right')
    plt.show()
    

def googl_csv():
    #read data from the csv file
    df = pd.read_csv('GOOGL_2021-22.csv', index_col='date', parse_dates=True)
    #display the data from the csv
    print("Initial Alphabet Inc. Dataframe: \n")
    print(df.describe())
    #plot the volume data from the csv
    df['volume'].plot()
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.show()
    
    #slice the data to keep only columns from open price to close price (inclusive)
    sliced_df = df.loc[:, 'open':'close']
    print("\nAlphabet Inc. Dataframe only showing columns open to close: \n")
    print(sliced_df.describe())
    
    #create new column to display the change between the open and close columns
    df['change'] = df['close'] - df['open']
    #plot the change data from the csv
    df['change'].plot()
    plt.xlabel('Date')
    plt.ylabel('Change')
    plt.title('Change of the closing price from the opening price')
    plt.show()
    
    #show the final changes to the dataframe
    print('\nFinal Alphabet Inc. Dataframe: \n')
    print(df.describe())
    
def brain_csv():
    brain_df = pd.read_csv('brain.csv')
    print("\nIntitial Brain Dataframe: \n")
    print(brain_df.describe())
    
    #group data by the data column
    grouped_df = brain_df.groupby('Gender')
    print("\nBrain Dataframe grouped by Gender: \n")
    print(grouped_df.describe())
  
    #display the data in the form of a boxplot
    grouped_df.boxplot(column=['Height', 'Weight'])
    plt.show()
    
    #plot and a display a scatter graph of the height and weight
    for name, group in grouped_df:
        plt.scatter(x=group['Height'], y=group['Weight'], label=name)
    plt.xlabel('Weight')
    plt.ylabel('Height')
    plt.title('Weight vs. Height by Gender')
    plt.legend()
    plt.show()
    
#question 1
googl_csv()
#extra work
fb_csv()
#question 2
brain_csv()