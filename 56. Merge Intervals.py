class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()   #方法一：先将线段从左到右排序，然后看下一个线段和上一个线段有无重叠。
        begin = float("-inf")
        end = float("-inf")
        res = []
        for inter in intervals:
            if inter[0] > end:
                res.append([begin,end])
                begin = inter[0]
                end = inter[1]
            else:
                begin = min(begin,inter[0])
                end = max(end,inter[1])
        res.append([begin,end])
        return res[1:]
a = Solution()
print(a.merge([[1,4],[4,5]]))