from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        prefix_val = [0] * (n + 1)   # formed number from non-zero digits
        prefix_sum = [0] * (n + 1)   # sum of non-zero digits
        prefix_cnt = [0] * (n + 1)   # count of non-zero digits

        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        for i, ch in enumerate(s):
            d = int(ch)

            prefix_val[i + 1] = prefix_val[i]
            prefix_sum[i + 1] = prefix_sum[i]
            prefix_cnt[i + 1] = prefix_cnt[i]

            if d != 0:
                prefix_val[i + 1] = (prefix_val[i] * 10 + d) % MOD
                prefix_sum[i + 1] += d
                prefix_cnt[i + 1] += 1

        ans = []

        for l, r in queries:
            left_val = prefix_val[l]
            right_val = prefix_val[r + 1]

            non_zero_count = prefix_cnt[r + 1] - prefix_cnt[l]

            x = (right_val - left_val * pow10[non_zero_count]) % MOD
            digit_sum = prefix_sum[r + 1] - prefix_sum[l]

            ans.append((x * digit_sum) % MOD)

        return ans