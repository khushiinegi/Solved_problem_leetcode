from collections import deque

class Solution:
    def findMaxPathScore(self, edges, online, k):
        n = len(online)

        if not edges:
            return -1

        graph = [[] for _ in range(n)]
        indeg = [0] * n

        for u, v, cost in edges:
            graph[u].append((v, cost))
            indeg[v] += 1

        # topological sort
        q = deque()
        for i in range(n):
            if indeg[i] == 0:
                q.append(i)

        topo = []
        while q:
            node = q.popleft()
            topo.append(node)

            for nei, cost in graph[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)

        def can(score):
            dist = [float('inf')] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == float('inf'):
                    continue

                if u != 0 and u != n - 1 and not online[u]:
                    continue

                for v, cost in graph[u]:
                    if cost < score:
                        continue

                    if v != n - 1 and not online[v]:
                        continue

                    if dist[u] + cost < dist[v]:
                        dist[v] = dist[u] + cost

            return dist[n - 1] <= k

        low = 0
        high = max(cost for _, _, cost in edges)
        ans = -1

        while low <= high:
            mid = (low + high) // 2

            if can(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans