"""
Problem Statement

Given a string, find the length of the longest substring in it with no more than K distinct characters.

You can assume that K is less than or equal to the length of the given string.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
Example 2:

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".
Example 3:

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
"""

"""
new words:
hashmap
constitute
stepwise fashion
decrement
asymptotically equivalent
"""

"""
solution:
1. we can use the sliding window strategy
    and using a hashmap to store the characters and the hashmap key's length is the distinct character number
2. add a new character to the sliding window
3. if distinct num is greater than k, then continue to shrink the sliding window
4. current window is ok, compare and store the max length
5. add a new character again like steps 2 to 4

Time Complexity:
will be O(N), where N is the number of characters in the string.

outer for loop runs for all characters
inner while loop processes each character once
O(N + N) which is asymptotically equivalent to O(N)

Space Complexity:
will be O(K) 
as we will be storing a maximum of K + 1 characters in the hashmap

"""


def find_longest(k, string):
    longest_length = 0
    window_start = 0
    frequency = {}
    for window_end in range(len(string)):
        # add
        if string[window_end] in frequency:
            frequency[string[window_end]] += 1
        else:
            frequency[string[window_end]] = 1
        while len(frequency) > k:
            # shrink
            frequency[string[window_start]] -= 1
            if frequency[string[window_start]] == 0:
                del frequency[string[window_start]]
            window_start += 1
        longest_length = max(longest_length, window_end - window_start + 1)
    return longest_length


def main():
    assert find_longest(2, "araaci") == 4
    assert find_longest(1, "araaci") == 2
    assert find_longest(3, "cbbebi") == 5


if __name__ == '__main__':
    main()
