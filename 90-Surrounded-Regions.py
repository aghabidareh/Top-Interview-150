class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()

        def bfs(r, c):
            q.append((r, c))
            board[r][c] = 'G'
            while q:
                x, y = q.popleft()
                for dx, dy in dir:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < rows
                            and 0 <= ny < cols
                            and board[nx][ny] == 'O'):
                        q.append((nx, ny))
                        board[nx][ny] = 'G'

        for i in range(cols):
            if (board[0][i] == 'O'):
                bfs(0, i)
            if (board[rows - 1][i] == 'O'):
                bfs(rows - 1, i)
        for j in range(rows):
            if (board[j][0] == 'O'):
                bfs(j, 0)
            if (board[j][cols - 1] == 'O'):
                bfs(j, cols - 1)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'G':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'