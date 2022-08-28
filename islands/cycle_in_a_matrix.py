"""
Problem Statement

You are given a 2D matrix containing different characters, you need to find if there exists any cycle consisting of the same character in the matrix.

A cycle is a path in the matrix that starts and ends at the same cell and has four  or more cells. From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the same character value of the current cell.

Write a function to find if the matrix has a cycle.

Example 1
Input: matrix =



Output: true
Explanation: The given matrix has a cycle as shown below:



Example 2

Input: matrix =




Output: true
Explanation: The given matrix has one cycle as shown below:



Example 3

Input: matrix =



Output: false
Explanation: The given matrix has no cycle.
"""

"""
Solution:
We will traverse the matrix linearly to find any cycle.
Each cycle is like an island having cells containing same values.
 Hence, we can use the Depth First Search (DFS) or Breadth First Search (BFS)
 to traverse a cycle i.e., to find all of its connected cells with the same value.
 
Whenever we reach a cell that have already been visited,
  we can conclude that we have found a cycle.
This also means that we need to be careful to not start traversing the parent cell and wrongly finding a cycle.


Time Complexity:

Space Complexity:

"""


def dfs_cycle(matrix, visited, char, x, y, prev_x, prev_y) -> bool:
    if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]):
        return False
    if matrix[x][y] != char:
        return False
    if visited[x][y]:
        return True
    visited[x][y] = True
    is_cycle = any([
        prev_x != x - 1 and dfs_cycle(matrix, visited, char, x - 1, y, x, y),
        prev_y != y + 1 and dfs_cycle(matrix, visited, char, x, y + 1, x, y),
        prev_x != x + 1 and dfs_cycle(matrix, visited, char, x + 1, y, x, y),
        prev_y != y - 1 and dfs_cycle(matrix, visited, char, x, y - 1, x, y),
    ])
    return is_cycle


def solution(matrix):
    visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if visited[i][j]:
                continue
            if dfs_cycle(matrix, visited, matrix[i][j], i, j, i, j):
                return True
    return False


def main():
    assert solution([
        ['a', 'a', 'a', 'a'],
        ['b', 'a', 'c', 'a'],
        ['b', 'a', 'c', 'a'],
        ['b', 'a', 'a', 'a']]) is True

    assert solution([
        ['a', 'a', 'a', 'a'],
        ['a', 'b', 'b', 'a'],
        ['a', 'b', 'a', 'a'],
        ['a', 'a', 'a', 'c']]) is True

    assert solution([
        ['a', 'b', 'e', 'b'],
        ['b', 'b', 'b', 'b'],
        ['b', 'c', 'c', 'd'],
        ['c', 'c', 'd', 'd']]) is False


if __name__ == '__main__':
    main()
