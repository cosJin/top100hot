class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)/2
            if nums[mid] == target:  # mid > target 的有两种情况，一种是mid在前半段，
                #一种是mid在后半段，   其中mid在前半段时又分两种情况，target在前半段还是后半段。
                #分情况可以分成 left变到mid 和 right变到mid
                return mid
            elif nums[mid] > target:  #
                if nums[l] > target and nums[l] <= nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:   #mid < target 同理
                if nums[r] < target and nums[r] >= nums[mid]:
                    r = mid - 1                    
                else:
                    l = mid + 1
        return -1
a = Solution()        
print(a.search([1,2,3,4,5,6],5))