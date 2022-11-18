"""
Shortest Word Edit Path
Given two words source and target, and a list of words words, find the length of the shortest series of edits that transforms source to target.
Each edit must change exactly one letter at a time, and each intermediate word (and the final target word) must exist in words.
If the task is impossible, return -1.
source = "bit", target = "dog"
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]
output: 5
explanation: bit -> but -> put -> pot -> pog -> dog has 5 transitions.
source = "no", target = "go"
words = ["to"]
output: -1
"""

"""
Solution:
when i think of the edit distance or editing a word it	probably be boiling down to like updating a letter.
 since the initial list of words they're all going to be the	same word length that's probably just going to be updating a letter. 
 we're also thinking of minimum edit distances  a graph traversal algorithm	
 and since we're going for a minimum at a distance probably want to	something like breadth first search rather than	depth first search 


Time Complexity: O(N^2*M) N is words count, M is word length 
Space Complexity: O(N^2)

"""


def solution(source, target, words):
    # construct the graph
    one_edit_distance_graph = {}
    words.append(source)
    for i in range(len(words)):
        base_word = words[i]
        for j in range(len(words)):
            if i != j:
                new_word = words[j]
                if is_one_edit_distance(base_word, new_word):
                    if base_word in one_edit_distance_graph:
                        one_edit_distance_graph[base_word].append(new_word)
                    else:
                        one_edit_distance_graph[base_word] = [new_word]

    # bfs traverse graph
    queue = [(source, 0)]
    visited_word_set = set()
    while queue:
        current_word, current_step = queue.pop(0)
        for word in one_edit_distance_graph[current_word]:
            if word in visited_word_set:
                continue
            if word == target:
                return current_step + 1
            visited_word_set.add(word)
            queue.append((word, current_step + 1))
    return


def is_one_edit_distance(word1, word2):
    diff_char_count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff_char_count += 1
        if diff_char_count > 1:
            return False
    return True


def main():
    words = ["but", "put", "big", "pot", "pog", "dog", "lot"]
    assert solution(source="bit", target="dog", words=words) == 5
    words = ["fail", "fall", "fale", "fait", "falt", "folt"]
    assert solution(source="fail", target="fale", words=words) == 2


if __name__ == '__main__':
    main()
