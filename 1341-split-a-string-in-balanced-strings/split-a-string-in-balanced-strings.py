class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c = 0
        r = 0
        l = 0
        for i in s:
            if i == 'L':
                l+=1
            else:
                r+=1
            if l == r:
                c+=1
        return c

