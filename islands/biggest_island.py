"""
Problem Statement

Given a 2D array (i.e., a matrix) containing only 1s (land) and 0s (water), find the biggest island in it. Write a function to return the area of the biggest island.

An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water). Each cell is considered connected to other cells horizontally or vertically (not diagonally).

Example 1

Input: matrix =



Output: 5
Explanation: The matrix has three islands. The biggest island has 5 cells .


"""

"""
Solution:
We will use Depth First Search or Breadth First Search to traverse every island return island area.


Time Complexity:
DFS will be O(M*N)

Space Complexity:
DFS will be O(M*N)

"""


def dfs_island_area(matrix, x, y) -> int:
    if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]):
        return 0
    if matrix[x][y] == 0:
        return 0
    area = 1
    matrix[x][y] = 0
    area += dfs_island_area(matrix, x - 1, y)
    area += dfs_island_area(matrix, x, y + 1)
    area += dfs_island_area(matrix, x + 1, y)
    area += dfs_island_area(matrix, x, y - 1)
    return area


def solution(matrix):
    max_area = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                continue
            area = dfs_island_area(matrix, i, j)
            max_area = max(max_area, area)
    return max_area


def main():
    assert solution([
        [1, 1, 1, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 1, 0, 0]
    ]) == 5


if __name__ == '__main__':
    main()
