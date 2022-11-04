"""
Find The Duplicates

Given two sorted arrays arr1 and arr2 of passport numbers, implement a function findDuplicates that returns an array of all passport numbers
that are both in arr1 and arr2. Note that the output array should be sorted in an ascending order.

Let N and M be the lengths of arr1 and arr2, respectively. Solve for two cases and analyze the time & space complexities of your solutions:
  M ≈ N - the array lengths are approximately the same
  M ≫ N - arr2 is much bigger than arr1.

input:  arr1 = [1, 2, 3, 5, 6, 7], arr2 = [3, 6, 7, 8, 20]
output: [3, 6, 7]

"""

"""
Solution 1:
if M is equal to N, then we can use two pointers iterator two arrays.
Time Complexity: O(M+N) iterator two arrays
Space Complexity: O(N) for the output array

--------------------
Solution 2:
if M is much bigger than N, then we can iterator the smaller array, then using binary search for the bigger array.

Time Complexity: O(M * log N) binary search is O(log N), for M times
Space Complexity: O(N) for the output array
"""


def solution1(arr1, arr2):
    i, j = 0, 0
    duplicates = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            duplicates.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return duplicates


def solution2(arr1, arr2):
    # let arr2 becomes the smaller one
    if len(arr1) < len(arr2):
        arr1, arr2 = arr2, arr1
    duplicates = []
    last_index = 0
    for i in arr2:
        search_index = binary_search_index(arr1, i, last_index, len(arr1) - 1)
        if search_index != -1:
            duplicates.append(arr1[search_index])
    return duplicates


def binary_search_index(arr, element, start, end):
    i, j = start, end
    # 0, 1, 2, 3
    while i <= j:
        mid = (i + j) // 2
        if arr[mid] == element:
            return mid
        if arr[mid] < element:
            i = mid + 1
        else:
            j = mid - 1
    return -1


def main():
    assert solution1(arr1=[1, 2, 3, 5, 6, 7], arr2=[3, 6, 7, 8, 20]) == [3, 6, 7]
    assert solution2(arr1=[1, 2, 3, 5, 6, 7], arr2=[3, 6, 7, 8, 20]) == [3, 6, 7]


if __name__ == '__main__':
    main()
