from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        answer = 0

        def dfs(node: int) -> tuple[int, int]:
            visited[node] = True
            vertices = 1
            degree_sum = len(graph[node])

            for neighbour in graph[node]:
                if not visited[neighbour]:
                    child_vertices, child_degree_sum = dfs(neighbour)
                    vertices += child_vertices
                    degree_sum += child_degree_sum

            return vertices, degree_sum

        for node in range(n):
            if not visited[node]:
                vertices, degree_sum = dfs(node)

                # Every undirected edge is counted twice in degree_sum
                edges_in_component = degree_sum // 2
                required_edges = vertices * (vertices - 1) // 2

                if edges_in_component == required_edges:
                    answer += 1

        return answer