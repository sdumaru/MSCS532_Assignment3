""" Understanding Randomized Quicksort """

import timeit
import random
from memory_profiler import profile

def partition(array, first, last):
    """ Split the array into 2 parts based on the pivot element """
    pivot = array[last]                                                         # Select a pivot element to compare with other elements
    low_index = first - 1                                                       # Select the highest index of opposite side of pivot

    # Traverse through the array from beginning till end except the pivot element
    # If the element is smaller than pivot then we swap it the left side,
    # and save the index for pivot element
    for index in range(first, last):
        if array[index] <= pivot:
            low_index += 1
            array[low_index], array[index] = array[index], array[low_index]

    # Once the traversal ends, pivot element is added on the last index
    # which separated smaller and larger element
    array[low_index + 1], array[last] = array[last], array[low_index + 1]

    return (low_index + 1)                                                      # Return the new index of pivot element

def randomized_partition(array, first, last):
    """ Function to select a random pivot element and do partition """
    random_pivot = random.randint(first, last)                                  # Select pivot randomly
    array[last], array[random_pivot] = array[random_pivot], array[last]         # Swap last element with random pivot element
    return partition(array, first, last)                                        # Apply normal partition function

# @profile
def randomized_quicksort(array, first, last):
    """ Function that will take array, leftmost index and rightmost index of array 
        as an input and return sorted array """
    if len(array) == 0:                                                         # Return array if it's empty
        return array

    if first < last:
        partition_index = randomized_partition(array, first, last)

        # Divide-and-Conquer method
        randomized_quicksort(array, first, partition_index - 1)
        randomized_quicksort(array, partition_index + 1, last)
    return array

def print_execution_times(array_name):
    """ Function to print execution times """
    timer_stmt = '''randomized_quicksort({0}, 0, len({0}) - 1)'''
    times = timeit.repeat(stmt=timer_stmt.format(array_name), repeat=5, number=10000, globals=globals())
    print('total execution time: ' + str(min(times)))

def huge_random_array():
    """ Function to return huge number of random integers for testing purpose """
    array = []
    max_numbers = 500
    for i in range(max_numbers):
        array.append(random.randint(0, max_numbers))
    return array

# Testing performance of algorithms on these arrays
empty_array = []
randomized_array = [23, 65, 98, 1, 36, 47, 76, 28, 83, 15]
sorted_array = [1, 15, 23, 28, 36, 47, 65, 76, 83, 98]
reversed_sorted_array = [98, 83, 76, 65, 47, 36, 28, 23, 15, 1]
repeated_elements_array = [23, 56, 23, 84, 56, 23, 56, 84, 23, 84]

# PRINT SORTED ARRAYS
# print(randomized_quicksort(empty_array, 0, len(empty_array) - 1))
# print(randomized_quicksort(randomized_array, 0, len(randomized_array) - 1))
# print(randomized_quicksort(sorted_array, 0, len(sorted_array) - 1))
# print(randomized_quicksort(reversed_sorted_array, 0, len(reversed_sorted_array) - 1))
# print(randomized_quicksort(repeated_element_array, 0, len(repeated_elements_array) - 1))

# Print execution times for the array
print("EMPTY ARRAY", end = " ")
print_execution_times(empty_array)

print("RANDOM ARRAY", end = " ")
print_execution_times(randomized_array)

print("SORTED ARRAY", end = " ")
print_execution_times(sorted_array)

print("REVERSED SORTED ARRAY", end = " ")
print_execution_times(reversed_sorted_array)

print("REPEATED ELEMENTS ARRAY", end = " ")
print_execution_times(repeated_elements_array)

print("HUGE RANDOM ARRAY", end = " ")
print_execution_times(huge_random_array())
