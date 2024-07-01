class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = [1] * len(nums)

        curr = 1
        for i in range(len(nums)-1):
            curr = curr * nums[i]
            results[i+1] = curr
            
        curr = 1
        for i in (range(len(nums)-1, 0, -1)):
            curr = curr * nums[i]
            results[i-1] *= curr

        return results
