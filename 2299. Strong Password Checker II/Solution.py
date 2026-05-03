class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        #Time O(N)
        #Space O(1)
        lower = False
        upper = False
        digit = False
        Special = False
        if len(password) < 8:
            return False
        for i in range(len(password)):
            if password[i].islower():
                lower = True
            elif password[i].isupper():
                upper = True
            elif password[i].isdigit():
                digit = True
            elif password[i] in "!@#$%^&*()-+":
                Special = True
            if i != len(password)-1:
                if password[i] == password[i+1]:
                    return False
        return True if lower and upper and digit and Special else False
