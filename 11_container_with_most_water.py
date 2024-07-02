class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l, r = 0, len(height) - 1

        maxArea = 0
        
        while l < r:
            h1, h2 = height[l], height[r]

            length = min(h1,h2)
            width = r - l

            area = length * width
            
            # Update current max
            if area > maxArea:
                maxArea = area
            
            # ptr update conditions
            if h1 <= h2:
                l += 1
            else:
                r -= 1
            

        return maxArea
