class Solution:
    def longestPalindrome(self, s: str) -> str:
        c = 0
        s1 = s[0]
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i] == s[j]:
                    a = s[i:j+1] 
                    if a == a[::-1] and j-i+1>c:
                        c = j-i+1
                        s1 = s[i:j+1]
        return s1



        