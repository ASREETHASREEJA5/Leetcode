class Solution:
    def fairCandySwap(self, a: List[int], b: List[int]) -> List[int]:
        d = (sum(b)-sum(a))//2
        for i in a:
            if i+d in b:
                return [i,i+d]
        