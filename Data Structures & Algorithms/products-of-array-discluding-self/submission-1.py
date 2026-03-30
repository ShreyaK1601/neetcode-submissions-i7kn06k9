class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Brute Force technique
        # result = [0]*len(nums)
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if i==j:
        #             continue
        #         product *= nums[j]
        #     result[i] = product
        # return result
    
        #Optimal Solution using Prefix Sufix method
        n = len(nums)
        result = [1]*n
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result
        