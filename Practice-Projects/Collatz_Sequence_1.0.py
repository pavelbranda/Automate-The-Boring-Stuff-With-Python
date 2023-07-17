
def collatz(number):
    while number != 1:      # While loop that continues until 'number' becomes 1 (if 'number' == 1 condition = False - loop terminates)
        if number % 2 == 0: 
            number = number // 2    # even number
        else:
            number = 3 * number + 1 # odd number
        print(number)

valid_input = True # Default state of variable valid_input (for ExceptionHandling)

while valid_input: 
    try:
        number = int(input('Enter number:\n')) # Outside the function code
        valid_inpput = False
        break
    except ValueError:
        print('Please enter a number.')
        valid_input = True
    
collatz(number) # Calls the 'collatz' Func. with the user-input as and Argument

# one-liner: >>> collatz(int(input('Enter number:')))
# readability and maintainability are highly valued in Python programming
# Remember, the goal is to write code that is easy to understand, debug, and maintain, rather than purely focusing on reducing the number of lines

'''
TEST:
# Currently not working with negative numbers/zero (e.g. -4/0) - infinite loop of negative numbers/zeros
'''
