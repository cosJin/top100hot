class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = int(l + (r-l)/2)
            print(mid)
            if nums[l] == target and nums[r] == target:
                return [l,r]
            elif nums[mid] < target:
                l = mid+1
            elif nums[mid] > target:
                r = mid-1
            elif nums[mid] == target:
                ll = mid - 1
                rr = mid + 1                    #我的方法，找到target后左右延伸。
                while nums[ll] == nums[mid]:
                    if ll == 0:
                        ll -= 1
                        break
                    ll -= 1
                while nums[rr] == nums[mid]:
                    if rr == len(nums) - 1: 
                        rr += 1
                        break
                    rr += 1
                l, r = ll + 1, rr - 1
        return [-1,-1]
def searchRange(self, nums, target):
    def binarySearchLeft(A, x):
        left, right = 0, len(A) - 1
        while left <= right:
            mid = (left + right) / 2
            if x > A[mid]: left = mid + 1   #终止的时候 r在l 的左边，l指向 target的最左端的坐标。
            else: right = mid - 1
        return left

    def binarySearchRight(A, x):
        left, right = 0, len(A) - 1
        while left <= right:
            mid = (left + right) / 2
            if x >= A[mid]: left = mid + 1  #最右端。
            else: right = mid - 1
        return right
        
    left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
    return (left, right) if left <= right else [-1, -1]
a = Solution()
print(a.searchRange([1,2,2],2))
