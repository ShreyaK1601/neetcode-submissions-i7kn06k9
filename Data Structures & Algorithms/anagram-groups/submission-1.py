class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Optimal Solution using Hash Table with TC = O(m*n) 
        #and SC = O(m) extra space and O(m*n) space for output list
        result = defaultdict(list)
        for st in strs:
            count = [0] * 26
            for char in st:
                count[ord(char) - ord('a')] += 1
            result[tuple(count)].append(st)
        return list(result.values())

        