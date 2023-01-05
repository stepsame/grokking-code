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
Solution 1(division):
calculate the total product of the array. for every index just divide it.

specific situation: 1. only 1 number. 2. one zero 3. more than one zero

Time Complexity: O(N) iterator the array.
Space Complexity: O(N)

Solution 2(without division):

Every product contains two parts: the prefix products and the suffix products.

First, we can initialize the result array ans of length equal to nums filled with 1.

Then, we traverse the array once. for every i,
we calculate the prefix products before i and store it in the result array.
so result[i] = result[i - 1] * num[i - 1]

Then, we traverse the aray again in reverse order. 
for every i, we calculate the suffix products after i, 
so suffix_products = last_suffix_products * num[i + 1]
then multiply it with the current value result[i].


Time Complexity: O(N) 

Because we traverse the array twice, the time complexity is linear time.

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


def solution_2(arr):
    n = len(arr)
    if n < 2:
        return []
    result = [1] * n
    for i in range(1, n):
        result[i] = result[i - 1] * arr[i - 1]
    suffix_products = 1
    for i in range(n - 2, -1, -1):
        suffix_products = suffix_products * arr[i + 1]
        result[i] *= suffix_products
    return result


def main():
    assert solution_2([2, 7, 3, 4]) == [84, 24, 56, 42]
    assert solution_2([1]) == []
    assert solution_2([1, 0, 8]) == [0, 8, 0]
    assert solution_2([1, 0, 0, 1]) == [0, 0, 0, 0]


if __name__ == '__main__':
    main()
