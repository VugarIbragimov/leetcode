from typing import List


class Solution():
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.helper([], nums, result)
        return result

    def helper(self, curr, nums, result):

        if len(curr) == len(nums):
            result.append(curr.copy())
            return

        for num in nums:
            if num not in curr:
                curr.append(num)
                self.helper(curr, nums, result)
                curr.pop()


nums = [1, 2, 3]

test = Solution()
test_1 = test.permute(nums)
print(test_1)
