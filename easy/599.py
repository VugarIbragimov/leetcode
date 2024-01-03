# 599 Minimum Index Sum of Two Lists
from typing import List


class Solution():
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        sum_index = {}
        common = set(list1) & set(list2)
        for i, v in enumerate(list1):
            if v in common:
                sum_index[v] = i
        for i, v in enumerate(list2):
            if v in common:
                sum_index[v] += i
        min_sum = min(sum_index.values())
        return [r for r, s in sum_index.items() if s == min_sum]


a = ['asd', 'baran', 'polyak' 'dagestan']
b = ['drf', 'polyak', 'dagestan', 'asd']
test = Solution()
test_1 = test.findRestaurant(a, b)
print(test_1)
