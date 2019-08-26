class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        def dfs(path,node):
            path.sort()
            res.add(tuple(path))
            if node==[]:return
            for i,n in enumerate(node):
                dfs(path+[n],node[:i]+node[i+1:])
        dfs([],nums)
        res = [list(i) for i in res]
        return res

class Solution2(object):
    def subsets(self, nums):
        result = [[]]
        for i in nums:
            for j in range(len(result)):
                result.append(result[j][:])  #添加一遍现有的所有result
                result[j].append(i)#  讲原来的result均加上个i
        return result
a = Solution2()
print(a.subsets([1,2,3]))


