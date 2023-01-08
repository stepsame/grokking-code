"""
Absolute Value Sort
Given an array of integers arr, write a function absSort(arr), that sorts the array according to the absolute values of the numbers in arr.
If two numbers have the same absolute value, sort them according to sign, where the negative numbers come before the positive numbers.
Examples:
input:  arr = [2, -7, -2, -2, 0]
output: [0, -2, -2, 2, -7]

"""

"""
Solution:
quick sort and compare number with its absolute value.

Time Complexity: O(NlogN)
Space Complexity: O(1)
"""


def compare(a, b):
    if abs(a) < abs(b):
        return -1
    if abs(a) == abs(b) and a < b:
        return -1
    if a == b:
        return 0
    return 1


# Function to find the partition position
# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot
def partition(array, low, high):
    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements compare each element with pivot
    for j in range(low, high):
        if compare(array[j], pivot) == -1:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            array[i], array[j] = array[j], array[i]

    # Swap the pivot element with the greater element specified by i
    array[i + 1], array[high] = array[high], array[i + 1]

    # Return the position from where partition is done
    return i + 1


def quick_sort(array, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quick_sort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quick_sort(array, pi + 1, high)

    return array


def solution(arr):
    return quick_sort(arr, 0, len(arr) - 1)


def main():
    result = solution(arr=[2, -7, -2, -2, 0])
    print(result)
    assert result == [0, -2, -2, 2, -7]


if __name__ == '__main__':
    main()
