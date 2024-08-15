class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        ROWS = len(grid)
        COLS = len(grid[0])

        max_area = 0
        seen = [[0] * COLS for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, self.dfs(0, r, c, grid, seen, ROWS, COLS))

        return max_area

    def dfs(self, area, r, c, grid, seen, ROWS, COLS):
        if r not in range(ROWS) or c not in range(COLS):
            return 0
        if grid[r][c] == 0:
            return 0
        if seen[r][c] == 1:
            return 0

        seen[r][c] = 1

        return (
            1
            + self.dfs(area + 1, r + 1, c, grid, seen, ROWS, COLS)
            + self.dfs(area + 1, r - 1, c, grid, seen, ROWS, COLS)
            + self.dfs(area + 1, r, c + 1, grid, seen, ROWS, COLS)
            + self.dfs(area + 1, r, c - 1, grid, seen, ROWS, COLS)
        )
