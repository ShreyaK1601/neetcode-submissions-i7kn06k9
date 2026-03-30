class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #Brute force approach
        # result = 0
        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i, len(nums)):
        #         sum += nums[j]
        #         if sum == k:
        #             result += 1
        # return result
        result = curSum = 0
        prefixSums = {0:1}

        for i in nums:
            curSum += i
            diff = curSum - k

            result += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
        return result 


        