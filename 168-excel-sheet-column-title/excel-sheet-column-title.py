class Solution:
    def convertToTitle(self, c: int) -> str:
        if c<=26:
            return chr(64+c)
        ans = ""
        while c>0:
            c-=1
            rem = c%26
            ans = chr(65+rem)+ans
            c //=26
        return ans




        