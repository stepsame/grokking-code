"""
Problem Statement
You are visiting a farm to collect fruits. The farm has a single row of fruit trees. You will be given two baskets, and your goal is to pick as many fruits as possible to be placed in the given baskets.

You will be given an array of characters where each character represents a fruit tree. The farm has following restrictions:

Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
You can start with any tree, but you can’t skip a tree once you have started.
You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
Write a function to return the maximum number of fruits in both baskets.


Example 1:
Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Example 2:
Input: Fruit = ['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

"""

"""
solutions:
just like longest substring with k distinct characters and k equal to two.

1. We using the sliding window strategy.
 We use a hashmap to store character number, the hashmap's keys is the distinct number.
2. add new char to sliding window
3. shrink the sliding window if distinct number greater than k(=2)
4. current substring is ok, compare and store the max length

Time Complexity:
will be O(N). 
outer for loop runs for all fruits.
inner while loop will only process every fruit once.
O(N + N) asymptotically equivalent to O(N)

Space Complexity: 
will be O(1)

we only store 3 char's frequencies.
"""


def find_max_fruits(fruits):
    fruit_frequency = {}
    window_start = 0
    max_fruits = 0
    for window_end in range(len(fruits)):
        if fruits[window_end] not in fruit_frequency:
            fruit_frequency[fruits[window_end]] = 1
        else:
            fruit_frequency[fruits[window_end]] += 1
        while len(fruit_frequency) > 2:
            fruit_frequency[fruits[window_start]] -= 1
            if fruit_frequency[fruits[window_start]] == 0:
                del fruit_frequency[fruits[window_start]]
            window_start += 1
        max_fruits = max(max_fruits, window_end - window_start + 1)
    return max_fruits


def main():
    assert find_max_fruits(['A', 'B', 'C', 'A', 'C']) == 3
    assert find_max_fruits(['A', 'B', 'C', 'B', 'B', 'C']) == 5


if __name__ == '__main__':
    main()
