class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Brute Force with TC = O(nlogn+mlogm) SC = O(1)/O(n+m)depend on Sorting algo
        # if len(s) != len(t):
        #     return False
        # return True if sorted(s) == sorted(t) else False

        #Optimal Solution using HashMap TC= O(n+m) and SC = O(1)
        if len(s) != len(t):
            return False
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return True if countS == countT else False





        