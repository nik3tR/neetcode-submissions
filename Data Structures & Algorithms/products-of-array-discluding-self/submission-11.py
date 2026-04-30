class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        pre = []
        post = [1] * len(nums)
        prod = 1
        for num in nums:
            pre.append(prod)
            prod *= num

        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            post[i] = prod
            prod *= nums[i]
            res[i] = pre[i] * post[i]
        
        return res
