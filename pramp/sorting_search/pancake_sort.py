"""
Pancake Sort
Given an array of integers arr:
   1. Write a function flip(arr, k) that reverses the order of the first k elements in the array arr.
   2. Write a function pancakeSort(arr) that sorts and returns the input array.
      You are allowed to use only the function flip you wrote in the first step in order to make changes in the array.
input:  arr = [1, 5, 4, 3, 2]
output: [1, 2, 3, 4, 5] # to clarify, this is pancakeSort's output
"""

"""
Solution:
flip method: two pointers.
then find the biggest num index mi, flip first mi elements, so biggest num will be the first element, then we can flip the whole array.
then we can find the next biggest one.

Time Complexity: O(N^2)
Space Complexity: O(1)

"""


def flip(arr, k):
    low, high = 0, k
    while low < high:
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1


def find_max_index(arr, end):
    max_num = 0
    mi = 0
    for i in range(end + 1):
        if arr[i] > max_num:
            max_num = arr[i]
            mi = i
    return mi


def solution(arr):
    n = len(arr)
    for i in range(n - 1, -1, -1):
        mi = find_max_index(arr, i)
        flip(arr, mi)
        flip(arr, i)
        # print(arr)
    return arr


def main():
    assert solution(arr = [1, 5, 4, 3, 2]) == [1, 2, 3, 4, 5]


if __name__ == '__main__':
    main()
