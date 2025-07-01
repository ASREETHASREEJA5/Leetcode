class Solution:
    def possibleStringCount(self, word: str) -> int:
        if set(word) == word:
            return 1
        elif len(set(word)) == 1:
            return len(word)
        else:
            c = len(word)
            for i in range(1,len(word)):
                if word[i] != word[i-1]:
                    c-=1
        return c



        