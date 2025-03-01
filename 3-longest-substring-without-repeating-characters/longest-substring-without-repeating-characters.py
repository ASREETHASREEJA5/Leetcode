class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            c = [s[i]]
            for j in range(i+1,len(s)):
                if s[j] not in c:
                    c.append(s[j])
                else:
                    break
            max_len = max(max_len,len(c))
        return max_len

        