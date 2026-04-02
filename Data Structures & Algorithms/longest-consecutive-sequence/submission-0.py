class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Brute Force Solution with TC = O(n^2) and SC = O(n)
        # result = 0
        # store = set(nums)
        
        # for num in nums:
        #     streak, curr = 0, num
        #     while curr in store:
        #         streak += 1
        #         curr += 1
        #     result = max(result, streak)
        # return result

        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest





