class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Do a DFS search on all directions everytime we see a 1
        # Whenever we start a DFS search we increment island count

        if not grid or not grid[0]:
            return 0

        ROWS = len(grid)
        COLS = len(grid[0])

        count = 0
        seen = [[0] * COLS for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and seen[r][c] == 0:
                    count += 1
                    self.dfs(r, c, grid, seen, ROWS, COLS)
        return count

    def dfs(self, r, c, grid, seen, ROWS, COLS):
        if r not in range(ROWS) or c not in range(COLS):
            # Out of bounds of grid
            return

        if grid[r][c] == "0":
            # Not an island
            return

        if seen[r][c] == 1:
            # Already visited this coordinate
            return

        # Set this coordinate as seen
        seen[r][c] = 1

        self.dfs(r + 1, c, grid, seen, ROWS, COLS)
        self.dfs(r - 1, c, grid, seen, ROWS, COLS)
        self.dfs(r, c + 1, grid, seen, ROWS, COLS)
        self.dfs(r, c - 1, grid, seen, ROWS, COLS)
