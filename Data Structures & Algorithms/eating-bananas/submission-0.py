class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l+r)//2
            totTime = 0
            for p in piles:
                totTime += math.ceil(float(p)/k)
            if totTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res

        