class Solution:
    def sortVowels(self, s: str) -> str:
        vowels =list("aeiouAEIOU")
        v=[]
        temp=""
        for i in s:
            if i in vowels:
                v.append(i)
        v= sorted(v)
        n=0
        for i in s:
            if i not in vowels:
                temp+=i
            else:
                temp+=v[n]
                n+=1
        return temp



