from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def maxActiveSectionsAfterTrade(
        self,
        s: str,
        queries: List[List[int]]
    ) -> List[int]:

        n = len(s)
        total_ones = s.count('1')

        # Store every consecutive block of 1s as [start, end].
        starts = []
        ends = []

        i = 0
        while i < n:
            if s[i] == '0':
                i += 1
                continue

            start = i

            while i < n and s[i] == '1':
                i += 1

            starts.append(start)
            ends.append(i - 1)

        m = len(starts)

        # No 1-block exists, so no trade is possible.
        if m == 0:
            return [total_ones] * len(queries)

        # full_gain[j] is the gain obtained by choosing the j-th 1-block
        # when both adjacent zero-blocks are completely available.
        full_gain = [0] * m

        for j in range(m):
            previous_end = ends[j - 1] if j > 0 else -1
            next_start = starts[j + 1] if j + 1 < m else n

            left_zeros = starts[j] - previous_end - 1
            right_zeros = next_start - ends[j] - 1

            full_gain[j] = left_zeros + right_zeros

        # Segment tree for range maximum of full_gain.
        size = 1
        while size < m:
            size *= 2

        tree = [0] * (2 * size)

        for j in range(m):
            tree[size + j] = full_gain[j]

        for j in range(size - 1, 0, -1):
            tree[j] = max(tree[2 * j], tree[2 * j + 1])

        def range_max(left: int, right: int) -> int:
            """Maximum full gain from index left to right."""
            if left > right:
                return 0

            left += size
            right += size
            result = 0

            while left <= right:
                if left % 2 == 1:
                    result = max(result, tree[left])
                    left += 1

                if right % 2 == 0:
                    result = max(result, tree[right])
                    right -= 1

                left //= 2
                right //= 2

            return result

        def clipped_gain(j: int, query_left: int, query_right: int) -> int:
            """
            Calculates the gain for a boundary 1-block whose adjacent
            zero-block may be cut by the query boundaries.
            """
            previous_end = ends[j - 1] if j > 0 else -1
            next_start = starts[j + 1] if j + 1 < m else n

            full_left = starts[j] - previous_end - 1
            full_right = next_start - ends[j] - 1

            available_left = starts[j] - query_left
            available_right = query_right - ends[j]

            left_gain = min(full_left, available_left)
            right_gain = min(full_right, available_right)

            return left_gain + right_gain

        answer = []

        for left, right in queries:
            # The chosen 1-block must not touch either query boundary.
            # start > left and end < right.
            first = bisect_right(starts, left)
            last = bisect_left(ends, right) - 1

            if first > last:
                answer.append(total_ones)
                continue

            best_gain = clipped_gain(first, left, right)

            if first != last:
                best_gain = max(
                    best_gain,
                    clipped_gain(last, left, right)
                )

                # Middle blocks have complete zero-blocks on both sides.
                best_gain = max(
                    best_gain,
                    range_max(first + 1, last - 1)
                )

            answer.append(total_ones + best_gain)

        return answer