class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        w1 = s1.split()
        w2 = s2.split()
        if len(w1)>len(w2):
            w1,w2 = w2,w1
        i = 0
        while i < len(w1) and w1[i] == w2[i]:
            i+=1
        j = 0
        while j < len(w1) and w1[-(j+1)] == w2[-(j+1)]:
            j+=1
        return i+j>=len(w1)

        