class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Set = set(nums)
        
        maxLength = 0
        
        for i in nums:
            if (i - 1) not in Set:
                longestSequence = [i]
            
                while (i + 1) in Set:
                    longestSequence.append(i + 1)
                    i += 1

                if len(longestSequence) > maxLength:
                    maxLength = len(longestSequence) 
            


        return maxLength

