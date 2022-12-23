"""
Problem 1: Given an unsorted array of numbers and a target ‘key’, remove all instances of ‘key’ in-place and return the new length of the array.

Example 1:

Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
Output: 4
Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9].
Example 2:

Input: [2, 11, 2, 2, 1], Key=2
Output: 2
Explanation: The first two elements after removing every 'Key' will be [11, 1].
"""

"""
Solution:
We can follow a two-pointer approach and shift numbers left upon encountering the ‘key’.

Time Complexity:
will be O(N)

Space Complexity:
will be O(1)

"""


def solution(array, key):
    current_index = -1
    i = 0
    while i < len(array):
        if key != array[i]:
            current_index += 1
            array[current_index] = array[i]
        i += 1
    return current_index + 1


def main():
    assert solution([3, 2, 3, 6, 3, 10, 9, 3], key=3) == 4
    assert solution([2, 11, 2, 2, 1], key=2) == 2


if __name__ == '__main__':
    main()
