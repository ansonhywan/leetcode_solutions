class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, nums, sum):
            if sum == target:
                res.append(nums.copy())
                return
            if i >= len(candidates) or sum > target:
                return

            nums.append(candidates[i])
            dfs(i, nums, sum + candidates[i])
            nums.pop()
            dfs(i + 1, nums, sum)

        dfs(0, [], 0)
        return res
