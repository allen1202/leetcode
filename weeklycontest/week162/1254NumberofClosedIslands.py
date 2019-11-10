class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        no = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    self.dfs(grid, i, j)
                    res += 1

        for i in range(len(grid)):
            if grid[i][0] == 3:
                self.dfs1(grid, i, 0)
                res -= 1

            if grid[i][len(grid[0]) - 1] == 3:
                self.dfs1(grid, i, len(grid[0]) - 1)
                res -= 1

        for j in range(len(grid[0])):
            if grid[0][j] == 3:
                self.dfs1(grid, 0, j)
                res -= 1

            if grid[len(grid) - 1][j] == 3:
                self.dfs1(grid, len(grid) - 1, j)
                res -= 1

        return res

    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 0:
            return

        grid[i][j] = 3
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)

    def dfs1(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 3:
            return

        grid[i][j] = 4
        self.dfs1(grid, i + 1, j)
        self.dfs1(grid, i - 1, j)
        self.dfs1(grid, i, j + 1)
        self.dfs1(grid, i, j - 1)
