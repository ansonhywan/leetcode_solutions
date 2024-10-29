class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algorithm
        # Choice 1: Extend the maximum sum subarray ending at the previous element by adding the current element to it. If the maximum subarray sum ending at the previous index is positive, then it is always better to extend the subarray.
        # Choice 2: Start a new subarray starting from the current element. If the maximum subarray sum ending at the previous index is negative, it is always better to start a new subarray from the current element.
        res = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n

            res = max(res, curSum)

        return res
