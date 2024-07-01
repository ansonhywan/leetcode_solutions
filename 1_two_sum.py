class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {} # num : index

        for i, num in enumerate(nums):
            diff = target - num
            if diff in index_map:
                return i, index_map[diff]
            index_map[num] = i
