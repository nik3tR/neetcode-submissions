class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        # for i in range(nums)
        #   product = 1
        #   for every element in nums
        #       if elem not equal nums[i]
        #           product *= element
        #   output.append(product)
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]
            output.append(product)
        return output