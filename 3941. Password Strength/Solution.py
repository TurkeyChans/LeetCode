class Solution:
    # Time O(N)
    # Space O(1)
    def passwordStrength(self, password: str) -> int:
        d1 = set()
        ans = 0
        for i in password:
            if i.islower() and i not in d1:
                d1.add(i)
                ans += 1
            elif i.isupper() and i not in d1:
                d1.add(i)
                ans += 2
            elif i.isdigit() and i not in d1:
                d1.add(i)
                ans += 3
            elif i in {'!', '@', '#' , '$'} and i not in d1:
                d1.add(i)
                ans += 5
        return ans
