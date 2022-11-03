"""
Move Zeros To End
Given a static-sized array of integers arr, move all zeroes in the array to the end of the array.
You should preserve the relative order of items in the array.
We should implement a solution that is more efficient than a naive brute force.
input:  arr = [1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]
output: [1, 10, 2, 8, 3, 6, 4, 5, 7, 0, 0, 0, 0, 0]

"""

"""
Solution:

We use a pointer point first zero index. all numbers before pointer is non-zero.
iterator the array, if we met a non-zero number, we swap this number and pointer number, and then move pointer to next.

Time Complexity:
O(N) N is length of the array

Space Complexity:
O(1) constant space

"""


def solution(arr):
    first_zero = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[first_zero] = arr[first_zero], arr[i]
            first_zero += 1
    print(arr)
    return arr


def main():
    assert solution([1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]) == [1, 10, 2, 8, 3, 6, 4, 5, 7, 0, 0, 0, 0, 0]


if __name__ == '__main__':
    main()
