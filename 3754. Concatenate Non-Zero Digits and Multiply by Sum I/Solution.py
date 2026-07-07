class Solution:
    def sumAndMultiply(self, n: int) -> int:
    #Time O(n)
    #Space O(n)
        a = str(n)
        b = ""
        sums = 0
        if n == 0:
            return 0
        for i in a:
            if i != "0":
                sums += int(i)
                b += i
        return int(b) * sums
