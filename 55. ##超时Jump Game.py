class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #           方法一：后往前找，有能到达终点的就标记此点可到达终点。超时了
        n = len(nums)
        dp = [False for _ in range(n)]
        dp[-1] = True
        for i in range(n-2,-1,-1):
            for step in range(i+1,i+1+nums[i] if i+1+nums[i] <= n else n):  ##
                ####不用循环遍历着找后面的 好节点，只需要记录下来最右侧的好节点即可！！！
                if dp[step] == True:
                    dp[i] = True
                    continue
        return dp[0]

class Solution2(object):
    #################
    #     标准方法
    #################
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        right_most = n - 1
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= right_most:
                right_most = i
        return right_most == 0



        #################################################
        #       方法二 遍历所有分支，还是超时了,不如方法一好
        ###################################################
        # if len(nums) == 1:return True
        # dp = [False for _ in range(len(nums))]

        # def dfs(ii):   #nums 为 当前覆盖的input索引们
        #     for i in range(ii+1,ii+1+nums[ii] if ii+1+nums[ii] <= len(nums) else len(nums)):
        #         dp[i] = True
        #         dfs(i)
        #     if dp[-1] == True:return True
        #     else:return False
        # return True if dfs(0) is True else False

            
a = Solution()
print(a.canJump([2,0,0]))