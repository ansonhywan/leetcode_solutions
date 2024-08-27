class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        ROWS = len(rooms)
        COLS = len(rooms[0])

        visited = set()
        q = deque()

        def addRoom(r, c):
            if r not in range(ROWS) or c not in range(COLS):
                return
            if (r, c) in visited:
                return
            if rooms[r][c] == -1:
                return
            q.append([r, c])
            visited.add((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))

        dist = 0
        while len(q) != 0:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)

            dist += 1
