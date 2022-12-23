"""
Problem Statement

Given a string, find the length of the longest substring, which has all distinct characters.

 Example 1:
Input: String="aabccbb"
Output: 3
Explanation: The longest substring with distinct characters is "abc".
Example 2:

Input: String="abbbb"
Output: 2
Explanation: The longest substring with distinct characters is "ab".
Example 3:

Input: String="abccde"
Output: 3
Explanation: Longest substrings with distinct characters are "abc" & "cde".
"""

"""
Solution:
1. This problem can use the sliding window strategy to solve.
We use a hashmap to store char. 
2. add char to the sliding window
3. if new char frequency greater than one, shrink sliding window.
4. current sliding window is ok, compare and store the length.

Time Complexity:
will be O(N)
outer for loop runs for every char
inner while loop will only process every char once.
So time complexity will be O(N + N) asymptotically equivalent to O(N)

Space Complexity:
will be O(K)
store all distinct char.

"""


def find_longest_distinct(string):
    char_freq = {}
    window_start = 0
    max_length = 0
    for window_end in range(len(string)):
        if string[window_end] not in char_freq:
            char_freq[string[window_end]] = 1
        else:
            char_freq[string[window_end]] += 1
        while 1 < char_freq[string[window_end]]:
            char_freq[string[window_start]] -= 1
            if char_freq[string[window_start]] == 0:
                del char_freq[string[window_start]]
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    assert find_longest_distinct("aabccbb") == 3
    assert find_longest_distinct("abbbb") == 2
    assert find_longest_distinct("abccde") == 3


if __name__ == '__main__':
    main()

