class Solution():
    def isAnagram(self, s: str, t: str) -> bool:

        return sorted(s) == sorted(t)


s = "anagram"
t = "nagaram"
test = Solution()
test_1 = test.isAnagram(s, t)
print(test_1)
