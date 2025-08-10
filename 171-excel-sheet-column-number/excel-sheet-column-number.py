class Solution:
    def titleToNumber(self, c: str) -> int:
        ans = 0
        c = c[::-1]
        for i in range(len(c)):
            ans+=(26**i)*(ord(c[i])-64)
        return ans

        