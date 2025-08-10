from itertools import permutations
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def pow2(n):
            return n > 0 and (n & (n - 1)) == 0
        s = str(n)
        if n==1:
            return True
        l = list(s)
        for i in permutations(l):
            n1 = int("".join(i))
            if len(str(n1)) == len(s) and pow2(n1):
                return True
        return False

        