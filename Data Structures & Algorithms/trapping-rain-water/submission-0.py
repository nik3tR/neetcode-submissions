class Solution:
    def trap(self, height: List[int]) -> int:

        totalWater = 0

        for i in range(len(height)):

            # start maxes from i
            maxL = height[i]
            maxR = height[i]

            # check for largest column left of i
            for j in range(i):
                if maxL < height[j]:
                    maxL = height[j]
            
            # largest column right of i
            for k in range(i+1, len(height)):
                if maxR < height[k]:
                    maxR = height[k]

            # water for i calc by smallest column - i
            water = min(maxL, maxR) - height[i] 

            if water > 0: totalWater += water
        
        return totalWater


