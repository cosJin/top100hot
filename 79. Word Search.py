class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:return False
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        self.res = False
        def dfs(target,i,j,board):
            if target == "":
                self.res = True
                return 
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if 0 <= x <= len(board)-1 and 0 <= y <= len(board[0])-1 and self.res != True: #这里判断res很重要，可以提高速度。
                    if board[x][y] == target[0]:
                        t = board[i][j]
                        board[i][j] = "#"
                        dfs(target[1:],x,y,board)
                        board[i][j] = t
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    dfs(word[1:],i,j,board)
        return self.res
a = Solution()
print(a.exist([["A","B","C","E"],
               ["S","F","E","S"],
               ["A","D","E","E"]], "ABCESEEEFS"))


            