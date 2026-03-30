class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid and not grid[0]:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    islands += 1
                    stack = [(r,c)]
                    grid[r][c] = "0"
                    while stack:
                        cr, cc = stack.pop()
                        for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                            nr, nc = cr+dr, cc+dc
                            if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == "1":
                                grid[nr][nc] = "0"
                                stack.append((nr,nc))
        return islands

        