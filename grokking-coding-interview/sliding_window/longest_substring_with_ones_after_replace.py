"""
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

Example 1:

Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
Example 2:

Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
"""

"""
Solution:
This problem follows the sliding window pattern.
We will use a hashmap to count the frequency of the letter.
We will also keep track of the maximum repeating 1 in any sliding window.

1. We add new letter to sliding window, to store max repeat number.
2. if current sliding window length is greater than max repeat number plus k, then we need to shrink the sliding window.
3. current sliding window is ok or not. but we can be sure if sliding window length greater than old, then it is ok.

Time Complexity:
will be O(N)

Space Complexity:
will be O(1)
"""


def solution(array, k):
    window_start = 0
    # letter_freq = {}
    one_freq = 0
    max_length = 0
    max_repeat = 0
    for window_end in range(len(array)):
        current = array[window_end]
        if current == 1:
            one_freq += 1
        max_repeat = max(max_repeat, one_freq)
        if window_end - window_start + 1 > max_repeat + k:
            if array[window_start] == 1:
                one_freq -= 1
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    assert solution([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2) == 6
    assert solution([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3) == 9


if __name__ == '__main__':
    main()
