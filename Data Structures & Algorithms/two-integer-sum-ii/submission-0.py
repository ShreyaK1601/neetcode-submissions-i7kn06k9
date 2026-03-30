class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmp = defaultdict(int)
        for i in range(len(numbers)):
            temp = target - numbers[i]
            if hashmp[temp]:
                return [hashmp[temp], i+1]
            else:
                hashmp[numbers[i]] = i+1

        return [] 
        