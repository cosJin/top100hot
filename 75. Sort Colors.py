class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        numof0 = 0
        res = []
        for n in nums:
            if n == 0:
                res.insert(0,0)
                numof0 += 1
            elif n == 2: res.append(2)
            else:res.insert(numof0,1)
        print(res)
        nums = res[:]
        return nums

a = Solution()
print(a.sortColors([2,0,2,1,1,0]))
            
