class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pac = set()
        atl = set()
        res = []

        def dfs(r, c, prev_h, visited):
            if r not in range(ROWS) or c not in range(COLS):
                return

            cur_h = heights[r][c]

            if cur_h < prev_h:
                return
            if (r, c) in visited:
                return

            visited.add((r, c))

            dfs(r + 1, c, cur_h, visited)
            dfs(r - 1, c, cur_h, visited)
            dfs(r, c + 1, cur_h, visited)
            dfs(r, c - 1, cur_h, visited)

        for r in range(ROWS):
            # Loop through first and last col
            dfs(r, 0, heights[r][0], pac)
            dfs(r, COLS - 1, heights[r][COLS - 1], atl)

        for c in range(COLS):
            # Loop through first and last row
            dfs(0, c, heights[0][c], pac)
            dfs(ROWS - 1, c, heights[ROWS - 1][c], atl)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res
