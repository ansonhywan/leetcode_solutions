class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])

        # Invert the problem:
        # Instead of capturing all surrounded regions, capture everything except unsurrounded regions.
        def dfs(r, c):
            if r not in range(ROWS) or c not in range(COLS):
                return
            if board[r][c] != "O":
                return

            # Temporarily denote captured unsurrounded regions with a 'T'
            board[r][c] = "T"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Go around edge of board and run DFS to capture all unsurrounded regions.
        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(r, 0)
        for r in range(ROWS):
            if board[r][COLS - 1] == "O":
                dfs(r, COLS - 1)
        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0, c)
        for c in range(COLS):
            if board[ROWS - 1][c] == "O":
                dfs(ROWS - 1, c)

        # Capture all regions.
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # Uncapture unsurrounded regions.
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
