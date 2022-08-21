"""
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

Example 1:

Input: String="aabccbb", k=2
Input: String="aabcdbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
Example 2:

Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
Example 3:

Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".

"""
"""
Solution:
This problem follows sliding window pattern.
We can use a hashmap to count the frequency of each letter.
We will also keep track of the count of the maximum repeating letter in any window 
(let’s call it max_repeat).
1. we add new letter to sliding window
2. if sliding window length greater than max repeating letter + k, then we need shrink the sliding window
3. current sliding window is ok or not ok, we compare and store maximum letters

Time Complexity:
O(N)

Space Complexity:
O(1)
"""


def find_longest(k, string):
    window_start = 0
    max_repeating = 0
    char_frequency = {}
    max_length = 0
    for window_end in range(len(string)):
        if string[window_end] not in char_frequency:
            char_frequency[string[window_end]] = 1
        else:
            char_frequency[string[window_end]] += 1
        max_repeating = max(max_repeating, char_frequency[string[window_end]])
        if window_end - window_start + 1 > max_repeating + k:
            char_frequency[string[window_start]] -= 1
            if char_frequency[string[window_start]] == 0:
                del char_frequency[string[window_start]]
            window_start += 1
        print('ll', char_frequency, string[window_end])
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    assert find_longest(2, 'aabccbb') == 5
    assert find_longest(1, 'abbcb') == 4
    assert find_longest(1, 'abccde') == 3
    assert find_longest(2, 'aabcdbb') == 5
    assert find_longest(2, 'aaaaa') == 5


if __name__ == '__main__':
    main()
