class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmp = defaultdict(list)

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] += 1
            hashmp[tuple(count)].append(s)
        return list(hashmp.values())

        