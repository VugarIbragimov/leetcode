# 463. Island Perimeter
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Initialize perimeter to 0
        perimeter = 0

        # Loop through each cell in the grid
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    # Check the cell's neighbors and
                    # add to perimeter accordingly
                    if i == 0 or grid[i-1][j] == 0:
                        perimeter += 1
                    if j == 0 or grid[i][j-1] == 0:
                        perimeter += 1
                    if i == len(grid)-1 or grid[i+1][j] == 0:
                        perimeter += 1
                    if j == len(grid[i])-1 or grid[i][j+1] == 0:
                        perimeter += 1

        return perimeter


a = [[0, 1, 0], [0, 1, 0], [1, 0, 0]]
test = Solution()
test_1 = test.islandPerimeter(a)
print(test_1)
