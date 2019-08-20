class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1: return 1
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[-1][-1] = 1
        def bfs(next):
            nex = set()
            if len(next) == 1:
                return dp[0][1] + dp[1][0]
            for point in next:
                dp[point[0]][point[1]] = (0 if point[0] == m-1 else dp[point[0]+1][point[1]]) + (0 if point[1] == n-1 else dp[point[0]][point[1] + 1])
                if point[0] != 0: nex.add((point[0] - 1, point[1])) 
                if point[1] != 0: nex.add((point[0], point[1] - 1)) 
            return bfs(nex)
        return bfs(((m-2,n-1),(m-1,n-2)))
a = Solution()
print(a.uniquePaths(3,2))
    



