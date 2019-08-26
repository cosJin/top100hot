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
                
                    
a = Solution()
print(a.minWindow("ADOBECODEBANC","ABC"))