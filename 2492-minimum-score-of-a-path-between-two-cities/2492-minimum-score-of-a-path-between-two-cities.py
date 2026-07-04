class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n + 1)]

        for a, b, d in roads:
            graph[a].append((b, d))
            graph[b].append((a, d))

        visited = [False] * (n + 1)
        stack = [1]
        visited[1] = True
        ans = float("inf")

        while stack:
            city = stack.pop()

            for nei, dist in graph[city]:
                ans = min(ans, dist)

                if not visited[nei]:
                    visited[nei] = True
                    stack.append(nei)

        return ans