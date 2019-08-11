class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 如果给定的nums是 6,5,4,8,7,5,1，因为它的子序列8,7,5,1是已经按降序排列好的，
        # 调换这里的任意一个数字都不可能使排列更大，所以从后往前搜索一直到4这个数字，
        # 这时4,8,7,5,1已经不是降序排列的子数组了 ，并且4<5，如果能将4和5调换，
        # 那么整体数组变成6,5,5,8,7,4,1，这个时候的排列的确比nums要大，
        # 但是不满足题目中的next greater这个条件，我们要找的是它的下一个更大的排列，
        # 所以在调换了4和这5之后，需要把子数组8,7,4,1按照升序排列，nums变为6,5,5,1,4,7,8，
        # 这个数组就是我们要找的下一个更大的数字排列组合了。
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[i-1]:
                a = nums[i:]
                a.sort()
                for j in range(len(a)):
                    if a[j]>nums[i-1]:
                        nums[i-1],a[j] = a[j],nums[i-1]
                        break
                for n in range(i,len(nums)):
                    nums[n] = a[n-i]
                break
            elif i == 1:
                nums.sort()
                return 
        return
a = Solution()
nums = [3,2,1]
a.nextPermutation(nums)
print(nums)