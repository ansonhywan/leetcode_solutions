class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.dp(nums[1:]), self.dp(nums[:-1]))

    def dp(self, nums):
        rob1 = 0
        rob2 = 0

        # [rob1, rob2, n, n+1, n+2, n+3, ...]
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
