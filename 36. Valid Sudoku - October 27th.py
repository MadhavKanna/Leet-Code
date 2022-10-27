class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            if not check_row(row):
                return False

        if not check_vertical(board):
            return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not check_box([row[j: j + 3] for row in board[i: i + 3]]):
                    return False

        return True


def check_row(row: List[str]):
    present = []
    for i in row:
        if i != '.' and i in present:
            return False
        present.append(i)
    return True


def check_vertical(board: List[List[str]]):
    for j in range(9):
        present = []
        for i in range(9):
            if board[i][j] != '.' and board[i][j] in present:
                return False
            present.append(board[i][j])
    return True


def check_box(box: List[List[str]]):
    present = []
    for row in box:
        for i in row:
            if i != '.' and i in present:
                return False
            present.append(i)
    return True
