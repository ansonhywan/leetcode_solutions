class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = (
            1,
            1,
        )  # Keep track of cur max and cur min because negatives can flip them

        for n in nums:
            if (
                n == 0
            ):  # If we meet a 0, reset the cur max and cur min because n * 0 = 0
                curMax, curMin = 1, 1
                continue

            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        return res
