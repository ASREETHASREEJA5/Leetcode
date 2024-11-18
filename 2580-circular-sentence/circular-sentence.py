class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        l = sentence.split()
        if len(l) == 1:
            if sentence[0] == sentence[-1]:
                return True
            else:
                return False
        for i in range(len(l)-1):
            a = l[i]
            if a[-1] != l[i+1][0] :
                return False
        if l[-1][-1] == l[0][0]:
            return True
        else:
            return False
            
        