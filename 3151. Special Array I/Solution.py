class Solution:
    #Time O(N)
    #Space O(1)
    def isArraySpecial(self, nums: List[int]) -> bool:
        Old = True
        Even = True
        for i in nums:
            if Old and (i % 2 == 1):
                Even = True
                Old = False
            elif Even and (i % 2 == 0):
                Even = False
                Old = True
            else:
                return False
        return True
