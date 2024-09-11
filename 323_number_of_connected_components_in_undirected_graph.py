class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Solution 1 - Intuitive DFS on each edge with adjacency List
        # Time Complexity: O(N + E)

        # adjList = {i: [] for i in range(n)}
        # for edge in edges:
        #     adjList[edge[0]].append(edge[1])
        #     adjList[edge[1]].append(edge[0])

        # visitSet = set()

        # def dfs(i):
        #     if i in visitSet:
        #         return

        #     visitSet.add(i)

        #     for e in adjList[i]:
        #         dfs(e)

        #     return

        # cc = 0
        # for i in range(n):
        #     if i not in visitSet:
        #         cc += 1
        #     dfs(i)

        # return cc

        # Solution 2 - Union Find Algorithm
        par = [i for i in range(n)]
        rank = [1] * n

        def findRootParent(n1):
            res = n1
            while res != par[res]:
                par[res] = par[par[res]]  # Path compression for optimization
                res = par[res]
            return res

        def union(n1, n2):
            p1 = findRootParent(n1)
            p2 = findRootParent(n2)

            if p1 == p2:
                # Same parent
                return 0

            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1

        cc = n
        for n1, n2 in edges:
            cc -= union(n1, n2)
        return cc
