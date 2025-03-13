class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]==1:
            return 0
        rows,cols = len(obstacleGrid),len(obstacleGrid[0])
        dp = [[0]*cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if i==0 and j==0:
                    dp[i][j] = 1
                elif i==0:
                    dp[i][j] = dp[i][j-1] if obstacleGrid[i][j]==0 else 0
                elif j==0:
                    dp[i][j] = dp[i-1][j] if obstacleGrid[i][j]==0 else 0
                else:
                    dp[i][j] = (dp[i-1][j] + dp[i][j-1]) if obstacleGrid[i][j]==0 else 0
        return dp[rows-1][cols-1]
