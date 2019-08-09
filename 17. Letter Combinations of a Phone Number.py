class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        dir = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        res = []
        word = ""
        last = dir[digits[0]]
        digits = digits[1:]
        for d in digits:
            now = []
            for a in last:
                for b in dir[d]:
                    now.append(a+b)
            last = now
        return last
#也可以定义一个函数，进行迭代
    def letterCombinations2(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        self.dir = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        now = self.dir[digits[0]]
        return self.bfs(now,digits[1:])

    def bfs(self,now,letters):
        print(letters)
        if letters == "":
            return now
        temp = []
        for a in now:
            for b in self.dir[letters[0]]:
                temp.append(a+b)
        return self.bfs(temp,letters[1:])
a = Solution()
print(a.letterCombinations2("3"))