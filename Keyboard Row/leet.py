from typing import List
#SPACE = O(N)
#TIME = O(N * M)
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        row_one = "qwertyuiop"
        row_two = "asdfghjkl"
        row_three = "zxcvbnm"
        one = set()
        two = set()
        three = set()
        for k in range(len(row_one)):
            one.add(row_one[k])
        for j in range(len(row_two)):
            two.add(row_two[j])
        for l in range(len(row_three)):
            three.add(row_three[l])
        
        for i in range(len(words)):
            temps = str(words[i])
            temp = temps.lower()
            row_b_one = False 
            row_b_two = False 
            row_b_three = False
            for s in range(len(temp)):
                if((temp[s] in one) and not row_b_two and not row_b_three):
                    row_b_one = True
                    if(s == len(temp)-1):
                        ans.append(temps)
                elif((temp[s] in two) and not row_b_one and not row_b_three):
                    row_b_two = True
                    if(s == len(temp)-1):
                        ans.append(temps)
                elif((temp[s] in three) and not row_b_two and not row_b_one):
                    row_b_three = True
                    if(s == len(temp)-1):
                        ans.append(temps)
                else:
                    break
        return ans

            


s1 = Solution()
print(s1.findWords(["omk"]))