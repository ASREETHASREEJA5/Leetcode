class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for i in strs:
            s_w = "".join(sorted(i))
            mp[s_w].append(i)
        return list(mp.values())
        