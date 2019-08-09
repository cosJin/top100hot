class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        maximum = min(height[i],height[j]) * (j - i)
        while i < j:
            if height[i] <= height[j]:
                i+=1
                maximum = max(maximum,min(height[i],height[j]) * (j - i))
            elif height[i] > height[j]:
                j-=1
                maximum = max(maximum,min(height[i],height[j]) * (j - i))
        return maximum
a = Solution()
print(a.maxArea([]))