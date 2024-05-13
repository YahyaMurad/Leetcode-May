class Solution:
    def matrixScore(self, grid):
        for i in range(len(grid)):
            if grid[i][0] == 0:
                for j in range(len(grid[i])):
                    grid[i][j] ^= 1

        for i in range(len(grid[0])):
            one_count = 0
            for j in range(len(grid)):
                one_count += grid[j][i]

            if one_count < len(grid) - one_count:
                for j in range(len(grid)):
                    grid[j][i] ^= 1

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += grid[i][j] << (len(grid[0]) - j - 1)

        return res



sol = Solution()
print(sol.matrixScore([[0,1,1],[1,1,1],[0,1,0]]))