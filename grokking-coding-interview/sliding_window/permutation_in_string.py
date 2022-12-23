"""
Problem Statement

Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

abc
acb
bac
bca
cab
cba
If a string has ‘n’ distinct characters, it will have n!n! permutations.

Example 1:

Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.
Example 2:

Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.
Example 3:

Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.
Example 4:

Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.
"""

"""
Solution:
This problem follows the sliding window pattern.
If a string contains a permutation for a pattern, it must contains a substring the freq hashmap is same with the pattern.

1. we add char to sliding window. we keep track of the char frequency hashmap.
2. if the length of the sliding window greater than pattern, we shrink it.
3. we check if current sliding window hashmap equal to the pattern frequency hashmap.

Time Complexity:
will be O(M+N) M is length of pattern, N is length of string

Space Complexity:
will be O(M). In the worst case, we will store all characters.

"""


def solution(string, pattern):
    char_freq = {}
    for c in pattern:
        if c not in char_freq:
            char_freq[c] = 1
        else:
            char_freq[c] += 1
    window_start = 0
    matched = 0
    for window_end in range(len(string)):
        char = string[window_end]
        if char in char_freq:
            char_freq[char] -= 1
            if char_freq[char] == 0:
                matched += 1
        if window_end - window_start + 1 > len(pattern):
            if string[window_start] in char_freq:
                char_freq[string[window_start]] += 1
                if char_freq[string[window_start]] == 1:
                    matched -= 1
            window_start += 1
        if window_end - window_start + 1 == len(pattern):
            if len(char_freq) == matched:
                return True

    return False


def main():
    assert solution(string="oidbcaf", pattern="abc") is True
    assert solution(string="odicf", pattern="dc") is False
    assert solution(string="bcdxabcdy", pattern="bcdyabcdx") is True
    assert solution(string="aaacb", pattern="abc") is True


if __name__ == '__main__':
    main()
