class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        vis = [[0] * m for _ in range(n)]

        def dfs(x, y):
            vis[x][y] = 1
            for dx, dy in [(-1,0), (0,1), (1,0), (0,-1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not vis[nx][ny] and board[nx][ny] == 'O':
                    dfs(nx, ny)

        for i in range(n):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][m-1] == 'O':
                dfs(i, m-1)

        for j in range(m):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[n-1][j] == 'O':
                dfs(n-1, j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and vis[i][j] == 0:
                    board[i][j] = 'X'