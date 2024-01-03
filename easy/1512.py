# 1512. Number of Good Pairs
from typing import List


class Solution():
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j:
                    counter += 1
        return counter


nums = [1, 2, 3, 1, 1, 3]
test = Solution()
test_1 = test.numIdenticalPairs(nums)
print(test_1)
