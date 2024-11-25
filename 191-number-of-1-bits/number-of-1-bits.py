class Solution:
    def hammingWeight(self, n: int) -> int:
        a = list(bin(n))
        c = 0
        for i in a:
            if i == '1':
                c+=1
        return c
        
        