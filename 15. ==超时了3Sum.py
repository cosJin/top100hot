class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        print(nums)
        res = []
        for i,n in enumerate(nums):
            if n != nums[i-1] or i==0:
                newlist = nums[i+1:]
                left, right = 0, len(newlist)-1
                while right > left:
                    if newlist[left] + newlist[right] + n > 0:
                        right -= 1
                    elif newlist[left] + newlist[right] + n < 0:
                        left += 1
                    elif newlist[left] + newlist[right] + n == 0:
                        if [n,newlist[right],newlist[left]] not in res:
                            res.append([n,newlist[right],newlist[left]])
                        right -= 1
                        left += 1
        return res
    ##上面为自己想的办法，一个指针一个指针的挪，最后超过了时间限制不好
    ##下面为利用字典查询的方法。
    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i-1]:
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v,-v-x,x))
        return map(list,res)
a = Solution()
print(a.threeSum([-1,0,1,2,-1,-4]))

        