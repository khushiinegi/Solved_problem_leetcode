from typing import List
from math import gcd

class Solution:
    def gcdSum(self, nums: List[int]) -> int:
        prefix_gcd = []
        current_max = 0
        for num in nums:
            current_max = max(current_max, num)
            prefix_gcd.append(gcd(num, current_max))
        prefix_gcd.sort()

        left = 0
        right = len(prefix_gcd) - 1
        answer = 0
        while left < right:
            answer += gcd(prefix_gcd[left], prefix_gcd[right])
            left += 1
            right -= 1

        return answer