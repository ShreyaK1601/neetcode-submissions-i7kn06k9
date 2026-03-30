class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Optimal Sliding Window approach
        hMap = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in hMap:
                l = max(l, hMap[s[r]] + 1)
            hMap[s[r]] = r
            res = max(res, hMap[s[r]] - l + 1)
        return res

        #Brute Force Approach
        # res = 0
        # for i in range(len(s)):
        #     subStr = set()
        #     for j in range(i, len(s)):
        #         if s[j] in subStr:
        #             break
        #         subStr.add(s[j])
        #     res = max(res, len(subStr))
        # return res