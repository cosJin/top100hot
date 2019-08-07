class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        fast = slow = 0
        dic = {}
        maxi = 0
        leng = 0
        while fast <= len(s)-1:
            if s[fast] not in dic:
                dic[s[fast]] = 1   #看了discuss，这里字典中存其位置比较好，
                                        #当遇到重复字符时，直接将slow指到位置加一的地方即可
                leng +=1
                fast += 1
            elif s[fast] in dic:
                dic.pop(s[slow])
                slow += 1
                leng -= 1
            maxi = leng if leng > maxi else maxi
        return maxi

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi = slow = 0
        dic = {}
        for fast,ss in enumerate(s):
            if ss in dic: slow = max(dic[ss] + 1, slow)
                                  # slow 只能往后移动
            dic[ss] = fast
            leng = fast - slow + 1
            maxi = max(leng,maxi)
        return maxi
a = Solution2()
print(a.lengthOfLongestSubstring("abba"))

