class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        i = 1
        while 1:
            if i not in nums:
                return i
            i += 1
        #这么写更简洁
        while i in nums:
            i += 1
        return i
a = Solution()
print(a.firstMissingPositive([2]))