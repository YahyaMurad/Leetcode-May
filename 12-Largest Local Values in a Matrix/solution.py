class Solution:
    def largestLocal(self, grid):
        kernel = [
            (0, 0), (0, 1), (0, 2),
            (1, 0), (1, 1), (1, 2),
            (2, 0), (2, 1), (2, 2),
        ]
        res = []

        for i in range(len(grid) - 2):
            res.append([])
            for j in range(len(grid[0]) - 2):
                largest = float("-INF")
                for x, y in kernel:
                    largest = max(largest, grid[i + x][j + y])

                res[-1].append(largest)
        
        return res
