"""
Decode Variations
A letter can be encoded to a number in the following way:
'A' -> '1', 'B' -> '2', 'C' -> '3', ..., 'Z' -> '26'
A message is a string of uppercase letters, and it is encoded first using this scheme. For example, 'AZB' -> '1262'
Given a string of digits S from 0-9 representing an encoded message, return the number of ways to decode it.
input:  S = '1262'
output: 3
explanation: There are 3 messages that encode to '1262': 'AZB', 'ABFB', and 'LFB'.
"""

"""
Solution: We can use dynamic programming to solve this problem.
first, let's think about basic situation. When we only have one number, the ways equal to 1.
Then, we use the function f(i) represent the ways to decode string zero to index i.
if char in index i is zero, then ways is zero, otherwise, this number can used as a single letter, which means f(i) is equal to f(i-1).
And if char i-1 and char i together is between 10 to 26, means this two numbers can used as a leeter, which means f(i) can add up to f(i-2)

Time Complexity: O(N)
Space Complexity: O(N) or O(1)

"""


def solution(s):
    dp = [0 for _ in range(len(s))]
    dp[0] = 1
    for i in range(1, len(s)):
        if s[i] != '0':
            dp[i] += dp[i - 1]
        if 10 <= int(s[i-1:i+1]) <= 26:
            dp[i] += dp[i - 2] if i - 2 > 0 else 1
    return dp[-1]


def main():
    assert solution(s = '1262') == 3


if __name__ == '__main__':
    main()
