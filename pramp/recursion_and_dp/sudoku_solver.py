"""
Sudoku Solver
Write the function sudokuSolve that checks whether a given sudoku board (i.e. sudoku puzzle) is solvable. If so, the function will returns true.
Otherwise (i.e. there is no valid solution to the given sudoku board), returns false.
In sudoku, the objective is to fill a 9x9 board with digits so that each column, each row, and each of the nine 3x3 sub-boards
that compose the board contains all of the digits from 1 to 9. The board setter provides a partially completed board,
which for a well-posed board has a unique solution. As explained above, for this problem, it suffices to calculate whether a given sudoku board has a solution.
No need to return the actual numbers that make up a solution.
A sudoku board is represented as a two-dimensional 9x9 array of the characters ‘1’,‘2’,…,‘9’ and the '.' character, which represents a blank space.
The function should fill the blank spaces with characters such that the following rules apply:
  1) In every row of the array, all characters ‘1’,‘2’,…,‘9’ appear exactly once.
  2) In every column of the array, all characters ‘1’,‘2’,…,‘9’ appear exactly once.
  3) In every 3x3 sub-board that is illustrated below, all characters ‘1’,‘2’,…,‘9’ appear exactly once.
A solved sudoku is a board with no blank spaces, i.e. all blank spaces are filled with characters that abide to the constraints above.
If the function succeeds in solving the sudoku board, it’ll return true (false, otherwise).
"""

"""
Solution:
The main idea for the solution is using a recursive algorithm that iterates through the empty cell on the board,
and on the possible candidate numbers for each empty cell, and tries to fill them. 

First, we want to find the smallest sized 'newCandidates', plus remember the position where it was found
If we have not found any empty cell, then the whole board is filled already
Then, For each possible value that can be placed in position (row, col), let's place that value 
and then recursively query whether the board can be solved.
    If it can, we are done.
    Otherwise, there is no value that can be placed into position (row, col) to make the board solved

because the size of the sudoku board is fixed,
the asymptotic behavior of our algorithm is capped and therefore both are constant.
Time Complexity: O(1)
Space Complexity: O(1)

"""


def get_candidates(board, row, col):
    candidates = set('123456789')
    for j in range(9):
        # ignore current (row, j),
        if board[row][j] != '.':
            candidates.discard(board[row][j])
    for i in range(9):
        # ignore current (i, col)
        if board[i][col] != '.':
            candidates.discard(board[i][col])
    # 0, 0 ;  0, 3, 0, 6
    # 3, 0;  3, 3, 3, 6
    # 6, 0;  6, 3, 6, 6
    sub_board_i = row // 3 * 3
    sub_board_j = col // 3 * 3
    for i in range(sub_board_i, sub_board_i + 3):
        for j in range(sub_board_j, sub_board_j + 3):
            # ignore current 3x3 sub-board
            if board[i][j] != '.':
                candidates.discard(board[i][j])
    return candidates


def solution(board):
    min_candidates = set()
    min_i, min_j = 0, 0
    is_filled = True
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                is_filled = False
                new_candidates = get_candidates(board, i, j)
                if not min_candidates or new_candidates < min_candidates:
                    min_candidates = new_candidates
                    min_i, min_j = i, j

    if is_filled:
        return True

    for candidate in min_candidates:
        board[min_i][min_j] = candidate
        if solution(board):
            return True
        # restore value to '.'
        board[min_i][min_j] = '.'

    return False


def main():
    assert solution([
        ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
    ]) is True


if __name__ == '__main__':
    main()
