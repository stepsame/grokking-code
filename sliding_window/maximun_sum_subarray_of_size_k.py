"""
Maximum Sum Subarray of Size K (easy)
Problem Statement:
Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:

Input: [2, 3, 4, 1, 5], k=2
Output: 7
Explanation: Subarray with maximum sum is [3, 4].

"""


def find_max(k, array):
    """
    Time Complexity: O(N)
    Space Complexity: constant space O(1)
    """
    max_sum, window_sum, window_start = 0.0, 0.0, 0
    for window_end in range(len(array)):
        window_sum += array[window_end]
        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= array[window_start]
            window_start += 1
    return max_sum


def main():
    assert find_max(3, [2, 1, 5, 1, 3, 2]) == 9
    assert find_max(2, [2, 3, 4, 1, 5]) == 7


if __name__ == '__main__':
    main()

