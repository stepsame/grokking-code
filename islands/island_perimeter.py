"""
Problem Statement

You are given a 2D matrix containing only 1s (land) and 0s (water).

An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water). Each cell is considered connected to other cells horizontally or vertically (not diagonally).

There are no lakes on the island, so the water inside the island is not connected to the water around it. A cell is a square with a side length of 1..

The given matrix has only one island, write a function to find the perimeter of that island.

Example 1

Input: matrix =



Output: 14
Explanation: The boundary of the island constitute 14 sides.

Example 2

Input: matrix =



Output: 12
Explanation: The boundary of the island constitute 12 sides.
"""

"""
Solution:
We will use depth first search or breadth first search to traverse the island.
We will include the side in the island perimeter if the next cell is water or next to the boundary.

Time Complexity:
O(M*N)

Space Complexity:
O(M*N)

"""


def dfs_get_perimeter(matrix, visited, x, y) -> int:
    if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]):
        return 1
    if visited[x][y]:
        return 0
    if matrix[x][y] == 0:
        return 1
    visited[x][y] = True
    perimeter = 0
    perimeter += dfs_get_perimeter(matrix, visited, x - 1, y)
    perimeter += dfs_get_perimeter(matrix, visited, x, y + 1)
    perimeter += dfs_get_perimeter(matrix, visited, x + 1, y)
    perimeter += dfs_get_perimeter(matrix, visited, x, y - 1)
    return perimeter


def solution(matrix) -> int:
    visited = [[False for j in range(len(matrix[0]))] for i in range(len(matrix))]
    perimeter = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if visited[i][j] or matrix[i][j] == 0:
                continue
            perimeter = dfs_get_perimeter(matrix, visited, i, j)
    return perimeter


def main():
    assert solution([
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
    ]) == 14
    assert solution([
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 0, 0],
    ]) == 12


if __name__ == '__main__':
    main()
