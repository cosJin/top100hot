class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.res = False
        tag = [[0 for _ in board[0]] for _ in board]
        def bfs(target,i,j):
            if target == "":
                self.res = True
                return 
            if i == 0 and board[i+1][j] == target[0] and tag[i+1][j] == 0:
                tag[i+1][j] = 1
                bfs(target[1:],i+1,j)
            elif i == len(board)-1 and board[i-1][j] == target[0] and tag[i-1][j] == 0: 
                tag[i-1][j] = 1
                bfs(target[1:],i-1,j)
            elif i != 0 and i != len(board)-1:
                if board[i-1][j] == target[0] and tag[i-1][j] == 0:
                    tag[i-1][j] = 1
                    bfs(target[1:],i-1,j)
                if board[i+1][j] == target[0] and tag[i+1][j] == 0:
                    tag[i+1][j] = 1
                    bfs(target[1:],i+1,j)
            if j == 0 and board[i][j+1] == target[0] and tag[i][j+1] == 0:
                tag[i][j+1] = 1
                bfs(target[1:],i,j+1)
            elif j == len(board[0])-1 and board[i][j-1] == target[0] and tag[i][j-1] == 0: 
                tag[i][j-1] = 1
                bfs(target[1:],i,j-1)
            elif j != 0 and j != len(board[0])-1:
                if board[i][j-1] == target[0] and tag[i][j-1] == 0:
                    tag[i][j-1] = 1
                    bfs(target[1:],i,j-1)
                if board[i][j+1] == target[0] and tag[i][j+1] == 0:
                    tag[i][j+1] = 1
                    bfs(target[1:],i,j+1)
        bfs(word,0,0)
        return self.res
a = Solution()
print(a.exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']],"BCCED"))


            