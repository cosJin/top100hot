class Solution(object):
    def trap2(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #方法一：一层一层的看，先看最底层，统计有多少个0，再看第二层....
        #当层数太大的时候超时了。
        res = 0
        while height.count(0) != len(height):
            ceng = [c!=0 for c in height]
            height = [c-1 if c != 0 else 0 for c in height]
            stack = []
            for k in range(len(ceng)):
                if ceng[k] == 1:
                    if stack != []:
                        res += k - stack.pop() - 1
                    stack.append(k)
        return res
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #方法一：一层一层的看，先看最底层，统计有多少个0，再看第二层....
        #当层数太大的时候超时了。
        #方法二：前后两遍遍历数组，分别保存左侧最大值，和右侧最大值，然后计算每个节点可存储的水量
        #另外还有个很巧妙的算法，在discuss里面。
        left = []
        right = []
        res = 0
        leng = len(height)
        leftmax = 0
        rightmax = 0
        for i in range(leng):
            left.append(leftmax)
            leftmax = max(leftmax, height[i])
            right.append(rightmax)
            rightmax = max(rightmax, height[leng-1-i])
        for i in range(leng):
            water = min(left[i],right[leng-1-i])
            if water - height[i] > 0:
                res += water - height[i]
        return res

a = Solution()
print(a.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
