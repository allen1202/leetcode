class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        right = len(height) - 1
        maxarea = 0
        while left < right:
            if height[left] < height[right]:
                maxarea = max(maxarea, (right - left) * height[left])
                left += 1

            else:
                maxarea = max(maxarea, (right - left) * height[right])
                right -= 1

        return maxarea