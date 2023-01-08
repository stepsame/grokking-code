"""
Array Quadruplet (meaning 4Sum)
Given an unsorted array of integers arr and a number s, write a function findArrayQuadruplet that finds four numbers (quadruplet) in arr that sum up to s.
Your function should return an array of these numbers in an ascending order. If such a quadruplet doesn’t exist, return an empty array.
Note that there may be more than one quadruplet in arr whose sum is s. You’re asked to return the first one you encounter (considering the results are sorted).
Explain and code the most efficient solution possible, and analyze its time and space complexities.
input:  arr = [2, 7, 4, 0, 9, 5, 1, 3], s = 20
output: [0, 4, 7, 9] # The ordered quadruplet of (7, 4, 0, 9)
                     # whose sum is 20. Notice that there
                     # are two other quadruplets whose sum is 20:
                     # (7, 9, 1, 3) and (2, 4, 9, 5), but again you’re
                     # asked to return the just one quadruplet (in an
                     # ascending order)
"""

"""
Solution:
 the array to be sorted, so we do that first.
 Also, it's easier to deal with duplicates if the array is sorted: repeated values are next to each other and easy to skip.
For 3Sum, we enumerate each value in a single loop, and use the two sum method for the rest of the array.
For kSum, we will have k - 2 nested loops to enumerate all combinations of k - 2 values.

We can implement k - 2 loops using a recursion.
 We will pass the starting point and k as the parameters.
  When k == 2, we will call twoSum, terminating the recursion.

Time Complexity:

O(N^3)

Space Complexity:

"""


def two_sum(arr, target):
    num = set()
    for i in arr:
        if target - i in num:
            return [target - i, i]
        num.add(i)
    return []


def k_sum(arr, target, k):
    if len(arr) == 0:
        return []
    if k == 2:
        return two_sum(arr, target)
    if arr[-1] < target // k or arr[0] > target // k:
        return []
    for i in range(len(arr)):
        # if i == 0 or arr[i - 1] != arr[i]:
        sub_k_sum = k_sum(arr[i+1:], target - arr[i], k - 1)
        if sub_k_sum:
            return [arr[i], *sub_k_sum]
    return []


def solution(arr, s):
    # sort
    arr.sort()
    return k_sum(arr, s, 4)


def main():
    assert solution(arr=[2, 7, 4, 0, 9, 5, 1, 3], s=20) == [0, 4, 7, 9]
    assert solution(arr=[1, 0, -1, 0, -2, 2], s=0) == [-2, -1, 1, 2]
    assert solution(arr=[2, 2, 2, 2, 2], s=8) == [2, 2, 2, 2]


if __name__ == '__main__':
    main()
