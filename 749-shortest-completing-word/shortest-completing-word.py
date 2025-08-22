class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        words = ["".join(w.lower()) for w in words]
        chars = "".join(ch.lower() for ch in licensePlate if ch.isalpha())
        need = Counter(chars)
        ans = None
        for i in words:
            w_c = Counter(i)
            if all(w_c[j]>=need[j] for j in need):
                if ans is None or len(ans)>len(i):
                    ans = i
        return ans
            

        