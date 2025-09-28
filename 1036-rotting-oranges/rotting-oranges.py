class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        fresh = 0
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] ==2:
                    q.append((r,c,0))
                elif grid[r][c]==1:
                    fresh+=1
        d = [(0,1),(1,0),(-1,0),(0,-1)]
        m = 0
        while q:
            dr,dc,m = q.popleft()
            for i,j in d:
                nr = dr+i
                nc = dc+j
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
                    grid[nr][nc]=2
                    fresh-=1
                    q.append((nr,nc,m+1))
        return m if fresh==0 else -1
                


        