class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        tmp = 0
        m = -float('inf')
        for i in range(len(nums)):
            if tmp < 0:       #主要思路就是一旦前面之和等于零了，局部和 就归零
                tmp = 0
            tmp += nums[i]
            m = max(tmp,m)
        return m
a = Solution()
print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
