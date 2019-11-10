class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        nums = [[0] * m for _ in range(n)]

        for index in indices:
            x = index[0]
            for i in range(m):
                nums[x][i] += 1

            y = index[1]

            for j in range(n):
                nums[j][y] += 1

        res = 0

        for i in range(n):
            for j in range(m):
                if nums[i][j] % 2 != 0:
                    res += 1

        return res