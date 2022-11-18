"""
Pairs with Specific Difference
Given an array arr of distinct integers and a nonnegative integer k,
write a function findPairsWithGivenDifference that returns an array of all pairs [x,y] in arr, such that x - y = k.
If no such pairs exist, return an empty array.
Note: the order of the pairs in the output array should maintain the order of the y element in the original array.
input:  arr = [0, -1, -2, 2, 1], k = 1
output: [[1, 0], [0, -1], [-1, -2], [2, 1]]
input:  arr = [1, 7, 5, 3, 32, 17, 12], k = 17
output: []

"""

"""
Solution:
Just like two sum. we can use a set to store all number. for every number, check if x + k in set.

Time Complexity: O(N)
Space Complexity: O(N)

"""


def solution(arr, k):
    num = set()
    for i in arr:
        num.add(i)
    result = []
    for i in arr:
        if (i + k) in num:
            result.append([i + k, i])

    return result


def main():
    assert solution(arr=[0, -1, -2, 2, 1], k=1) == [[1, 0], [0, -1], [-1, -2], [2, 1]]
    assert solution(arr=[1, 7, 5, 3, 32, 17, 12], k=17) == []


if __name__ == '__main__':
    main()
