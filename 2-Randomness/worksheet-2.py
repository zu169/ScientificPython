import numpy as np

def question1():
    print("Question 1")
    #for loop to print out 5 random numbers fro 1 to 10
    print("For loop: ")
    for i in range(5):
        print(np.random.randint(1,11))
    #list containing 5 random integers between 1 and 10
    rand_ints = [np.random.randint(1,11) for i in range(5)]
    print("\nList comprehension: ", rand_ints)
    #list created using numpy.array function
    arr_np = np.array(np.random.randint(1,11,5))
    print("\nNumpy Array: ", arr_np)

def question2():
    print("\nQuestion 2: ")
    print("6 sided die: ")
    rolls = np.array(np.random.randint(1,7,10000))    
    counts = np.bincount(rolls)
    sixdie = {1:counts[1]/100, 2:counts[2]/100, 3:counts[3]/100, 4:counts[4]/100, 5:counts[5]/100, 6:counts[6]/100}
    print("Percentage Occurrence: ", sixdie)
   
def checkWinStage(num_matches, bonus):
    if num_matches == 6:
        return 6
    elif num_matches == 5 and bonus == True:
        return 0
    elif num_matches == 2:
        return 2
    elif num_matches == 1 or num_matches == 0:
        return 1
    else: return num_matches
    
def lotto(entry):
    #print("\nEntry Numbers: ", entry)
    win = np.array(np.random.randint(1,60,6))
    #print("\nLottery Numbers: ", win)
    bonus_ball = np.array(np.random.randint(1,60,1))
    #print("\nBonus Ball: ", bonus_ball) 
    
    num_matches = len(set(entry).intersection(win))
    bonus = True | len(set(entry).intersection(bonus_ball)) == 1
    return checkWinStage(num_matches, bonus)
    
def question3():
    print("\nQuestion 3: ")
    print("Lotto Game: ")
    #entry = np.array(np.random.randint(1,60,6))
    entry = [3,13,46,34,28,50]
    
    prizes = {0:0,1:0,2:0,3:0,4:0,5:0,6:0}
    chance = []
    
    for i in range(104):
        prize = lotto(entry)
        prizes[prize] += 1
        
    for i in range(6):
        chance.append(round(prizes[i]/104,2) *100)

    print("\nKey: \n 0 is Match 5+1,\n 1 is No Prize,\n 2 is Lucky Dip,\n 3 is Match 3,\n 4 is Match 4,\n 5 is Match 5,\n 6 is Jackpot")
    print(prizes)
    print("\n", chance[1], "% Loss Percentage")
    chance.remove(chance[1])
    print("\n", sum(chance), "% Win Percentage" )
    
   

question1()
question2()
question3()