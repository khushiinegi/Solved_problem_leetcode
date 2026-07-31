class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        active = s.count('1')
        t = '1' + s + '1'

        groups = []
        i = 0

        # Store consecutive groups as: [character, length]
        while i < len(t):
            j = i

            while j < len(t) and t[j] == t[i]:
                j += 1

            groups.append((t[i], j - i))
            i = j

        max_gain = 0

        # Look for pattern: zero block + one block + zero block
        for i in range(1, len(groups) - 1):
            if (
                groups[i][0] == '1'
                and groups[i - 1][0] == '0'
                and groups[i + 1][0] == '0'
            ):
                gain = groups[i - 1][1] + groups[i + 1][1]
                max_gain = max(max_gain, gain)

        return active + max_gain