class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count={'a': 0, 'b': 0, 'c': 0}
        res,left=0,0
        for right in range(len(s)):
            count[s[right]]+=1
            while all(count[a]>0 for a in "abc"):
                res+=len(s)-right
                count[s[left]]-=1
                left+=1
        return res


        