"""
Problem Statement

Given a string and a pattern, find the smallest substring in the given string which has all the character occurrences of the given pattern.

Example 1:

Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"
Example 2:

Input: String="aabdec", Pattern="abac"
Output: "aabdec"
Explanation: The smallest substring having all characters occurrences of the pattern is "aabdec"
Example 3:

Input: String="abdbca", Pattern="abc"
Output: "bca"
Explanation: The smallest substring having all characters of the pattern is "bca".
Example 4:

Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern
"""

"""
Solution:
This problem follows the sliding window pattern.
We will use a hashmap to keep the frequency of pattern letter.
1. we add new letter to sliding window. we decrease the frequency at hashmap.
2. if the letter count equal to zero, it means this letter is ok
3. when all letter count equal to zero, then current substring is what we need.
Then we need to shrink the sliding window since we want the smallest substring.
we will stop shrink when one letter count greater than zero.

Time Complexity:
will be O(M+N)

Space Complexity:
will be O(K)

"""


def solution(string, pattern):
    letter_freq = {}
    window_start = 0
    matched_number = 0
    min_length = len(string) + 1
    min_start = 0
    for char in pattern:
        if char not in letter_freq:
            letter_freq[char] = 0
        letter_freq[char] += 1
    for window_end in range(len(string)):
        if string[window_end] in letter_freq:
            letter_freq[string[window_end]] -= 1
            if letter_freq[string[window_end]] == 0:
                matched_number += 1
        while matched_number == len(letter_freq):
            if string[window_start] in letter_freq:
                letter_freq[string[window_start]] += 1
                if letter_freq[string[window_start]] == 1:
                    matched_number -= 1
                    if min_length > window_end - window_start + 1:
                        min_length = window_end - window_start + 1
                        min_start = window_start
            window_start += 1
    if min_length == len(string) + 1:
        return ""
    return string[min_start:min_start + min_length]


def main():
    assert solution(string="aabdec", pattern="abc") == "abdec"
    assert solution(string="aabdec", pattern="abac") == "aabdec"
    assert solution(string="abdbca", pattern="abc") == "bca"
    assert solution(string="adcad", pattern="abc") == ""


if __name__ == '__main__':
    main()
