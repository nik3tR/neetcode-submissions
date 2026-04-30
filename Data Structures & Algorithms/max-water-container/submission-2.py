class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        for i in range(len(heights)-1):
            for j in range(i+1, len(heights)):
                minHeight = min(heights[i], heights[j])
                water = (j-i) * minHeight
                maximum = max(maximum, water)
        return maximum