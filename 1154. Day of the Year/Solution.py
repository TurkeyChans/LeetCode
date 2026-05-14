#Time O(1)
#Space O(1)
import calendar
class Solution:
    def dayOfYear(self, date: str) -> int:
        ans = 0
        num = [31,28,31,30,31,30,31,31,30,31,30,31]
        if calendar.isleap(int(date[:4])):
            num[1] += 1
        ans += sum(num[i] for i in range(int(date[5:7])-1))
        return ans + int(date[-2:]) 
