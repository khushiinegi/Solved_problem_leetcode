class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = 1

        # case for 1
        if 1 in freq:
            ans = max(ans, freq[1] if freq[1] % 2 == 1 else freq[1] - 1)

        for x in freq:
            if x == 1:
                continue

            cur = x
            length = 0

            while cur in freq:
                if freq[cur] >= 2:
                    length += 2
                    cur = cur * cur
                else:
                    length += 1
                    break

            # pattern length must be odd
            if length % 2 == 0:
                length -= 1

            ans = max(ans, length)

        return ans