"""
Problem Statement

Given an array of sorted numbers, remove all duplicate number instances from it in-place, such that each element appears only once. The relative order of the elements should be kept the same and you should not use any extra space so that that the solution have a space complexity of O(1).

Move all the unique elements at the beginning of the array and after moving return the length of the subarray that has no duplicate in it.

Example 1:

Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
Example 2:

Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].
"""

"""
Solution:
we will keep one pointer for iterating the array and one pointer for placing the next non-duplicate number.
 So our algorithm will be to iterate the array and whenever we see a non-duplicate number
  we move it next to the last non-duplicate number we’ve seen.

Time Complexity:
will be O(N)

Space Complexity:
will be O(1)

"""


def solution(array):
    current_distinct_index = 0
    i = 1
    while i < len(array):
        if array[current_distinct_index] != array[i]:
            current_distinct_index += 1
            array[current_distinct_index] = array[i]
        i += 1
    return current_distinct_index + 1


def main():
    assert solution([2, 3, 3, 3, 6, 9, 9]) == 4
    assert solution([2, 2, 2, 11]) == 2


if __name__ == '__main__':
    main()
