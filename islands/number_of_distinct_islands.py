"""
Problem Statement

You are given a 2D matrix containing only 1s (land) and 0s (water).

An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water). Each cell is considered connected to other cells horizontally or vertically (not diagonally).

Two islands are considered the same if and only if they can be translated (not rotated or reflected) to equal each other.

Write a function to find the number of distinct islands in the given matrix.

Example 1

Input: matrix =



Output: 2
Explanation: There are four islands in the given matrix, but three of them are the same; hence, there are only two distinct islands.

Example 2

Input: matrix =



Output: 2
Explanation: There are three islands in the given matrix, but two of them are the same; hence, there are only two distinct islands.
"""
from enum import IntEnum

"""
Solution:
We will traverse the matrix linearly to find islands.
 We can use depth first search or breadth first search to traverse a island.
 
If two islands are same, their traversal path should be same too.
While traversing an island, we can construct a string map the traversal path of the island.

We can use a hashmap to store all the distinct paths.
 The total number of elements in the hashmap will be the number of distinct islands.

Time Complexity:
DFS will be O(M*N)

Space Complexity:
DFS will be O(M*N)

"""


class Direction(IntEnum):
    DEFAULT = 0
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


def dfs_get_path(matrix, visited, x, y, direction: Direction) -> str:
    if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]):
        return ""
    if visited[x][y] or matrix[x][y] == 0:
        return ""
    path = str(direction.value)
    visited[x][y] = True
    path += dfs_get_path(matrix, visited, x - 1, y, Direction.UP)
    path += dfs_get_path(matrix, visited, x, y + 1, Direction.RIGHT)
    path += dfs_get_path(matrix, visited, x + 1, y, Direction.DOWN)
    path += dfs_get_path(matrix, visited, x, y - 1, Direction.LEFT)
    return path


def solution(matrix):
    visited = [[False for j in range(len(matrix[0]))] for i in range(len(matrix))]
    path_map = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0 or visited[i][j]:
                continue
            path = dfs_get_path(matrix, visited, i, j, Direction.DEFAULT)
            path_map.add(path)
    return len(path_map)


def main():
    assert solution([
        [1, 1, 0, 1, 1],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1],
        [0, 1, 1, 0, 1]]) == 2
    assert solution([
        [1, 1, 0, 1],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 1, 0]]) == 2


if __name__ == '__main__':
    main()
