# class Solution(object):
#     def numTrees(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n == 1 or n == 0:return 1
#         # a=[1 for _ in range(n+1)]
#         # print(a)
#         res = 0
#         for i in range(1,n+1):
#             res += self.numTrees(i-1)*self.numTrees(n-i)
#         return res
#上面超时了，应该把已经算过的记录下来

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = [0 for _ in range(n+1)]
        a[0] = a[1] = 1
        def helper(n):
            if n == 1 or n == 0:
                return 1
            res = 0
            for i in range(1,n+1):
                s = a[i-1] if a[i-1] != 0 else helper(i-1)
                b = a[n-i] if a[n-i] != 0 else helper(n-1)
                res += s * b
                a[n] = res
                print(a)
            return res
        return helper(n)
# The pattern is simply:
# T(0) = 1 (defined for convenience)
# T(1) = 1 (number of binary search trees possible with one node)
# T(2) = 2 (number of binary search trees possible with two nodes)
# T(3) = T(0)*T(2) + T(1)*T(1) + T(2)*T(0) (1st term: lowest number is root, 2nd term: middle number is root, 3rd term: biggest number is root)
# T(4) = T(0)*T(3) + T(1)*T(2) + T(2)*T(1) + T(3)*T(0)
# T(5) = T(0)*T(4) + T(1)*T(3) + T(2)*T(2) + T(3)*T(1) + T(4)*T(0)

    def numTrees2(self, n):
        T = [1, 1, 2] + [0]*(n - 2)
        for m in range(3, n + 1):
            for i in range(m):
                T[m] += T[i] * T[m - 1 - i]
        return T[n]


a = Solution()
print(a.numTrees2(4))