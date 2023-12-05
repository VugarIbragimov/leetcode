from typing import List


class Solution(object):
    def plusOne(self, digits: List) -> List:
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = ''
        for num in digits:
            n += str(num)
        k = str(int(n) + 1)

        return [int(k[i]) for i in range(len(k))]
