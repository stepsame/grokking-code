"""
Word Count Engine
Implement a document scanning function wordCountEngine, which receives a string document and returns a list of all unique words in it
and their number of occurrences, sorted by the number of occurrences in a descending order. If two or more words have the same count,
they should be sorted according to their order in the original sentence. Assume that all letters are in english alphabet.
You function should be case-insensitive, so for instance, the words “Perfect” and “perfect” should be considered the same word.
The engine should strip out punctuation (even in the middle of a word) and use whitespaces to separate words.
input:  document = "Practice makes perfect. you'll only
                    get Perfect by practice. just practice!"
output: [ ["practice", "3"], ["perfect", "2"],
          ["makes", "1"], ["youll", "1"], ["only", "1"],
          ["get", "1"], ["by", "1"], ["just", "1"] ]
Important: please convert the occurrence integers in the output list to strings (e.g. "3" instead of 3).
"""
from collections import OrderedDict

"""
Solution:
1. split the words
2. lower case words
3. store word into a ordereddict, and count the occurrences.
4. using bucket sort algorithm to sort the result by occurrences.

Time Complexity: O(N) number of the words
Space Complexity: O(M) different words

"""


def solution(document):
    word_count = OrderedDict()
    raw_words = document.split()
    max_count = 0
    for word in raw_words:
        processed_word = ""
        for char in word:
            if char.isalpha():
                processed_word += char.lower()
        if processed_word in word_count:
            word_count[processed_word] += 1
            max_count = max(max_count, word_count[processed_word])
        else:
            word_count[processed_word] = 1

    # bucket sort
    buckets = [[] for i in range(max_count + 1)]
    for word, count in word_count.items():
        buckets[count].append(word)

    result = []
    for count in range(max_count, 0, -1):
        for word in buckets[count]:
            result.append([word, str(count)])
    return result


def main():
    assert solution(document='''Practice makes perfect. you'll only get Perfect by practice. just practice!''') == [
        ["practice", "3"], ["perfect", "2"],
        ["makes", "1"], ["youll", "1"], ["only", "1"],
        ["get", "1"], ["by", "1"], ["just", "1"]]


if __name__ == '__main__':
    main()
