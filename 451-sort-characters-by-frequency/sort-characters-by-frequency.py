from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        d = Counter(s)
        keys = [(key,freq) for key,freq in d.most_common()]
        s = ""
        for i in keys:
            for j in range(i[1]):
                s+=i[0]
        return s
        
        