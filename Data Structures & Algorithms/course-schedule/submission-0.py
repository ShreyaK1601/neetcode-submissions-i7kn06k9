class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for cr, pre in prerequisites:
            preMap[cr].append(pre)
        path = set()
        def dfs(cr):
            if cr in path:
                return False
            if preMap[cr] == []:
                return True
            path.add(cr)
            for pre in preMap[cr]:
                if not dfs(pre):
                    return False

            path.remove(cr)
            preMap[cr] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        