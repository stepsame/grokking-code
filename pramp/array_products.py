"""
Array of Array Products
Given an array of integers arr, you’re asked to calculate for each index i the product of all integers except the integer at that index (i.e. except arr[i]).
Implement a function arrayOfArrayProducts that takes an array of integers and returns an array of the products.
input:  arr = [8, 10, 2]
output: [20, 16, 80] # by calculating: [10*2, 8*2, 8*10]
input:  arr = [2, 7, 3, 4]
output: [84, 24, 56, 42] # by calculating: [7*3*4, 2*3*4, 2*7*4, 2*7*3]

"""

"""
Solution:
calculate the total product of the array. for every index just divide it.

specific situation: 1. only 1 number. 2. one zero 3. more than one zero

Time Complexity: O(N) iterator the array.
Space Complexity: O(N)

"""


def solution(arr):
    if len(arr) < 2:
        return []
    zero_count = arr.count(0)
    if zero_count > 1:
        return [0] * len(arr)
    total_product = 1
    for i in arr:
        if i != 0:
            total_product *= i
    result = []
    for i in arr:
        if zero_count == 1:
            if i != 0:
                result.append(0)
            else:
                result.append(total_product)
        else:
            result.append(total_product // i)
    return result


def main():
    assert solution([2, 7, 3, 4]) == [84, 24, 56, 42]
    assert solution([1]) == []
    assert solution([1, 0, 8]) == [0, 8, 0]
    assert solution([1, 0, 0, 1]) == [0, 0, 0, 0]


if __name__ == '__main__':
    main()
