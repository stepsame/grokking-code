"""
Problem Statement

Given a 2D array (i.e., a matrix) containing only 1s (land) and 0s (water), count the number of islands in it.

An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water). Each cell is considered connected to other cells horizontally or vertically (not diagonally).

Example 1

Input: matrix =


Output: 1
Explanation: The matrix has only one island. See the highlighted cells below.

Example 2

Input: matrix =


Output: 3
Explanation: The matrix has three islands. See the highlighted cells below.

"""
import collections

"""
new words:
matrix
edge
horizontally
vertically
diagonally
traverse
depth
breadth
"""

"""
Solution:
We can traverse the matrix linearly to find islands.

Whenever we find a cell with the value 1, we have found an island.
Using that cell as the root node, we will perform a
Depth First Search(DFS) or Breadth First Search(BFS) to find all of its connected land cells.
During our DFS or BFS traversal, we will find and mark all the horizontally and vertically connected land cells.

Time Complexity:
DFS: will be O(M*N)
BFS: will be O(M*N)

Space Complexity:
DFS: will be O(M*N). Because the DFS recursion stack can goo M*N deep when the whole matrix is filled with '1's.
BFS: will be O(Min(M,N))
"""


def bfs_island(matrix, x, y):
    nodes = collections.deque([(x, y)])
    while nodes:
        i, j = nodes.popleft()
        if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
            continue
        if matrix[i][j] == 0:
            continue
        matrix[i][j] = 0
        nodes.append((i-1, j))
        nodes.append((i+1, j))
        nodes.append((i, j+1))
        nodes.append((i, j-1))


def dfs_island(matrix, x, y):
    if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]):
        return
    if matrix[x][y] == 0:
        return
    matrix[x][y] = 0
    dfs_island(matrix, x-1, y)
    dfs_island(matrix, x, y+1)
    dfs_island(matrix, x+1, y)
    dfs_island(matrix, x, y-1)


def count_islands(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                count += 1
            # dfs_island(matrix, i, j)
            bfs_island(matrix, i, j)
    return count


def main():
    assert count_islands([
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 1],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]) == 1
    assert count_islands([
        [1, 1, 1, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 0, 1, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0]
    ]) == 3
    assert count_islands([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]) == 1


if __name__ == '__main__':
    main()
