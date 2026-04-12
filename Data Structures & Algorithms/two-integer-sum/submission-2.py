class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Brute Force approach using 
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return []
        
        #Optimal Solution using Hashmap
        prevMap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[nums[i]] = i

        return []        