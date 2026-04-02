class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #TC: O(nlogn) and SC: O(1) or O(n) depending on the sorting algorithm.
        people.sort()
        res = 0
        l, r = 0, len(people)-1
        while l<=r:
            remain = limit - people[r]
            r -= 1
            res += 1
            if l<=r and remain>= people[l]:
                l += 1
        return res

        #Optimal solution using Counting Sort
        # wt = max(people)
        # count = [0] * (wt + 1)
        # for p in people:
        #     count[p] += 1
        # indx, i = 0, 1
        # while indx<len(people):
        #     while count[i]==0:
        #         i += 1








