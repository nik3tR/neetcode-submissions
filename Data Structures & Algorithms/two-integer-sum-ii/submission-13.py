class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numSet = set(numbers)

        for i in range(len(numbers)):
                if (target - numbers[i]) in numSet:
                    for j in range (i, len(numbers)):
                        if numbers[j] == target - numbers[i]:
                            return [i+1, j+1]
        