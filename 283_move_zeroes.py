class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # To do in place (no creating new array), we need to use two-pointer technique
        l = 0
        for r in range(1, len(nums)):
            if nums[l] != 0:
                l += 1
            if nums[l] == 0 and nums[r] != 0:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l += 1
            r += 1
