"""
Problem Statement

Given a string and a list of words, find all the starting indices of substrings in the given string that are a concatenation of all the given words exactly once without any overlapping of words. It is given that all words are of the same length.

Example 1:

Input: String="catfoxcat", Words=["cat", "fox"]
Output: [0, 3]
Explanation: The two substring containing both the words are "catfox" & "foxcat".
Example 2:

Input: String="catcatfoxfox", Words=["cat", "fox"]
Output: [3]
Explanation: The only substring containing both the words is "catfox".
"""
import copy

"""
Solution:
This problem follow the sliding window pattern.
We will use a hashmap to keep track of the frequency of the words.
1. Starting from every index in the string, try to match all words.
2. In each iteration, reset the hashmap to original.
Then decrease word count in the hashmap. if one word is not found or frequency less than zero, we can stop.
3. we store the index.

Time Complexity:
will be O(N*M*LEN)

Space Complexity:
will be O(2M+N) O(M+N)

"""


def solution(string, words):
    words_freq = {}
    word_len = 0
    for w in words:
        word_len = len(w)
        if w not in words_freq:
            words_freq[w] = 0
        words_freq[w] += 1
    match_result = []
    for i in range(len(string) - word_len * len(words) + 1):
        match_freq = copy.copy(words_freq)
        matched = True
        for j in range(len(words)):
            word = string[i+j*word_len:i+(j+1)*word_len]
            if word not in match_freq:
                matched = False
                break
            match_freq[word] -= 1
            if match_freq[word] < 0:
                matched = False
                break
        if matched:
            match_result.append(i)
    return match_result


def main():
    assert solution(string="catfoxcat", words=["cat", "fox"]) == [0, 3]
    assert solution(string="catcatfoxfox", words=["cat", "fox"]) == [3]


if __name__ == '__main__':
    main()
