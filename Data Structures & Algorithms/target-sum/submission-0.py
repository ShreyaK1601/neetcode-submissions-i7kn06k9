class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #SOlution using Top-down approach with TC & SC = O(m*n)
        # dp = {}
        # def backtrack(i, total):
        #     if i == len(nums):
        #         return 1 if total == target else 0
        #     if (i, total) in dp:
        #         return dp[(i, total)]
        #     dp[(i, total)] = (backtrack(i+1, total + nums[i]) + backtrack(i+1, total - nums[i]))
        #     return dp[(i, total)]

        # return backtrack(0, 0)

        #Optimal Solution using DP space optimized approach with TC = O(m*n) & SC = O(n)
        dp = defaultdict(int)
        dp[0] = 1
        for i in nums:
            new_dp = defaultdict(int)
            for total, count in dp.items():
                new_dp[total + i] += count
                new_dp[total - i] += count
            dp = new_dp
        return dp[target]