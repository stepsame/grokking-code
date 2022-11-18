"""
Smallest Substring of All Characters (Minimum Window Substring)
Given an array of unique characters arr and a string str, Implement a function getShortestUniqueSubstring that finds the smallest substring of str
containing all the characters in arr. Return "" (empty string) if such a substring doesn’t exist.
input:  arr = ['x','y','z'], str = "xyyzyzyx"
output: "zyx"
"""

"""
Solution:
Sliding windows method.
using a dict to store char and count.
expand the sliding window, if meet all char, then we can shrink the window from left. and record the minimum length and index.

Time Complexity: O(N)
Space Complexity: O(M)

"""


def solution(arr, string):
    char_count = {char: 0 for char in arr}
    meet_count = 0
    i = 0
    min_length = len(string)
    result_start, result_end = 0, 0
    for j in range(len(string)):
        char = string[j]
        if char in char_count:
            if char_count[char] == 0:
                meet_count += 1
            char_count[char] += 1

        if meet_count == len(arr):
            # shrink
            while i <= j:
                # record
                if j - i + 1 < min_length:
                    min_length = j - i + 1
                    result_start = i
                    result_end = j

                # shrink
                if string[i] in char_count:
                    char_count[string[i]] -= 1
                    if char_count[string[i]] == 0:
                        meet_count -= 1
                i += 1
                if meet_count < len(arr):
                    break

    return string[result_start : result_end+1]


def main():
    assert solution(arr = ['x','y','z'], string = "xyyzyzyx") == "zyx"


if __name__ == '__main__':
    main()
