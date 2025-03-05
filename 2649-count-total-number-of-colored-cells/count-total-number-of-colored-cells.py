class Solution:
    def coloredCells(self, n: int) -> int:
        ans = 1
        def colorc(n):
            if n == 1:
                return 1
            return colorc(n-1)+(4*(n-1))
        return colorc(n)
        