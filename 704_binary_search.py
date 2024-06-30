class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums) - 1
        m = h // 2

        while l <= h:
            if nums[m] == target:
                return m

            if target > nums[m]:
                l = m + 1
            else:
                h = m - 1
            m = (h + l) // 2

        return -1
