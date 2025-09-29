from collections import defaultdict, deque
from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        rev_graph = defaultdict(list)
        outdegree = [0] * n

        # Build reverse graph & outdegree count
        for u in range(n):
            for v in graph[u]:
                rev_graph[v].append(u)
            outdegree[u] = len(graph[u])

        # Queue for terminal nodes (outdegree = 0)
        q = deque([i for i in range(n) if outdegree[i] == 0])
        safe = [False] * n

        while q:
            node = q.popleft()
            safe[node] = True
            for prev in rev_graph[node]:
                outdegree[prev] -= 1
                if outdegree[prev] == 0:
                    q.append(prev)

        # Collect safe nodes
        return [i for i in range(n) if safe[i]]
