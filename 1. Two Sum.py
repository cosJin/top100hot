class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
        for i,num in enumerate(nums):
            if num in dic.keys():
                return [dic[num],i]
            else:
                dic[target-num] = i
    def twoSum2(self, nums, target):
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic.keys():
                return [dic[nums[i]],i]
            else:
                dic[target-nums[i]] = i

            
a = Solution()
print(a.twoSum([2,6,4,5],7))