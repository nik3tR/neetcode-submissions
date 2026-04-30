class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            if i+1 < len(numbers):
                curr = i+1
            else: 
                curr = i
            while curr < len(numbers):
                print(curr, i)
                if numbers[i] + numbers[curr] == target:
                    return [i+1, curr+1]
                curr += 1
        