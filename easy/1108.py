class Solution():
    def defangIPaddr(self, address: str) -> str:
        """
        :type address: str
        :rtype: str
        """
        return address.replace(".", "[.]")


address = "1.1.1.1"
test = Solution()
test_1 = test.defangIPaddr(address)
print(test_1)
