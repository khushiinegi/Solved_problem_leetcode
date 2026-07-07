class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        total = 0

        for digit in str(n):
            if digit != '0':
                x = x * 10 + int(digit)
                total += int(digit)

        return x * total
        