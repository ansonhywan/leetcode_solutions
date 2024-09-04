class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS
        # Start from rotting o, bfs add adjacent cells to bfs queue
        # Do not revisit visited cells, use set to hold visited coordinates
        # Every bfs expansion (iteration) is a "minute"

        ROWS = len(grid)
        COLS = len(grid[0])
        mins = 0
        o = 0

        q = deque()

        def addCell(r, c, o):
            if r not in range(ROWS) or c not in range(COLS):
                return o
            if grid[r][c] == 0:
                return o
            if grid[r][c] == 2 or grid[r][c] == 0:
                return o

            grid[r][c] = 2
            o -= 1
            q.append([r, c])
            return o

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])
                if grid[r][c] == 1:
                    o += 1

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while o > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    o = addCell(row, col, o)

            mins += 1

        return mins if o == 0 else -1
