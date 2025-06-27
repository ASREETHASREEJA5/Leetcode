class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) !=len(t):
            return False
        s_to_t = {}
        t_to_s = {}
        for i,j in zip(s,t):
            if i in s_to_t:
                if s_to_t[i] !=j:
                    return False
            else:
                s_to_t[i] = j

            if j in t_to_s:
                if t_to_s[j] !=i:
                    return False
            else:
                t_to_s[j] = i
        return True

        