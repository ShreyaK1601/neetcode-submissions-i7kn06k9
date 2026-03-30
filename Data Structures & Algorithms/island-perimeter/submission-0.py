class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        x, y = len(grid), len(grid[0])
        perimeter = 0
        for r in range(x):
            for c in range(y):
                if grid[r][c] == 1:
                    perimeter += 4
                    if r and grid[r-1][c]:
                        perimeter -= 2
                    if c and grid[r][c-1]:
                        perimeter -= 2
        return perimeter
        