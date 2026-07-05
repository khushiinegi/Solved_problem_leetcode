class Solution:
    def pathsWithMaxScore(self, board):
        MOD = 10**9 + 7
        n = len(board)

        score = [[-1] * n for _ in range(n)]
        count = [[0] * n for _ in range(n)]

        score[n-1][n-1] = 0
        count[n-1][n-1] = 1

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if board[i][j] == 'X':
                    continue

                if i == n - 1 and j == n - 1:
                    continue

                best = -1
                ways = 0

                # From down, right, down-right
                directions = [(i + 1, j), (i, j + 1), (i + 1, j + 1)]

                for x, y in directions:
                    if x < n and y < n and score[x][y] != -1:
                        if score[x][y] > best:
                            best = score[x][y]
                            ways = count[x][y]
                        elif score[x][y] == best:
                            ways = (ways + count[x][y]) % MOD

                if best == -1:
                    continue

                val = 0
                if board[i][j].isdigit():
                    val = int(board[i][j])

                score[i][j] = best + val
                count[i][j] = ways % MOD

        if score[0][0] == -1:
            return [0, 0]

        return [score[0][0], count[0][0]]