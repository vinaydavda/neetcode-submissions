class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Inspired from best answers
        res = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(area, res)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return res

        # My solution
        # res = 0
        # for i in range(len(heights)):
        #     for j in range(i + 1, len(heights)):
        #         res = max((min(heights[i], heights[j]) * (j - i)), res)
        
        # return res