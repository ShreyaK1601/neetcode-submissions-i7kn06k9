class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Binary Search (One Pass)
        rows, cols = len(matrix), len(matrix[0])
        l, rt = 0, rows*cols - 1
        while l <= rt:
            m = l + (rt - l)//2
            r, c = m // cols, m % cols
            if matrix[r][c] < target:
                l = m + 1
            elif matrix[r][c] > target:
                rt = m - 1
            else:
                return True
        return False
        