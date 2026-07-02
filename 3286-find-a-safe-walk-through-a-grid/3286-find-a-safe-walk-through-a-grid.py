from collections import deque
from typing import List

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        health -= grid[0][0]

        if health <= 0:
            return False

        maxHealth = [[-1] * n for _ in range(m)]
        maxHealth[0][0] = health

        q = deque([(0, 0, health)])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c, h = q.popleft()

            if r == m - 1 and c == n - 1:
                return True

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    newHealth = h - grid[nr][nc]

                    if newHealth > 0 and newHealth > maxHealth[nr][nc]:
                        maxHealth[nr][nc] = newHealth
                        q.append((nr, nc, newHealth))

        return False