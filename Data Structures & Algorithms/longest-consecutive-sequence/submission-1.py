class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        Set = set(nums)
        maxLength = 0
        
        for num in Set:
            if (num - 1) not in Set:
                length = 1

                while (num + length) in Set:
                    length += 1

                if length > maxLength: 
                    maxLength = length
            


        return maxLength

