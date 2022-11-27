"""
Diff Between Two Strings
Given two strings of uppercase letters source and target, list (in string form) a sequence of edits to convert from source to target
that uses the least edits possible.
For example, with strings source = "ABCDEFG", and target = "ABDFFGH" we might return: ["A", "B", "-C", "D", "-E", "F", "+F", "G", "+H"
More formally, for each character C in source, we will either write the token C, which does not count as an edit;
or write the token -C, which counts as an edit.
Additionally, between any token that we write, we may write +D where D is any letter, which counts as an edit.
At the end, when reading the tokens from left to right, and not including tokens prefixed with a minus-sign, the letters should spell out target
(when ignoring plus-signs.)
In the example, the answer of A B -C D -E F +F G +H has total number of edits 4 (the minimum possible), a
nd ignoring subtraction-tokens, spells out A, B, D, F, +F, G, +H which represents the string target.
If there are multiple answers, use the answer that favors removing from the source first.
"""

"""
Solution:
Our solution will be built in two steps: first, we'll find the edit distance, and then use it to construct the answer.

1. Finding the Editing Distance
First, let dp(i, j) = the minimum number of edits required for the problem with strings source[i:] and target[j:].
In general, when source[i] == target[j], then dp(i, j) = dp(i+1, j+1), because we simply write source[i].
 When source[i] != target[j], then we either edited source[i] (subtraction)
  and have the problem of transforming source[i+1:] to target[j:] left over (which has answer dp(i+1, j)),
  or we edited target[j] (addition) and have the problem of transforming source[i:] to target[j+1:] left over (which has answer dp(i, j+1)).
  
2. We should iterate through the source and target, and in each step using dp(i, j) to decide whether we need to delete or add another letter.

Time Complexity: O(MN), where M is the length of the source string and N is the length of the target string, from our construction of memo.
Space Complexity: O(MN), where M is the length of the source string and N is the length of the target string, the space taken by memo.

"""


def solution(source, target):
    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == len(source) or j == len(target):
            memo[(i, j)] = len(target) - j
        elif source[i] == target[j]:
            memo[(i, j)] = dp(i + 1, j + 1)
        else:
            memo[(i, j)] = 1 + min(dp(i + 1, j), dp(i, j + 1))
        return memo[(i, j)]

    dp(0, 0)

    i, j = 0, 0
    ans = []
    while i < len(source) and j < len(target):
        if source[i] == target[j]:
            ans.append(source[i])
            i += 1
            j += 1
        else:
            if memo[(i + 1, j)] <= memo[(i, j + 1)]:
                ans.append('-' + source[i])
                i += 1
            else:
                ans.append('+' + target[j])
                j += 1

    ans.extend(['+' + char for char in target[j:]])
    return ans



def main():
    assert solution(source = "ABCDEFG", target = "ABDFFGH") == ["A", "B", "-C", "D", "-E", "F", "+F", "G", "+H"]


if __name__ == '__main__':
    main()
