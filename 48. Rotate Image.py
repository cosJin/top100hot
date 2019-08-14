class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        matrix2 = [[a for a in b] for b in matrix]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[j][-i-1] = matrix2[i][j]
        return matrix
a = Solution()
print(a.rotate([[1,2,3],[4,5,6],[7,8,9]]))