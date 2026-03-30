class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Optimal solution with Two pointers
        l, r = 0, len(numbers) - 1
        
        while l<r:
            curSum = numbers[l] + numbers[r]

            if curSum < target:
                l += 1
            elif curSum > target:
                r -= 1
            else:
                return [l+1, r+1]
        return []



        #Optimal Solution with Hashmap
        # hashmp = defaultdict(int)
        # for i in range(len(numbers)):
        #     temp = target - numbers[i]
        #     if hashmp[temp]:
        #         return [hashmp[temp], i+1]
        #     else:
        #         hashmp[numbers[i]] = i+1

        # return [] 
        