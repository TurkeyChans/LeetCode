class Solution:
    #Time O(N)
    #Space O(1)
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vowel = False
        Consonant = False
        a = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
        for i in word:
            if not(i.isdigit()) and not(i.isalpha()):
                return False
            elif i in a:
                vowel = True
            elif i not in a and i.isalpha():
                Consonant = True
        return vowel and Consonant
