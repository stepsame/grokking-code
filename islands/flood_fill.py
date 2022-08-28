"""
Problem Statement

Any image can be represented by a 2D integer array (i.e., a matrix) where each cell represents the pixel value of the image.

Flood fill algorithm takes a starting cell (i.e., a pixel) and a color. The given color is applied to all horizontally and vertically connected cells with the same color as that of the starting cell. Recursively, the algorithm fills cells with the new color until it encounters a cell with a different color than the starting cell.

Given a matrix, a starting cell, and a color, flood fill the matrix.

Example 1

Input: matrix =



     starting cell = (1, 3)
     new color = 2
Output:


Example 2

Input: matrix =



     starting cell = (3, 2)
     new color = 5
Output:


"""

"""
Solution:

We will use depth first search or breadth first search to search all the cell
 and then update the cell with new color.

Time Complexity:
DFS will be O(M*N)

Space Complexity:
DFS will be O(M*N)

"""


def dfs_fill_color(matrix, x, y, old_color, new_color):
    if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]):
        return
    if matrix[x][y] != old_color:
        return
    matrix[x][y] = new_color
    dfs_fill_color(matrix, x - 1, y, old_color, new_color)
    dfs_fill_color(matrix, x, y + 1, old_color, new_color)
    dfs_fill_color(matrix, x + 1, y, old_color, new_color)
    dfs_fill_color(matrix, x, y - 1, old_color, new_color)


def solution(matrix, x, y, new_color):
    if matrix[x][y] != new_color:
        dfs_fill_color(matrix, x, y, matrix[x][y], new_color)
    return matrix


def main():
    assert solution([
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 1],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
    ], 1, 3, 2) == [
        [0, 2, 2, 2, 0],
        [0, 0, 0, 2, 2],
        [0, 2, 2, 2, 0],
        [0, 2, 2, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    assert solution([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
    ], 3, 2, 5) == [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 5, 5, 0],
        [0, 0, 5, 0, 0],
        [0, 0, 5, 0, 0],
    ]


if __name__ == '__main__':
    main()
