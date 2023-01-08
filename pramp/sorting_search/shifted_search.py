"""
Shifted Array Search
A sorted array of distinct integers shiftArr is shifted to the left by an unknown offset and you don’t have a pre-shifted copy of it.
For instance, the sequence 1, 2, 3, 4, 5 becomes 3, 4, 5, 1, 2, after shifting it twice to the left.
Given shiftArr and an integer num, implement a function shiftedArrSearch that finds and returns the index of num in shiftArr.
If num isn’t in shiftArr, return -1. Assume that the offset can be any value between 0 and arr.length - 1.
Explain your solution and analyze its time and space complexities.
input:  shiftArr = [9, 12, 17, 2, 4, 5], num = 2 # shiftArr is the
                                                 # outcome of shifting
                                                 # [2, 4, 5, 9, 12, 17]
                                                 # three times to the left
output: 3 # since it’s the index of 2 in arr
"""

"""
Solution:
We could use a modified binary search algorithm.

There are 3 cases:
If the mid element is equal to the target, return the mid index.
If the arr[low] <= the arr[mid], that means the shift pivot is not in the [low, mid] part, so this part is ordered. If arr[low]<= target < arr[mid], the target is in the left part, update the high pointer, otherwise update the low pointer.
If the arr[low] > the arr[mid], that means the shift pivot is in the [low, mid] part, so the [mid, high] part is ordered. If arr[mid]< target <= arr[high], the target is in the right part, update the low pointer, otherwise, update the high pointer.

Time Complexity: O(LogN)
Space Complexity: O(1)

"""


def solution(arr, num):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        # Case 0: we found the target num at index mid
        if arr[mid] == num:
            return mid
        # Case 1: no pivot in low-mid range, nums are ordered
        if arr[low] <= arr[mid]:
            if arr[low] <= num < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # Case 2: pivot in low-mid range, mid-high nums are ordered
        else:
            if arr[mid] < num <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


def main():
    assert solution(arr= [9, 12, 17, 2, 4, 5], num = 2) == 3


if __name__ == '__main__':
    main()
