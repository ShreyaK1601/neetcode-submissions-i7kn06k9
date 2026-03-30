class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1

            if len(count) <= 2:
                continue
            
            newCount = defaultdict(int)
            for i, c in count.items():
                if c > 1:
                    newCount[i] = c - 1
            count = newCount
        
        result = []
        for i in count:
            if nums.count(i) > len(nums) // 3:
                result.append(i)
        return result
        