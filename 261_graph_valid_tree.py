class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Build adjacency list
        adjList = {i: [] for i in range(n)}

        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        visitSet = set()

        # DFS each
        def dfs(i, prev):
            if i in visitSet:
                # Cycle exists
                return False

            visitSet.add(i)

            for j in adjList[i]:
                if j == prev:
                    # Cycle exists
                    continue
                if not dfs(j, i):
                    return False
            return True

        return dfs(0, -1) and n == len(visitSet)
