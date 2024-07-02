class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        sum = numbers[left] + numbers[right]

        while (sum != target):
            if (sum > target):
                right -= 1
            else:
                left += 1
            sum = numbers[left] + numbers[right]
        
        return [left + 1, right + 1]
            