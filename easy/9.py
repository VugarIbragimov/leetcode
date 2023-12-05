num = -121


def isPalindrome(x: int) -> bool:

    if x < 0:
        return False

    if int(str(x)[::-1]) == x:
        return True
    return False


ad = isPalindrome(num)

print(ad)
