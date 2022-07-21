#Binary Search Imlementation ->  Proving a binary search is faster than a normal search
# Jeremy Bargy
#7/21/2022

import random
import time

line_sep = "\n/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n"
# welcome screen
def welcome():

    begin = 'y'

    description ="""
    Binary search is a divide and conquer algorithim that searches through an ordered list faster rather than normally scanning every element in a list one by one.
    Let's search an order list of values sorted from least to greatest. We first look at the middle index. If our search item is equal return the the index of element.
    If it is not we check if it is less than the middle element than if true focus on the first half of the list.
    If it is greater than the middle element than we can focus on the second half of the list.

    Continue with the same divide and conquer method until we find the index of the element we want to search using recursion.

    This makes it much faster to search large lists of data.

    we will use a list of 10,000 random elements on normal and binary search methods to find every element in those lists and time how fast they complete those searches.

    Have you read the instructions and are ready to begin?
    Enter "Y" for yes. Please use capital letters.'
    Or enter "N" for no. Please use capital letters
    """
    
    print(description)
    #loop until user had read instructions
    begin = input('Begin program?\n ')
    while not(begin == 'Y' or begin == 'y') or begin=='' or begin== ' ':
        print('Error: please read the instructions and enter "Y" for yes to begin: \n')
        begin= input('Begin program? \n')


# function to check every element individually on at a time to see if a target is in the list
def normal_search(list, search_target):
    for item in range(len(list)):
        if list[item] == search_target:
            return item
    return -1

# Binary search known as a divide and conquer algorithm
# ASSUME THE LIST WILL BE SORTED
def binary_search(list, search_target, low = None, high = None):
    # set high and low index values
    # low at zero to start the list at the zero index
    if low == None:
        low = 0
    # high at the length of the list minus 1 to to end the list at the last index of the list
    if high== None:
        high = len(list) - 1
    # if the target is not in the list
    if high < low:
        return -1

    # find the midpoint of the list and round down
    midpoint_index = (low + high) // 2

    # check to see if the index is our target, if not decide what to do next based off of it being less or greater than the midpoint index
    if list[midpoint_index] == search_target:
        return midpoint_index
    # if target is less than the mipoint index use recursion to run binary_search
    elif search_target < list[midpoint_index]:
        return binary_search(list, search_target, low, midpoint_index - 1)
    else:
        # if target is greater than the midpoint index use recursion to run binary_search
        return binary_search(list, search_target, midpoint_index + 1, high)

if __name__ == "__main__":

    welcome()

    run_again = 'Y'

    while run_again == "Y":

        # create a list of 10000 values
        length = 10000
        sorted_list = set()
        while len(sorted_list) < length:
            #add rando numbers to list from -30000 to 30000
            sorted_list.add(random.randint( -3 * length, 3 * length))
        sorted_list = sorted(list(sorted_list))

        print(line_sep)

        # TIME TRIAL FOR NORMAL SEARCH
        start = time.time()
        for target in sorted_list:
            normal_search(sorted_list, target)
        end = time.time()
        # print results
        print("Normal search time: ", (end-start)/length, "seconds\n")

        # TIME TRAIL FOR BINARY SEARCH
        start = time.time()
        
        for target in sorted_list:
            binary_search(sorted_list, target)
        end = time.time()

        print("Binary search time: ", (end-start)/length, "seconds")

        print(line_sep)

        # Ask user to run progra again
        print("Would you like to see binary search win again?")
        run_again = input('Press "Y" to run again \n or "N" to end the program: \n')
        while not(run_again == 'Y' or run_again=='y' or run_again=='N' or run_again=='n') or run_again=='' or run_again== ' ':
            print('\nError: please "Y" for yes to restart:')
            print('Or enter "N" to end the program: ')
            run_again= input('Restart program? \n')
        run_again = run_again.upper()

    print("\n\n---------------------------------------") 
    print("----THANKS FOR USING THIS PROGRAM------")
    print("---------------GOODBYE ! --------------")
    print("---------------------------------------") 

    
