"""
Basic Regex Parser
Implement a regular expression function isMatch that supports the '.' and '*' symbols. The function receives two strings - text and pattern -
and should return true if the text matches the pattern as a regular expression.
In case you aren’t familiar with regular expressions, the function determines if the text and pattern are the equal, where the '.'
is treated as a single a character wildcard (see third example), and '*' is matched for a zero or more sequence of the previous letter.
input:  text = "aa", pattern = "a"
output: false
input:  text = "aa", pattern = "aa"
output: true
input:  text = "abc", pattern = "a.c"
output: true
input:  text = "abbb", pattern = "ab*"
output: true
input:  text = "acd", pattern = "ab*c."
output: true
"""

"""
Solution:
If there were no asterisk, the problem would be easier
 - we simply check from left to right if each character of the text matches the pattern.
When a star is present, we may need to check many different suffixes of the text and see if they match the rest of the pattern.
A recursive solution is a straightforward way to represent this relationship.

If a asterisk is present in the pattern, it will be in the second position pattern[1]. 
Then, we may ignore this part of the pattern, or delete a matching character in the text. 
If we have a match on the remaining strings after any of these operations, then the initial inputs matched.

Time Complexity:
a worst case pattern would consist of many .* to create as many diverging paths as possible,
 with a final text character which does not match the pattern.
Text: aaaaaaaaaab
Pattern: a*a*a*a*a*a*a*a*a*a*

when performing recursion, the algorithm will perform a depth first search on a tree. so the sub-problem number will be the nodes number.
the bottom level's dpeth which is (T+P/2). and the bottom level's nodes number is 2^(T+P/2)
O(2^(T+P/2))

Space Complexity: the same as time complexity, O(2^(T+P/2))

"""

"""
Solution 2:
As the problem has an optimal substructure, it is natural to cache intermediate results.
 We ask the question dp(i, j): does text[i:] and pattern[j:] match? We can describe our answer in terms of answers to questions involving smaller strings.

We proceed with the same recursion as in Approach 1, except because calls will only ever be made to match(text[i:], pattern[j:]),
 we use dp(i, j) to handle those calls instead, saving us expensive string-building operations and allowing us to cache the intermediate results.
 
Time Complexity: Let T,P be the lengths of the text and the pattern respectively.
 The work for every call to dp(i, j) for i=0,...,T; j=0,...,P is done once, and it is O(1) work.
  Hence, the time complexity is O(TP).

Space Complexity: The only memory we use is the O(TP) boolean entries in our cache. Hence, the space complexity is O(TP).
"""


# recursive
def is_match_helper(text, pattern):
    if not pattern:
        return not text
    first_match = text and (pattern[0] == text[0] or pattern[0] == '.')
    if len(pattern) >= 2 and pattern[1] == '*':
        # two cases
        return is_match_helper(text, pattern[2:]) or (first_match and is_match_helper(text[1:], pattern))
    return first_match and is_match_helper(text[1:], pattern[1:])


# dp top-down
def is_match_helper_dp(text, pattern):
    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if j == len(pattern):
            memo[(i, j)] = i == len(text)
        else:
            first_match = i < len(text) and (pattern[j] == '.' or pattern[j] == text[i])
            if j + 1 < len(pattern) and pattern[j + 1] == '*':
                memo[(i, j)] = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                memo[(i, j)] = first_match and dp(i + 1, j + 1)
        return memo[(i, j)]

    return dp(0, 0)



def solution(text, pattern):
    # return is_match_helper(text, pattern)
    return is_match_helper_dp(text, pattern)


def main():
    assert solution("aa", "a") is False
    assert solution("aa", "aa") is True
    assert solution("abc", "a.c") is True
    assert solution("abbb", "ab*") is True
    assert solution("abbc", "ab*") is False
    assert solution("acd", "ab*c.") is True
    # assert solution("", "*") is True
    assert solution("a", ".*") is True
    assert solution("bbb", ".*") is True
    assert solution("bcc", ".*") is True


if __name__ == '__main__':
    main()
