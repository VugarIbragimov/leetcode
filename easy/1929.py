# 1929. Concatenation of Array
from typing import List


class Solution():
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_list = []
        n = len(nums)
        for v in range(2*n):
            new_list.append(nums[v % n])
        return new_list


nums = [1, 3, 2, 1]
test = Solution()
test_1 = test.getConcatenation(nums)
print(test_1)
