class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        maxCount = 0
        result = 0
        for i in nums:
            count[i] += 1
            if count[i] > maxCount:
                result = i
                maxCount = count[i]
        return result

        