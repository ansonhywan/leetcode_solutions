class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        result = []
        cycleSet = set()
        visitSet = set()

        def dfs(crs):
            if crs in cycleSet:
                # Cycle exists
                return False
            if crs in visitSet:
                # No cycle and all prerequisites qualified
                return True

            cycleSet.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            cycleSet.remove(crs)
            visitSet.add(crs)
            result.append(crs)

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return result
