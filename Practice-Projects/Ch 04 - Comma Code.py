
def format_list(items): # Define a function named format_list that takes a single parameter called 'items'
    if not items:  # Check if the list 'items' is empty, code immediately exits the function and return an empty string ('')
        return ''  # This means that if the list is empty, the function will not execute any further code and will simply return an empty string as the result
    # Check if the list 'items' contains only one element, if so, return that element as a string. 
    if len(items) == 1:      # Check if the list contains exactly one element
        return str(items[0]) # If there is only one element in a list 'items'- FUNC immediately returns that element as a string

    # If there are more than one element in the list, execute the following steps:
    formatted_items = [str(item) for item in items[:-1]] # Convert each element in 'items' list to a string and store them in a new list 'formatted_items' - [:1] = Slice notation - exclude the last element from the 'items' list  
    # print(formatted_items) # for Debugging only
    
    formatted_items.append('and ' + str(items[-1])) # Add the last element of 'items' (converted to a string) with the string 'and' in front of it to 'formatted_items'
    # print(formatted_items) # for Debugging only 

    result = '' # Initialize an empty string named 'result'

    for i in range(len(formatted_items)): # Loop through each element (indices) in 'formatted_items' (*formatted_items = items - cats)
        result += formatted_items[i]      # Append the current element from 'formatted_items' to the 'result' string
        if i != len(formatted_items) - 1: # Check if the current element is not the last element in 'formatted_items'
            result += ', '                # If it's not the last elemetn - add a comma and a space to the 'result' string
            
    
    return result # Return the final 'result' string from the FUNC

spam = ['apples', 'bananas', 'tofu', 'cats'] # Create a list 'spam' - assigns it foru string values
'''TESTS:
spam = []       # Test - empty List
spam = ['pepa'] # Test - just one value in a List
'''

print(format_list(spam)) # Call the 'format_list' function with 'spam' as an argument and print the returned result
