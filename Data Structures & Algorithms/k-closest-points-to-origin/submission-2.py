class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #Solution using Max-Heap with TC= O(nlogk) and SC= O(k)
        maxHeap = []
        for x, y in points:
            dist = -(x**2 + y**2)
            heapq.heappush(maxHeap, [dist, x, y])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        result = []
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            result.append([x, y])
        return result
        