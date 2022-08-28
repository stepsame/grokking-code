"""
Problem Statement

You are given a 2D matrix containing only 1s (land) and 0s (water).

An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water). Each cell is considered connected to other cells horizontally or vertically (not diagonally).

A closed island is an island that is totally surrounded by 0s (i.e., water). This means all horizontally and vertically connected cells of a closed island are water. This also means that, by definition, a closed island can't touch an edge (as then the edge cells are not connected to any water cell).

Write a function to find the number of closed islands in the given matrix.

Example 1

Input: matrix =



Output: 1
Explanation: The given matrix has two islands, but only the highlighted island is a closed island. The other island is touching the boundary that's why is is not considered a closed island.

Example 2

Input: matrix =



Output: 2
Explanation: The given matrix has two islands and both of them are closed islands.
"""

"""
Solution:
We will use depth first search or breadth first search to traverse all the islands.
The return value of the dfs or bfs function is if the island is closed.
Closed island means it not connected with edge.
Then we will count all the all the closed islands.

Time Complexity:
DFS: will be O(M*N)

Space Complexity:
DFS: will be O(M*N)

"""


def dfs_is_closed(matrix, visited, x, y) -> bool:
    if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]):
        return False
    if matrix[x][y] == 0 or visited[x][y]:
        return True

    visited[x][y] = True

    is_closed = True
    is_closed &= dfs_is_closed(matrix, visited, x - 1, y)
    is_closed &= dfs_is_closed(matrix, visited, x, y + 1)
    is_closed &= dfs_is_closed(matrix, visited, x + 1, y)
    is_closed &= dfs_is_closed(matrix, visited, x, y - 1)
    return is_closed


def solution(matrix):
    closed_number = 0
    visited = [[False for j in range(len(matrix[0]))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if visited[i][j] or matrix[i][j] == 0:
                continue
            is_closed = dfs_is_closed(matrix, visited, i, j)
            if is_closed:
                closed_number += 1
    return closed_number


def main():
    assert solution([
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
    ]) == 1

    assert solution([
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0],
    ]) == 2


if __name__ == '__main__':
    main()
