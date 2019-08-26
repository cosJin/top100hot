class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        left = right = 0
        tmp = {}
        minimum = float('inf')
        res = ''
        while left <= right and right<=len(s)-1:
            while left <= right and len(tmp) < len(t) and right<=len(s)-1:
                print("right:",right)
                # print("s[right]",s[right])
                if s[right] in t and s[right] in tmp:tmp[s[right]] += 1
                elif s[right] in t and s[right] not in tmp: tmp[s[right]] = 1
                print("tmp",tmp)
                right += 1
            if right-left < minimum:res = s[left:right+1]
            minimum = min(minimum,right-left)


            tmp[s[left]] -= 1
            if tmp[s[left]] == 0:
                tmp.pop(s[left])
            if left <len(s)-1:left += 1
            while s[left] not in t:
                left += 1
            print("left:",left)
            if len(tmp) == len(t): 
                if right-left < minimum:res = s[left:right+1]
                minimum = min(minimum,right-left)
        return res
        #上面的方法不行

        #下面为答案：
import collections
class Solution2:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dicT = collections.Counter(t)
        print(dicT)#统计目标字符串各个字符的个数
        dicS = {}
        rec = set()
        j = 0
        res = float('inf')
        for i, c in enumerate(s):
            if c not in dicS:
                dicS[c] = 1
            else:
                dicS[c] += 1

            if c in dicT and dicT[c] <= dicS[c]:  #滑窗中的某字符个数满足要求，则加到rec中 
                rec.add(c)
                while len(rec) == len(dicT):   #当所有字符都满足要求的时候
                    dicS[s[j]] -= 1   #讲j指向的字母减一
                    if s[j] in dicT and dicT[s[j]] > dicS[s[j]]: #当减去一后不满足个数要求了就将该字符从rec中去掉。
                        rec.remove(s[j])
                        if res > i-j+1:
                            start = j
                            end = i
                            res = i-j+1  #减去1前的位置
                    j += 1
        if res == float('inf'):
            return ""
        return s[start:end+1]                    
a = Solution2()
print(a.minWindow("ADOBECODEBANC","ABC"))