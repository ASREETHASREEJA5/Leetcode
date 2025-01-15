from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = []
        d = Counter(nums)
        s_keys = [key for key,freq in d.most_common()]
        for i in s_keys:
            if len(l)<k:
                l.append(i)
        return l
        