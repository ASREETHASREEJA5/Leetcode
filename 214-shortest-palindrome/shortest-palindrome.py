class Solution:
    def shortestPalindrome(self, s: str) -> str:
        s1 = s[::-1]
        for i in range (len(s)+1):
            if s.startswith(s1[i:]):
                return s1[:i]+s
        
        