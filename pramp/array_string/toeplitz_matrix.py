"""
Toeplitz Matrix
A Toeplitz matrix is a matrix where every left-to-right-descending diagonal has the same element.
Given a non-empty matrix arr, write a function that returns true if and only if it is a Toeplitz matrix.
The matrix can be any dimensions, not necessarily square.
For example,
[[1,2,3,4],
 [5,1,2,3],
 [6,5,1,2]]
is a Toeplitz matrix, so we should return true, while
[[1,2,3,4],
 [5,1,9,3],
 [6,5,1,2]]
isn’t a Toeplitz matrix, so we should return false.
"""

"""
Solution: Just check every left-to-right-descending diagonal's number. start from (1, 1), check if (i - 1, j - 1) equal to (i, j)

Time Complexity: O(N*M)
Space Complexity: O(1)

"""


def solution(matrix):
    m, n = len(matrix), len(matrix[0])
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] != matrix[i-1][j-1]:
                return False
    return True


def main():
    assert solution([[1, 2, 3, 4],
                     [5, 1, 2, 3],
                     [6, 5, 1, 2]]) is True
    assert solution([[1, 2, 3, 4],
                     [5, 1, 9, 3],
                     [6, 5, 1, 2]]) is False


if __name__ == '__main__':
    main()
