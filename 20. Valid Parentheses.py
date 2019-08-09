class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":return True
        stack = []
        dir = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for a in s:
            if stack !=[] and a in dir:
                if dir[a] != stack.pop():return False  #如果不对，则直接返回False，不在继续下去
            else:stack.append(a)
            print(stack)
        return stack == []
a = Solution()
print(a.isValid("()[]"))

