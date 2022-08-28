"""
Problem Statement

Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

Example 1:

Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
Example 2:

Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11

"""

"""
Solution:
We can follow the Two Pointers approach.
We will start with one pointer pointing to the beginning of the array
 and another pointing at the end.
At every step, we will see if the numbers pointed by the two pointers add up to the target sum.
If they do, we have found our pair; otherwise, we will do one of two things:

If the sum of the two numbers pointed by the two pointers is greater than the target sum,
 this means that we need a pair with a smaller sum. So, to try more pairs, we can decrement the end-pointer. 
If the sum of the two numbers pointed by the two pointers is smaller than the target sum,
 this means that we need a pair with a larger sum. So, to try more pairs, we can increment the start-pointer.

Time Complexity:
will be O(N)

Space Complexity:
will be O(1)

"""


def solution(array, target):
    left, right = 0, len(array) - 1
    while left < right:
        two_sum = array[left] + array[right]
        if two_sum == target:
            return [left, right]
        if two_sum < target:
            left += 1
        else:
            right -= 1
    return []


def main():
    assert solution([1, 2, 3, 4, 6], 6) == [1, 3]
    assert solution([2, 5, 9, 11], 11) == [0, 2]


if __name__ == '__main__':
    main()
