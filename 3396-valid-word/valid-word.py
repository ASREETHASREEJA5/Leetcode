class Solution:
    def isValid(self, word: str) -> bool:
        vo = ['a','e','i','o','u','A','E','I','O','U']
        c = 0
        v = 0
        for i in word:
            if i in vo:
                c += 1
            elif i.isalpha() and i not in vo:
                v+=1        
        
        if len(word)>=3 and word.isalnum():
            if c>0 and v>0:
                return True
        return False
        