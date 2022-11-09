"""
Getting a Different Number
Given an array arr of unique nonnegative integers, implement a function getDifferentNumber that finds the smallest nonnegative integer that is NOT in the array.
input:  arr = [0, 1, 2, 3]
output: 4
input:  arr = [0, 2, 3]
output: 1
"""

"""
Solution:
1. first solution: binary search.
2. second solution: using a set/dict to store all number.
3. third solution: we can use the arr's index as the set.
we can iterate the arr, if current number is bigger than the length, we can ignore. 
if current number is smaller than the length, we put this number to the number index, and swap that number to current position.
the first one not equal to index is the answer. Otherwise, we return n.

Time Complexity: O(N)
Space Complexity: O(1)

"""


def solution(arr):
    n = len(arr)
    for i in range(n):
        if i != arr[i] and arr[i] < n:
            arr[arr[i]], arr[i] = arr[i], arr[arr[i]]
    print(arr)
    for i in range(n):
        if i != arr[i]:
            return i
    return n


def main():
    assert solution([100, 101, 108, 109]) == 0
    assert solution([100, 101, 108, 109]) == 0
    assert solution([0, 1, 2, 3]) == 4
    assert solution([0, 2, 3]) == 1


if __name__ == '__main__':
    main()
