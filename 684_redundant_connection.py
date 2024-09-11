class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Union Find Algorithm
        # Time Complexity: O(n)

        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def findRootParent(n1):
            res = n1

            while par[res] != res:
                par[res] = par[par[res]]  # Optimization line
                res = par[res]

            return res

        def union(n1, n2):
            n1 = findRootParent(n1)
            n2 = findRootParent(n2)

            if n1 == n2:
                return False

            if rank[n1] > rank[n2]:
                par[n2] = n1
                rank[n1] += rank[n2]
            else:
                par[n1] = n2
                rank[n2] += rank[n1]

            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
