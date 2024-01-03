from typing import List


class Solution():
    def buildArray(self, nums: List[int]) -> List[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new_list = []
        for x in range(len(nums)):
            new_list.append(nums[nums[x]])
        return new_list


nums = [0, 2, 1, 5, 3, 4]
test = Solution()
test_1 = test.buildArray(nums)
print(test_1)
