class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_w =0

        left, right = 0, len(height)-1

        while left < right :
            area = min(height[left], height[right]) * (right-left)

            max_w = max(max_w, area)

            if height[left] <= height[right] :
                left += 1
            elif height[left] > height[right] :
                right -= 1

            
        return max_w     
