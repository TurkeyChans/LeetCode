class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        #Time O(N * M)
        #Space O(N * M)
        ans = [[0] * n for _ in range(m)]
        count = 0
        l = len(original)
        if n*m > l or n*m < l:
            return []
        for i in range(m):
            for j in range(n):
                ans[i][j] = original[count]
                count += 1
        return ans if count == len(original) else []
