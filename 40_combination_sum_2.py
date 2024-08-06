class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        def backtrack(i, nums, sum):
            if sum == target:
                res.append(nums.copy())
                return

            if i == len(candidates) or sum > target:
                return

            nums.append(candidates[i])
            backtrack(i + 1, nums, sum + candidates[i])
            nums.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, nums, sum)

        backtrack(0, [], 0)
        return res
