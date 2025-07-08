class Solution:
    def maxProduct(self, n: int) -> int:
        l = []
        while n>0:
            rem = n%10
            l.append(rem)
            n = n//10
        l.sort(reverse = True)
        print(l)
        return int(l[0])*int(l[1])
        