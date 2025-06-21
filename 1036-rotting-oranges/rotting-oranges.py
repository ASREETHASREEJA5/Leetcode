from typing import List
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        q = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c,0))
                elif grid[r][c] == 1:
                    fresh+=1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m = 0 
        while q:
            r,c,m = q.popleft()
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh-=1
                    q.append((nr,nc,m+1))
        return m if fresh ==0 else -1
