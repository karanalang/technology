class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = [c for c in s if c.isalnum()]
        print(r)
        i1 = 0
        i2 = len(r)-1
        print("i2//2 -> ", i2//2)
        for i in range(int(round(i2/2))):
            print(" i => ", i)
            # print(" <- r[i].lower() -> ", r[i].lower())
            # print(" <- r[i2 - i].lower() -> ", r[i2 - i].lower())
            if r[i].lower() != r[i2 - i].lower():
                return bool(0)

        return bool(1)

# r[0], r[7]
# r[1], r[6]
# r[2], r[5]
# r[3], r[4]




p = Solution()
b = p.isPalindrome("race a car")
print(" isPalindrome => ", b)