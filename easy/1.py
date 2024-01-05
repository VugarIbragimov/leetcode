from typing import Any, List

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

a = -27 // 4
print(a)


class Singleton(object):
    _instance = None

    def __new__(cls_, *args, **kwargs):
        if not isinstance(cls_._instance, cls_):
            cls_._instance = object.__new__(cls_, *args, **kwargs)
        return cls_._instance
