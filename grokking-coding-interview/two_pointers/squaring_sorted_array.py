"""
Problem Statement

Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

Example 1:

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
Example 2:

Input: [-3, -1, 0, 1, 2]
Output: [0, 1, 1, 4, 9]

"""

"""
Solution:
An easier approach could be to first find the index of the first non-negative number in the array.
 After that, we can use Two Pointers to iterate the array.
  One pointer will move forward to iterate the non-negative numbers,
  and the other pointer will move backward to iterate the negative numbers.
 At any step, whichever number gives us a bigger square will be added to the output array.
 
 Since the numbers at both ends can give us the largest square,
  an alternate approach could be to use two pointers starting at both ends of the input array.
At any step, whichever pointer gives us the bigger square, we add it to the result array
 and move to the next/previous number according to the pointer.

Time Complexity:
will be O(N)

Space Complexity:
will be O(N)

"""


def solution(array):
    result = [None] * len(array)
    result_index = len(array) - 1
    left, right = 0, len(array) - 1
    while left <= right:
        square_left, square_right = array[left] * array[left], array[right] * array[right]
        if square_left > square_right:
            result[result_index] = square_left
            left += 1
        else:
            result[result_index] = square_right
            right -= 1
        result_index -= 1
    return result


def main():
    assert solution([-2, -1, 0, 2, 3]) == [0, 1, 4, 4, 9]
    assert solution([-3, -1, 0, 1, 2]) == [0, 1, 1, 4, 9]


if __name__ == '__main__':
    main()
