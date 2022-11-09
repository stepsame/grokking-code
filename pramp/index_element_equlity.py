"""
Array Index & Element Equality
Given a sorted array arr of distinct integers, write a function indexEqualsValueSearch that returns the lowest index i for which arr[i] == i.
Return -1 if there is no such index. Analyze the time and space complexities of your solution and explain its correctness.
input: arr = [-8,0,2,5]
output: 2 # since arr[2] == 2
input: arr = [-1,0,3,6]
output: -1 # since no index in arr satisfies arr[i] == i.
"""

"""
Solution:
We can use binary search to search the array.
if we found a match, then we need check the item before to find the first match.

Time Complexity: O(logN) worst case: O(N)
Space Complexity: O(1)

"""


def solution(arr):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if mid == arr[mid]:
            # find the first one
            while mid > 0 and mid - 1 == arr[mid - 1]:
                mid -= 1
            return mid
        if mid > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def main():
    assert solution([-8,0,2,5]) == 2
    assert solution([-1,0,3,6]) == -1


if __name__ == '__main__':
    main()
