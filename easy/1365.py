# 1365. How Many Numbers Are Smaller Than the Current Number
from typing import List


class Solution():
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new_list = []
        lst = sorted(nums)
        for i in nums:
            new_list.append(lst.index(i))
        return new_list


nums = [8, 1, 2, 2, 3]
test = Solution()
test_1 = test.smallerNumbersThanCurrent(nums)
print(test_1)
# Output: [4,0,1,1,3]
