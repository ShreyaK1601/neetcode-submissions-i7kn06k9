class Solution:
    def rob(self, nums: List[int]) -> int:
        #Solution using Recursion with TC=O(n^2)
        # def dfs(i):
        #     if i>= len(nums):
        #         return 0
        #     return max(nums[i] + dfs(i+2), dfs(i+1))

        # return dfs(0)

        r1, r2 = 0, 0
        for i in nums:
            tmp = max(i+r1, r2)
            r1 = r2
            r2 = tmp
        return tmp





        