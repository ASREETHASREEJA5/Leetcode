class Solution:
    def findOrder(self, n: int, p: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        ind = [0]*n
        for a,b in p:
            graph[b].append(a)
            ind[a]+=1
        q = deque([i for i in range(n) if ind[i]==0])
        ans = []
        while q:
            a = q.popleft()
            ans.append(a)
            for i in graph[a]:
                ind[i]-=1
                if ind[i]==0:
                    q.append(i)
        s = []
        if len(ans)==n:
            return ans
        else:
            return s


        