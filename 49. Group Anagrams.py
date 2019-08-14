class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #自己想到排序的方法，
        #看Solutuion里面有个统计数目的方法，用一串0统计
        res = {}
        for s in strs:
            dic = [0 for _ in range(26)]
            for l in s:
                dic[ord(l) - ord('a')] += 1
            if tuple(dic) in res:
                res[tuple(dic)].append(s)
            else:res[tuple(dic)] = [s]
        r = [res[i] for i in res]
        return r
a = Solution()
print(a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
            

