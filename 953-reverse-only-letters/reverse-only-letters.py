class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l = []
        for i in s:
            if i.isalpha():
                l.append(i)
        ans = ""
        for i in range(len(s)):
            if s[i].isalpha():
                ans+=l.pop()
            else:
                ans+=s[i]
        return ans

        