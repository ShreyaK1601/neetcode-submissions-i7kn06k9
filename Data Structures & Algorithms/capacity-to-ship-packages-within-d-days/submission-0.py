class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        result = r

        def canShip(capacity):
            ships, currCapacity = 1, capacity
            for w in weights:
                if currCapacity - w < 0:
                    ships += 1
                    currCapacity = capacity
                currCapacity -= w
            return ships <= days
            
        while l <= r:
            capacity = (l + r)//2
            if canShip(capacity):
                result = min(result, capacity)
                r = capacity - 1
            else:
                l = capacity + 1
        return result
        