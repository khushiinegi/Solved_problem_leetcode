from typing import List
from math import gcd


class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        maximum = max(nums)

        # dp[g1][g2] = number of ways to obtain these two GCDs
        dp = [[0] * (maximum + 1) for _ in range(maximum + 1)]
        dp[0][0] = 1

        for x in nums:
            new_dp = [[0] * (maximum + 1)
                      for _ in range(maximum + 1)]

            for g1 in range(maximum + 1):
                for g2 in range(maximum + 1):
                    ways = dp[g1][g2]

                    if ways == 0:
                        continue

                    # Choice 1: Do not use x
                    new_dp[g1][g2] = (
                        new_dp[g1][g2] + ways
                    ) % MOD

                    # Choice 2: Add x to seq1
                    new_g1 = gcd(g1, x)
                    new_dp[new_g1][g2] = (
                        new_dp[new_g1][g2] + ways
                    ) % MOD

                    # Choice 3: Add x to seq2
                    new_g2 = gcd(g2, x)
                    new_dp[g1][new_g2] = (
                        new_dp[g1][new_g2] + ways
                    ) % MOD

            dp = new_dp

        answer = 0

        for g in range(1, maximum + 1):
            answer = (answer + dp[g][g]) % MOD

        return answer