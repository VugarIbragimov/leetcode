from typing import List

nums = [1, 2, 3]
targ = 4


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(numbers):
            remaining = target - numbers[i]
            if remaining in seen:
                return [seen[remaining]+1, i+1]
            else:
                seen[value] = i


test = Solution.twoSum(Solution, numbers=nums, target=targ)
print(test)
