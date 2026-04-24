class Solution:
    def maxArea(self, heights: List[int]) -> int:
            # Take shortest pillar height in calculating volume
            res = 0
            for i in range(len(heights)):
                for j in range(i + 1, len(heights)):
                    res = max((min(heights[i], heights[j]) * (j - i)), res)
            
            return res