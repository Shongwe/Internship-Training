from typing import List, Set


def isValidSudoku(board: list[list[str]]) -> bool:
    """
    Determine if a 9x9 Sudoku board is valid.
    Only validate filled cells; empty cells are represented as '.'.

    Args:
        board (list[list[str]]): 9x9 Sudoku board

    Returns:
        bool: True if valid, False otherwise
    """
    rows: List[Set[str]]  = [set() for _ in range(9)]
    cols: List[Set[str]] = [set() for _ in range(9)]
    boxes: List[Set[str]] = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            cell = board[i][j]
            if cell == '.':
                continue

            # Box index: which 3x3 sub-grid
            box_idx = (i // 3) * 3 + (j // 3)

            # Check duplicates
            if cell in rows[i] or cell in cols[j] or cell in boxes[box_idx]:
                return False

            rows[i].add(cell)
            cols[j].add(cell)
            boxes[box_idx].add(cell)

    return True

def main():
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    print(isValidSudoku(board))  # Expected True

if __name__ == "__main__":
    main()
