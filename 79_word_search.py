class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        ROWS = len(board)
        COLS = len(board[0])

        def backtrack(row, col, pos):
            # pos is the position in the target word we have found up to

            # Base cases
            if pos == len(word):
                return True
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or pos >= len(word):
                return False
            if (row, col) in path:
                return False
            if board[row][col] != word[pos]:
                return False

            # Subproblem on the next letter
            # Next letter either up down left or right
            path.add((row, col))
            res = (
                backtrack(row + 1, col, pos + 1)
                or backtrack(row, col + 1, pos + 1)
                or backtrack(row - 1, col, pos + 1)
                or backtrack(row, col - 1, pos + 1)
            )
            path.remove((row, col))
            return res

        # Go through all letters in the board as a starting position
        for row in range(ROWS):
            for col in range(COLS):
                if backtrack(row, col, 0):
                    return True
        return False

        return backtrack(0, 0, 0, [])
