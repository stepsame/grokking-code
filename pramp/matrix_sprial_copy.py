"""
Matrix Spiral Copy
Given a 2D array (matrix) inputMatrix of integers, create a function spiralCopy that copies inputMatrix’s values into a 1D array in a spiral order, clockwise.
Your function then should return that array. Analyze the time and space complexities of your solution.
input:  inputMatrix  = [ [1,    2,   3,  4,    5],
                         [6,    7,   8,  9,   10],
                         [11,  12,  13,  14,  15],
                         [16,  17,  18,  19,  20] ]
output: [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]

"""

"""
Solution:
just traverse the matrix in a spiral order, clockwise. 
using four variable record current top, bottom, left, right.

Time Complexity: O(M*N)
Space Complexity: O(M*N)

"""


def solution(input_matrix):
    m, n = len(input_matrix), len(input_matrix[0])
    top, bottom, left, right = 0, m - 1, 0, n - 1
    result = []
    while top <= bottom and left <= right:
        # top row, left to right
        for j in range(left, right + 1):
            result.append(input_matrix[top][j])
        top += 1

        # right column, top to bottom
        for i in range(top, bottom + 1):
            result.append(input_matrix[i][right])
        right -= 1

        # bottom row, right to left
        for j in range(right, left - 1, -1):
            result.append(input_matrix[bottom][j])
        bottom -= 1

        # left column, bottom to top
        for i in range(bottom, top - 1, -1):
            result.append(input_matrix[i][left])
        left += 1
    return result


def main():
    assert solution(input_matrix=[[1, 2, 3, 4, 5],
                                  [6, 7, 8, 9, 10],
                                  [11, 12, 13, 14, 15],
                                  [16, 17, 18, 19, 20]]) == [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9,
                                                             14, 13, 12]

    assert solution(input_matrix=[
        [ 1,  2,  3,  4],
        [ 6,  7,  8,  9],
        [11, 12, 13, 15],
        [16, 17, 18, 20],
    ]) == [1, 2, 3, 4, 9, 15, 20, 18, 17, 16, 11, 6, 7, 8, 13, 12]


if __name__ == '__main__':
    main()
