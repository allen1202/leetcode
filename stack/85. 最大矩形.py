class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0

        n = len(matrix)
        m = len(matrix[0])

        heights = [0] * m
        maxarea = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    heights[j] = heights[j] + 1

                else:
                    heights[j] = 0

            maxarea = max(maxarea, self.largestRectangleArea(heights))

        return maxarea

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