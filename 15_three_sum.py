class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, num1 in enumerate(nums):
            if (i > 0) and (nums[i - 1] == num1):
                continue
                
            l, r = i + 1, len(nums) - 1

            while l < r:
                num2 = nums[l]
                num3 = nums[r]

                sum = num1 + num2 + num3
                if sum == 0:
                    res.append([num1, num2, num3])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif sum > 0:
                    r -= 1
                else:
                    l += 1
        
        return res
