class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        stack = [-1]
        maxarea = 0
        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                index = stack.pop()
                maxarea = max(maxarea, (i - stack[-1] - 1) * heights[index])

            stack.append(i)
        return maxarea