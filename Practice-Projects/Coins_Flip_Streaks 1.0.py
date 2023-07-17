import random


numberOfStreaks = 0 # variable declaration

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values
    coins_list = []
    for i in range(100):
        coins_list.append(random.randint(0,1))
    # print(coins_list) # Debugging - prints list of 100 coints for each of 10,000 experiments
    # does not matter if it is 0 or 1, H or T, peas or lentils. I am going to check if there is multiple 0 or 1 in a row


    # Code that checks if there is a streak of 6 heads or tails in a row
    current_streak = 1 # streaks start at 1
    for i in range(1, len(coins_list)):      # start at index 1, since you are looking at the previous one
        if coins_list[i] == coins_list[i-1]: # checks if current list item is the same as before 
            current_streak += 1
        else:
            current_streak = 1
        
        if current_streak == 6:
            numberOfStreaks += 1
            # print(numberOfStreaks) # Debugging - prints an overall streak score - always +1 if streak is found in current list 
            break # break after finding one 6-streak, since you don't want to double count in the same series of 100-flips
        
print('Chance of streaks: %s%%' % (numberOfStreaks / 100))

'''
TESTS:
???
'''

