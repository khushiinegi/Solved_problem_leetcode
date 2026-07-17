from typing import List
from bisect import bisect_right


class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_value = max(nums)

        # Frequency of every number
        freq = [0] * (max_value + 1)

        for num in nums:
            freq[num] += 1

        # exact_gcd[g] = number of pairs whose GCD is exactly g
        exact_gcd = [0] * (max_value + 1)

        # Process larger GCDs first
        for g in range(max_value, 0, -1):
            divisible_count = 0

            # Count numbers divisible by g
            for multiple in range(g, max_value + 1, g):
                divisible_count += freq[multiple]

            # All pairs where both numbers are divisible by g
            pair_count = divisible_count * (divisible_count - 1) // 2

            # Remove pairs having GCD 2g, 3g, ...
            for multiple in range(2 * g, max_value + 1, g):
                pair_count -= exact_gcd[multiple]

            exact_gcd[g] = pair_count

        # prefix[g] = number of GCD pairs having value <= g
        prefix = [0] * (max_value + 1)

        for g in range(1, max_value + 1):
            prefix[g] = prefix[g - 1] + exact_gcd[g]

        answer = []

        for query in queries:
            # query is 0-indexed.
            # bisect_right finds first prefix value greater than query.
            gcd_value = bisect_right(prefix, query)
            answer.append(gcd_value)

        return answer