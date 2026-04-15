import sys
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(0)
        num3 = int(num1)
        num4 = int(num2)
        ans = str(num3+num4)
        return ans
