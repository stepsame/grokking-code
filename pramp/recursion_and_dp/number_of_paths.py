"""
Number of Paths
You’re testing a new driverless car that is located at the Southwest (bottom-left) corner of an n×n grid.
The car is supposed to get to the opposite, Northeast (top-right), corner of the grid.
Given n, the size of the grid’s axes, write a function numOfPathsToDest that returns the number of the possible paths the driverless car can take.
For convenience, let’s represent every square in the grid as a pair (i,j).
The first coordinate in the pair denotes the east-to-west axis, and the second coordinate denotes the south-to-north axis.
The initial state of the car is (0,0), and the destination is (n-1,n-1).
The car must abide by the following two rules: it cannot cross the diagonal border.
In other words, in every step the position (i,j) needs to maintain i >= j.
In every step, it may go one square North (up), or one square East (right), but not both. E.g. if the car is at (3,1), it may go to (3,2) or (4,1).
input:  n = 4
output: 5
"""

"""
Solution:
We can use dynamic programming to solve this problem.
First, let us think about base situation. f(0, 0) is 1.
Then we can define a transition function f(i, j) i >= j, is equal to f(i - 1, j) + f(i, j - 1)

Time Complexity: O(N^2)
Space Complexity: O(N^2) can be optimized to O(N)

"""


def solution(n):
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(n):
            if i >= j:
                if i - 1 >= 0:
                    dp[i][j] += dp[i - 1][j]
                if j - 1 >= 0:
                    dp[i][j] += dp[i][j - 1]
    return dp[n - 1][n - 1]


def main():
    assert solution(n=4) == 5


if __name__ == '__main__':
    main()
