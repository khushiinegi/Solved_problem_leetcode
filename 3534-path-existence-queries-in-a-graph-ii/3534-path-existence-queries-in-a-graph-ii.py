from typing import List


class Solution:
    def pathExistenceQueries(
        self,
        n: int,
        nums: List[int],
        maxDiff: int,
        queries: List[List[int]]
    ) -> List[int]:

        # Sort nodes according to values
        order = sorted(range(n), key=lambda i: nums[i])
        values = [nums[i] for i in order]

        # Position of each original node in sorted order
        pos = [0] * n
        for i, node in enumerate(order):
            pos[node] = i

        # far[i] = farthest sorted position reachable in one edge
        far = [0] * n
        r = 0
        for l in range(n):
            if r < l:
                r = l
            while r + 1 < n and values[r + 1] - values[l] <= maxDiff:
                r += 1
            far[l] = r

        # Connected components
        comp = [0] * n
        for i in range(1, n):
            comp[i] = comp[i - 1]
            if values[i] - values[i - 1] > maxDiff:
                comp[i] += 1

        # Binary lifting
        LOG = n.bit_length()
        jump = [far]

        for _ in range(1, LOG):
            prev = jump[-1]
            cur = [0] * n
            for i in range(n):
                cur[i] = prev[prev[i]]
            jump.append(cur)

        ans = []

        for u, v in queries:
            a = pos[u]
            b = pos[v]

            if a > b:
                a, b = b, a

            if a == b:
                ans.append(0)
                continue

            if comp[a] != comp[b]:
                ans.append(-1)
                continue

            cur = a
            dist = 0

            for k in range(LOG - 1, -1, -1):
                if jump[k][cur] < b:
                    cur = jump[k][cur]
                    dist += 1 << k

            ans.append(dist + 1)

        return ans