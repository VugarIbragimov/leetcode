from typing import List


class Solution():
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        value = 0
        for x in range(len(operations)):
            if operations[x] == "X++" or operations[x] == "++X":
                value += 1
            if operations[x] == "--X" or operations[x] == "X--":
                value -= 1
        return value


operations = ["--X", "X++", "X++"]
test = Solution()
test_1 = test.finalValueAfterOperations(operations)
print(test_1)
